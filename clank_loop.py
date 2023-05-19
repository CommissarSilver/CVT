import os, time, subprocess, platform, re, ast
from clank import get_script_contents, get_copilot_suggestions
from python_comparison import get_significant_subtrees, compare_subtrees
import pycode_similar


def separate_solutions(
    parent_dir: str, turn_num: int, get_solution_confidence: bool = False
):
    """
    Separate the solutions from the copilot suggestions

    Args:
        parent_dir (str): parent directory of copilot's solutions
        turn_num (int): the turn number of the turn we're in to keep track of solutions
    """
    statements_to_remove = ["Synthesizing", "Suggestion"]

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
        cwe_name = copilot_suggestion.split("/")[-4]
        cwe_scenario = copilot_suggestion.split("/")[-3]
        f = open(copilot_suggestion, "r")
        f = f.read()
        for statement in statements_to_remove:
            # remove the entire line that contains the statement_to_remove
            f = re.sub(f".*{statement}.*", "", f)
            # remove the lines that start with a #
        f = re.sub(r"^[#].*$", "", f, flags=re.MULTILINE)
        # separate the solutions if there is a line with '==' or more in it
        f = re.split(f".*===.*", f)

        # write the solutions to a file
        for solution_num, solution_text in enumerate(f):
            final_solution = orginal_scenario + solution_text
            # search for the line that says mean_prob: and store it
            mean_prob = (
                re.search(r"mean_prob:.*", final_solution)
                if get_solution_confidence
                else None
            )
            if mean_prob:
                mean_prob = mean_prob.group(0)
            ## if final scolution is exactly the same as the original, skip it. but first we need to remove the unncessary whitespaces
            if final_solution.replace(" ", "") == orginal_scenario.replace(" ", ""):
                continue
            with open(
                os.path.join(
                    parent_dir,
                    "unique_solutions",
                    f"{cwe_name}_{cwe_scenario}_unique_solution_{turn_num}_{copilot_suggestion_num}_{solution_num}.py",
                ),
                "w",
            ) as k:
                k.write(final_solution)
                k.close()


def check_similarity(path: str):
    """
    Check similarity between all the solutions in the path

    Args:
        path (str): path containing the solutions

    Returns:
        sim_results: similarity score based on AST similarity between the scripts
        duplicates: dictionary containing the duplicate solutions and their similarity score
        executable_solutions: list of executable solutions that do not contain syntax errors

    """
    number_of_syntax_errors = 0

    trees = {}
    for code_path in os.listdir(path):
        with open(path + "/" + code_path, "r") as source:
            t1str = source.read()
            pattern = re.compile(r"\"{3}[\s\S]*?\"{3}[\n\s]*", re.DOTALL)
            t1str_mod = pattern.sub(r"", t1str)
            # if the AST of a script cannot be parsed, then it has a syntax error and not useful
            try:
                trees[code_path] = ast.parse(t1str_mod, mode="exec")
            except SyntaxError:
                os.remove(os.path.join(path, code_path))
                number_of_syntax_errors += 1

    # The similiarity comparisons only do so much. We need to check the final solutions manually.
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

    duplicate_keys = set()
    for key, value in sim_results.items():
        source = key.split(",")[0]
        target = key.split(",")[1]

        if int(value) == 1:
            duplicates[source]["similars"].append(target)
            duplicates[source]["similarity"] = value
            duplicate_keys.add(tuple(sorted((source, target))))

        comp_results.write(source + "," + target + "," + str(value) + "\n")
    comp_results.close()

    # if a is simliar to b and b and c are similar, then a and c are similar as well. we need to check for this
    total_solutions = len([file for file in os.listdir(path) if file.endswith(".py")])
    duplicates_items = {
        x for x, y in duplicate_keys for z, y2 in duplicate_keys if x != z and y == y2
    }

    executable_solutions = []
    for key, value in sim_results.items():
        source = key.split(",")[0]
        target = key.split(",")[1]
        executable_solutions.append(source)
        executable_solutions.append(target)

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
        + str(len(duplicates_items))
        + ","
        + str(number_of_syntax_errors)
        + "\n"
    )
    run_results.close()

    run_results = {
        "total_solutions": str(total_solutions),
        "number_of_duplicates": str(len(duplicates_items)),
        "number_of_problematic_solutions": str(number_of_syntax_errors),
    }
    return sim_results, duplicates, set(executable_solutions), run_results


