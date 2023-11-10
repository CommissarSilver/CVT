from decimal import DivisionByZero
import os, ast, re, shutil
from python_comparison import get_significant_subtrees, compare_subtrees


def script_builder(path):
    # list each .txt file in the directory
    files = [f for f in os.listdir(path) if f.endswith(".txt")]
    for file in files:
        # open each file and read the content
        # split the content into a list
        with open(path + "/" + file, "r") as f:
            content = f.read()
            # copilot uses ======= to separate the suggested codes
            content = content.split("=======")
            # build a python file for each suggested code
            for solution_num, solution in enumerate(content):
                filename = file.replace(".txt", "") + "_" + str(solution_num) + ".py"
                with open(path + "/PyScripts/" + filename, "w+") as py_script:
                    py_script.write(solution)


def generate_python_scripts_from_txt(path):
    # for each folder in the path list the subfolders
    j = list(os.listdir(path))
    for folder in os.listdir(path):
        if folder.startswith(".") or folder.endswith(".py") or folder.endswith(".txt"):
            pass
        # for each subfolder if PyScript folder doesn't exist in it, create it
        else:
            for subfolder in os.listdir(path + "/" + folder):
                if not os.path.exists(path + "/" + folder + "/" + subfolder + "/PyScripts"):
                    if not (
                        subfolder.startswith(".")
                        or subfolder.endswith(".py")
                        or subfolder.endswith(".txt")
                        or subfolder.endswith(".xlsx")
                        or subfolder.endswith(".md")
                    ):
                        os.mkdir(path + "/" + folder + "/" + subfolder + "/PyScripts")
                        script_builder(path + "/" + folder + "/" + subfolder)


# script_builder("CoPilot_on_Algorithm_Design/Sorting_Algorithms/Bucket_Sort")
# generate_python_scripts_from_txt(os.path.join(os.getcwd(), "CoPilot_on_Algorithm_Design"))


i = 6
path = "CoPilot_on_Algorithm_Design/Greedy_Algorithms/All_in_One_Go/PyScripts"


for code_path in os.listdir(path):
    with open(path + "/" + code_path, "r") as source:
        t1str = source.read()
        t1str_mod = re.sub(r"(\"{2,3}[\s\n]*)(?:.*?[\s\n]*)*([\n\s]*\"{2,3})", r"", t1str, flags=re.MULTILINE)
        try:
            tree1 = ast.parse(t1str_mod, mode="exec")
        except SyntaxError:
            continue

    subtree_list1 = get_significant_subtrees(tree1)
    for other_code_path in os.listdir(path):
        if code_path != other_code_path:

            similarity = 0
            with open(path + "/" + other_code_path, "r") as source2:
                t2str = source2.read()
                t1str_mod = re.sub(r"(\"{2,3}[\s\n]*)(?:.*?[\s\n]*)*([\n\s]*\"{2,3})", r"", t1str, flags=re.MULTILINE)
                try:
                    tree2 = ast.parse(t2str, mode="exec")
                except SyntaxError:
                    continue

            subtree_list2 = get_significant_subtrees(tree2)
            try:
                similarity = compare_subtrees(subtree_list1, subtree_list2, 10000)[0]
            except ZeroDivisionError:
                similarity = 0
            print(f"The index of similarity between prog1  and prog2 is: { similarity }")
            with open(path + "/" + "comparison_results.csv", "a+") as comp_results:
                comp_results.write(code_path + "," + other_code_path + "," + str(similarity) + "\n")

