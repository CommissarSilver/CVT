import os, time, subprocess, platform, re, ast
from clank import get_script_contents, get_copilot_suggestions
from python_comparison import get_significant_subtrees, compare_subtrees


def separate_solutions(parent_dir: str, turn_num: int):
    """
    Separate the solutions from the copilot suggestions

    Args:
        parent_dir (str): parent directory of copilot's solutions
        turn_num (int): the turn number of the turn we're in to keep track of solutions
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
            # remove the lines that start with a #
            f = re.sub(r"^[#].*$", "", f, flags=re.MULTILINE)
            # separate the solutions if there is a line with '==' or more in it
            f = re.split(f".*===.*", f)

        # write the solutions to a file
        for solution_num, solution_text in enumerate(f):
            final_solution = orginal_scenario + solution_text
            ## if final scolution is exactly the same as the original, skip it. but first we need to remove the unncessary whitespaces
            if final_solution.replace(" ", "") == orginal_scenario.replace(" ", ""):
                continue
            with open(
                os.path.join(
                    parent_dir,
                    "unique_solutions",
                    f"unique_solution_{turn_num}_{copilot_suggestion_num}_{solution_num}.py",
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
    number_of_duplicate_solutions = 0
    number_of_syntax_errors = 0
    number_of_all_solutions = len(os.listdir(path))

    trees = {}
    for code_path in os.listdir(path):
        with open(path + "/" + code_path, "r") as source:
            t1str = source.read()
            pattern = re.compile(r"\"{3}[\s\S]*?\"{3}[\n\s]*", re.DOTALL)
            t1str_mod = pattern.sub(r"", t1str)
            try:
                trees[code_path] = ast.parse(t1str_mod, mode="exec")
            except SyntaxError:
                os.remove(os.path.join(path, code_path))
                number_of_syntax_errors += 1

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

        if value > 0.9:
            duplicates[source]["similars"].append(target)
            duplicates[source]["similarity"] = value
            duplicate_keys.add(tuple(sorted((source, target))))

        comp_results.write(source + "," + target + "," + str(value) + "\n")
    comp_results.close()

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
                pattern = re.compile(r"\"{3}.*?\"{3}\n?", re.DOTALL)
                t1str_mod = pattern.sub("", t1str)

            try:
                ast.parse(t1str_mod, mode="exec")
            except SyntaxError:
                os.remove(os.path.join(par_dir, code_path))


if __name__ == "__main__":
    #! REMINDER: This need to be done MANUALLY
    #! REMINDER: TEMPRATURE NEEDS TO BE CHANGED AND SET MANUALLY AND THEN THIS NEEDS TO BE RE-RUN
    #! REMINDER: check the solutions for too many synthesize statements. It'll mess everything up
    original_paths = get_script_contents(os.path.join(os.getcwd(), "CWE_replication"))
    all_runs = {}
    
    for path in original_paths.keys():
        # path = "/Users/ahura/Nexus/CVT/CWE_replication/cwe-20/codeql-eg-IncompleteUrlSubstringSanitization"
        num_unique_solutions = 0
        turn_num = 0

        # while num_unique_solutions < 10:
        # if turn_num > 0:

        #     get_copilot_suggestions({path: original_paths[path]}, wait_time=10)
        #     print(
        #         "\033[33m"
        #         + f"turn {turn_num}: "
        #         + "\033[0m"
        #         + "\033[34m"
        #         + "copilot suggestions are ready"
        #         + "\033[0m"
        #     )
        # input("Press any key to continue...")

        # separate_solutions(path, turn_num)
        # print(
        #     "\033[33m"
        #     + f"turn {turn_num}: "
        #     + "\033[0m"
        #     + "\033[34m"
        #     + "Separating Solutions"
        #     + "\033[0m"
        # )

        remove_syntax_errors(path + "/gen_scenario")
        print(
            "\033[33m"
            + f"turn {turn_num}: "
            + "\033[0m"
            + "\033[34m"
            + "Removing Syntax Errors"
            + "\033[0m"
        )
        sim_results, duplicates, executable_solutions, run_results = check_similarity(
            path + "/gen_scenario"
        )
        print(
            "\033[33m"
            + f"turn {turn_num}: "
            + "\033[0m"
            + "\033[34m"
            + "Checking Similiarty"
            + "\033[0m"
        )

        remove_duplicates(path + "/gen_scenario", duplicates)
        print(
            "\033[33m"
            + f"turn {turn_num}: "
            + "\033[0m"
            + "\033[34m"
            + "Removing Duplicates"
            + "\033[0m"
        )

        turn_num += 1
        num_unique_solutions = len(os.listdir(path + "/gen_scenario"))
        all_runs[path] = run_results

    final_results = open(
        os.path.join(os.getcwd(), "CWE_replication", "final_results.csv"), "a+"
    )
    final_results.write(
        "CWE" + ","
        "Total Solutions" + ","
        "Number of Duplicates" + ","
        "Number of Problematic Solutions" + "\n"
    )
    for key, value in all_runs.items():
        final_results.write(
            key
            + ","
            + value["total_solutions"]
            + ","
            + value["number_of_duplicates"]
            + ","
            + value["number_of_problematic_solutions"]
            + "\n"
        )
    final_results.close()