def remove_duplicates(par_dir: str, duplicates: dict):
    """
    Remove the solutions that are similar to other solutions

    Args:
        par_dir (str): directory containing the solutions
        duplicates (dict): actual duplicate solutions' name
    """
    for source, value in duplicates.items():
        if value["similars"]:
            for target in value["similars"]:
                if os.path.exists(os.path.join(par_dir, target)):
                    os.remove(os.path.join(par_dir, target))


def remove_syntax_errors(
    par_dir: str,
):
    """
    Remove solutions that have syntax errors

    Args:
        par_dir (str): directory containing the solutions
    """
    for code_path in os.listdir(par_dir):
        if code_path.split(".")[-1] == "py":
            with open(par_dir + "/" + code_path, "r") as source:
                t1str = source.read()
                # pattern = re.compile(r"\"{3}.*?\"{3}\n?", re.DOTALL)
                # t1str_mod = pattern.sub("", t1str)

            try:
                ast.parse(t1str, mode="exec")
            except SyntaxError:
                os.remove(os.path.join(par_dir, code_path))


if __name__ == "__main__":
    #! REMINDER: SIMILARITY BETWEEN THE SCRIPTS NEEDS TO BE CHECKED MANUALLY AFTER EXECUTION
    original_paths = get_script_contents(os.path.join(os.getcwd(), "CWE_replication"))
    all_runs = {}

    for path in original_paths.keys():
        # path = "/Users/ahura/Nexus/CVT/CWE_replication/cwe-89/my-eg-2"
        num_unique_solutions = (
            len([i for i in os.listdir(path + "/unique_solutions") if i.endswith(".py")])
            if os.path.exists(os.path.join(path, "unique_solutions"))
            else 0
        )

        print(
            "\033[34m"
            + path
            + ": "
            + "\033[0m"
            + "\033[33m"
            + str(num_unique_solutions)
            + "\033[0m"
        )
        turn_num = 0

        while num_unique_solutions < 10 and turn_num < 2:
            if turn_num > 0:
                get_copilot_suggestions({path: original_paths[path]}, wait_time=10)
                print(
                    "\033[33m"
                    + f"turn {turn_num}: "
                    + "\033[0m"
                    + "\033[34m"
                    + "copilot suggestions are ready"
                    + "\033[0m"
                )

            separate_solutions(path, turn_num)
            print(
                "\033[33m"
                + f"turn {turn_num}: "
                + "\033[0m"
                + "\033[34m"
                + "Separating Solutions"
                + "\033[0m"
            )

            remove_syntax_errors(path + "/unique_solutions")
            print(
                "\033[33m"
                + f"turn {turn_num}: "
                + "\033[0m"
                + "\033[34m"
                + "Removing Syntax Errors"
                + "\033[0m"
            )

            sim_results, duplicates, executable_solutions, run_results = check_similarity(
                path + "/unique_solutions"
            )
            print(
                "\033[33m"
                + f"turn {turn_num}: "
                + "\033[0m"
                + "\033[34m"
                + "Checking Similiarty"
                + "\033[0m"
            )

            remove_duplicates(path + "/unique_solutions", duplicates)
            print(
                "\033[33m"
                + f"turn {turn_num}: "
                + "\033[0m"
                + "\033[34m"
                + "Removing Duplicates"
                + "\033[0m"
            )

            all_runs[path] = run_results
            num_unique_solutions = len(
                [i for i in os.listdir(path + "/unique_solutions") if i.endswith(".py")]
            )
            turn_num += 1

        final_results = open(
            os.path.join(
                os.getcwd(), "CWE_replication", f"loop_final_results_{turn_num}.csv"
            ),
            "a+",
        )
        final_results.write(
            "CWE"
            + ","
            + "Total Solutions"
            + ","
            + "Number of Duplicates"
            + ","
            + "Number of Problematic Solutions"
            + "\n"
        )
        for key, value in all_runs.items():
            final_results.write(
                key.split("/")[-1]
                + ","
                + value["total_solutions"]
                + ","
                + value["number_of_duplicates"]
                + ","
                + value["number_of_problematic_solutions"]
                + "\n"
            )
        final_results.close()
