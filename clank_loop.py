import os, time, subprocess, platform, re, ast
from clank import get_script_contents, get_copilot_suggestions
from python_comparison import get_significant_subtrees, compare_subtrees


def separate_solutions(parent_dir: str):
    """
    Separate the solutions from the copilot suggestions

    Args:
        parent_dir (str): parent directory of copilot's solutions
    """
    statements_to_remove = ["Synthesizing"]
    statements_to_separate = ["======="]
    # get all the files in the copilot_raw directory
    orginal_scenario = open(os.path.join(parent_dir, "scenario.py"), "r").read()
    scripts_dir = [
        os.path.join(parent_dir, "copilot_raw", script)
        for script in os.listdir(os.path.join(parent_dir, "copilot_raw"))
    ]
    # create a directory to store the unique solutions
    if not os.path.exists(os.path.join(parent_dir, "unique_solutions")):
        os.mkdir(os.path.join(parent_dir, "unique_solutions"))
    x = sorted(scripts_dir)
    for copilot_suggestion_num, copilot_suggestion in enumerate(scripts_dir):
        f = open(copilot_suggestion, "r")
        f = f.read()
        for statement in statements_to_remove:
            # remove the entire line that contains the statement_to_remove
            f = re.sub(f".*{statement}.*", "", f)
            # separate the solutions if there is a line with '==' or more in it
            f = re.split(f".*===.*", f)

        # write the solutions to a file
        for solution_num, solution_text in enumerate(f):
            final_solution = orginal_scenario + solution_text
            with open(
                os.path.join(
                    parent_dir,
                    "unique_solutions",
                    f"unique_solution_{copilot_suggestion_num}_{solution_num}.py",
                ),
                "w",
            ) as k:
                k.write(final_solution)
                k.close()


def check_similarity(path):
    trees = {}
    for code_path in os.listdir(path):
        with open(path + "/" + code_path, "r") as source:
            t1str = source.read()
            t1str_mod = re.sub(
                r"(\"{2,3}[\s\n]*)(?:.*?[\s\n]*)*([\n\s]*\"{2,3})",
                r"",
                t1str,
                flags=re.MULTILINE,
            )
            try:
                trees[code_path] = ast.parse(t1str_mod, mode="exec")
            except SyntaxError:
                continue

    sim_results = {}
    for key, tree in trees.items():
        for second_key, second_tree in trees.items():
            if key != second_key:
                subtree_list1 = get_significant_subtrees(tree)
                subtree_list2 = get_significant_subtrees(second_tree)
                try:
                    similarity = compare_subtrees(subtree_list1, subtree_list2, 10000)[0]
                except ZeroDivisionError:
                    similarity = 0
                if (
                    key + "," + second_key not in sim_results.keys()
                    and second_key + "," + key not in sim_results.keys()
                ):
                    sim_results[key + "," + second_key] = similarity

    comp_results = open(path + "/" + "comparison_results.csv", "a+")
    duplicates = {
        source.split(",")[0]: {"similars": [], "similarity": 0}
        for source in sim_results.keys()
    }

    for key, value in sim_results.items():
        source = key.split(",")[0]
        target = key.split(",")[1]
        if value > 0.9:
            duplicates[source]["similars"].append(target)
            duplicates[source]["similarity"] = value

        comp_results.write(source + "," + target + "," + str(value) + "\n")
    comp_results.close()

    total_solutions = len(os.listdir(path)) - 1

    number_of_duplicates = 0
    for key, value in duplicates.items():
        similars_temp = len(value["similars"]) + 1 if value["similars"] else 0
        number_of_duplicates += similars_temp

    number_of_problematic_solutions = 0
    executable_solutions = []
    for key, value in sim_results.items():
        source = key.split(",")[0]
        target = key.split(",")[1]
        executable_solutions.append(source)
        executable_solutions.append(target)

    number_of_problematic_solutions = total_solutions - len(set(executable_solutions))

    run_results = open(path + "/" + "run_results.csv", "a+")
    run_results.write(
        "total_solutions"
        + ","
        + "number_of_duplicates"
        + ","
        + "number_of_problematic_solutions"
        + "\n"
    )
    run_results.write(
        str(total_solutions)
        + ","
        + str(number_of_duplicates)
        + ","
        + str(number_of_problematic_solutions)
        + "\n"
    )
    return sim_results, duplicates, set(executable_solutions)


def remove_duplicates(par_dir: str, duplicates: dict):
    for source, value in duplicates.items():
        if value["similars"]:
            for target in value["similars"]:
                if os.path.exists(os.path.join(par_dir, target)):
                    os.remove(os.path.join(par_dir, target))


def remove_syntax_errors(par_dir: str, executable_solutions: set):
    for solution in os.listdir(par_dir):
        if solution not in executable_solutions:
            os.remove(os.path.join(par_dir, solution))


if __name__ == "__main__":
    original_paths = get_script_contents(os.path.join(os.getcwd(), "CWE_replication"))
    original_paths = list(original_paths.keys())
    for path in original_paths:
        separate_solutions(path)
        sim_results, duplicates, executable_solutions = check_similarity(
            path + "/unique_solutions"
        )
        remove_duplicates(path + "/unique_solutions", duplicates)
        remove_syntax_errors(path + "/unique_solutions", executable_solutions)
    # sim_results, duplicates, executable_solutions = check_similarity(
    #     "/Users/ahura/Nexus/CVT/CWE_replication/cwe-20/codeql-eg-IncompleteUrlSubstringSanitization/unique_solutions"
    # )
    # remove_duplicates(
    #     "/Users/ahura/Nexus/CVT/CWE_replication/cwe-20/codeql-eg-IncompleteUrlSubstringSanitization/unique_solutions",
    #     duplicates,
    # )
    # remove_syntax_errors(
    #     "/Users/ahura/Nexus/CVT/CWE_replication/cwe-20/codeql-eg-IncompleteUrlSubstringSanitization/unique_solutions",
    #     executable_solutions,
    # )
