# -*- coding : utf -8 -*-
""" Module for AST program comparison .

 This module implements functions for comparing .py files .
5 It uses abstract syntax trees from the built in module ’ast ’.
6
7 """

import ast
from _ast import *
import re

from munkres import Munkres


def compare_ASTs(ast_a: AST, ast_b: AST, reorder_depth: int) -> int:
    """ Compare two ASTs corresponding to python programs .
18 Args :
19 ast_a : The first program AST to compare .
20 ast_b : The first program AST to compare .
21 reorder_depth : The maximum children reorder depth for better
22 performance .
23
24 Returns :
25 True if the ASTs are equivalent , otherwise False .
26 """

    children_a = list(ast.iter_child_nodes(ast_a))
    # fffg
    children_b = list(ast.iter_child_nodes(ast_b))

    if (type(ast_a) == type(ast_b)) and len(list(children_a)) == 0 and len(list(children_b)) == 0:
        return 1

    if (type(ast_a) != type(ast_b)) or (len(children_a) != len(children_b)):
        return 0

    if reorder_depth == 0:
        match_index = sum(
            map(lambda pairs: compare_ASTs(pairs[0], pairs[1], reorder_depth), zip(children_a, children_b))
        )
        return match_index + 1

    elif reorder_depth > 0:
        match_index = reorder_children_compare(ast_a, ast_b, reorder_depth - 1)
        return match_index + 1

    return 0


def reorder_children_compare(ast_a: AST, ast_b: AST, reorder_depth: int) -> int:
    """ Reorders child nodes and compares them .
    56 Args :
    ast_a : The first AST for child comparison .
    ast_b : The second AST for child comparison .
    reorder_depth : The maximum children reorder depth for better
    performance .
    Returns :
    True if there is a way to match 1 -1 every child node of ast_a
    with every child node of ast_b , otherwise False ."""
    comparison_matrix = []
    cost_matrix = []
    best_match_value = 0
    children_a = list(ast.iter_child_nodes(ast_a))
    children_b = list(ast.iter_child_nodes(ast_b))
    if len(children_a) <= 1 or len(children_b) <= 1:
        for child_a in children_a:
            for child_b in children_b:
                best_match_value += compare_ASTs(child_a, child_b, reorder_depth)
    else:
        for child_a in children_a:
            row = []
            cost_row = []
            for child_b in children_b:
                similarity = compare_ASTs(child_a, child_b, reorder_depth)
                row.append(similarity)
                cost_row.append(10000000 - similarity)
            comparison_matrix.append(row)
            cost_matrix.append(cost_row)

        m = Munkres()
        indices = m.compute(cost_matrix)

        for row, col in indices:
            best_match_value += comparison_matrix[row][col]

    return best_match_value


def compare_subtrees(sig_subtrees_p1: list, sig_subtrees_p2: list, reorder_depth: int) -> tuple:

    """ Compare two lists of subtrees .
    Args :
    sig_subtrees_p1 : The first list of subtrees to compare .
    sig_subtrees_p2 : The second list of subtrees to compare .
    reorder_depth : The maximum children reorder depth for better
    performance .
    Returns :
    True if the subtrees are equivalent , otherwise False ."""

    comparison_matrix = []
    cost_matrix = []
    best_match = []
    best_match_value = 0
    best_match_weight = 0
    children_a = sig_subtrees_p1.copy()
    children_b = sig_subtrees_p2.copy()

    if len(children_a) <= 1 or len(children_b) <= 1:
        try:
            for child_a in children_a:
                best_match += [child_a]
                for child_b in children_b:
                    best_match_value += compare_ASTs(child_a, child_b, reorder_depth)
                    best_match += 1
        except:
            pass
    else:
        for child_a in children_a:
            row = []
            cost_row = []
            for child_b in children_b:
                similarity = compare_ASTs(child_a, child_b, reorder_depth)
                row.append(similarity)
                cost_row.append(10000000 - similarity)
            comparison_matrix.append(row)
            cost_matrix.append(cost_row)

        m = Munkres()
        indices = m.compute(cost_matrix)

        for row, col in indices:
            best_match_weight += apply_weights_to_subtrees_mult(
                comparison_matrix[row][col], sig_subtrees_p1[row], sig_subtrees_p2[col]
            )
            best_match += [sig_subtrees_p1[row], sig_subtrees_p2[col]]

    all_subtrees_weight = sum(
        map(lambda tree: apply_weights_to_subtrees(get_num_nodes(tree), tree), sig_subtrees_p1)
    ) + sum(map(lambda tree: apply_weights_to_subtrees(get_num_nodes(tree), tree), sig_subtrees_p2))

    similarity = 2 * best_match_weight / all_subtrees_weight
    return round(similarity, 4), best_match


def get_significant_subtrees(root: AST) -> list:
    """ Find the significant subtrees of an AST .
    Args :
    root : The root of the main AST.
    Returns :
    A list with all the significant subtrees of root ."""
    significant_subtrees = []
    for node in ast.walk(root):
        if is_significant(node):
            significant_subtrees.append(node)

    return significant_subtrees


def is_significant(root: AST) -> bool:
    """ Check if the root of the AST is significant .
    Args :
    root : The root of the AST to check .
    Returns :
    True if the root is significant , otherwise False ."""

    return (
        isinstance(root, Import)
        or isinstance(root, FunctionDef)
        or isinstance(root, If)
        or isinstance(root, ClassDef)
        or isinstance(root, While)
        or isinstance(root, For)
        or isinstance(root, comprehension)
        or isinstance(root, Return)
    )


def get_num_nodes(root: AST) -> int:
    """ Get the number of nodes in the AST .
    Args :
    root : The root of the AST to get the number of nodes from .
    Returns :
    The number of nodes in the AST ."""
    return len(list((ast.walk(root))))


def apply_weights_to_subtrees(weight: float, subtree: AST) -> float:
    """ Apply weights to the subtrees .
    Args :
    weight : The weight to apply to the subtrees .
    subtree : The subtree to apply the weight to .
    Returns :
    The subtree with the weight applied ."""
    new_weight = weight
    if isinstance(subtree, Import):
        new_weight *= 0.3
    elif isinstance(subtree, Module):
        new_weight *= 1
    elif isinstance(subtree, FunctionDef):
        new_weight *= 1.2
    elif isinstance(subtree, If):
        new_weight *= 0.5
    elif isinstance(subtree, ClassDef):
        new_weight *= 1
    elif isinstance(subtree, While):
        new_weight *= 1
    elif isinstance(subtree, For):
        new_weight *= 1
    elif isinstance(subtree, comprehension):
        new_weight *= 1
    elif isinstance(subtree, Return):
        new_weight *= 1
    return new_weight


def apply_weights_to_subtrees_mult(weight: float, ast_1: AST, ast_2: AST) -> float:
    """ Find the average weight of both trees in order to weigh the comparison .
    Args :
    weight : The weight of the comparison .
    ast_1 : The first compared tree .
    ast_2 : The second compared tree .
    Returns
    The average of the subtrees ’ weights ."""
    if weight == 0:
        return 0
    else:
        return (apply_weights_to_subtrees(weight, ast_1) + apply_weights_to_subtrees(weight, ast_2)) / 2

