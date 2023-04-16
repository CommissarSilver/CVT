import pycode_similar
import os

target_path = (
    "/Users/ahura/Nexus/CVT/CWE_replication/cwe-89/codeql-eg-SqlInjection-a/gen_scenario"
)
# get all the python files in the target path
python_files = [
    os.path.join(target_path, name)
    for name in os.listdir(target_path)
    if name.endswith(".py")
]
for filename_a in python_files:
    for filename_b in python_files:
        if filename_a != filename_b:
            x = pycode_similar.detect(
                [open(filename_a, "r").read(), open(filename_b, "r").read()],
                diff_method=pycode_similar.UnifiedDiff,
                keep_prints=False,
                module_level=False,
            )
            if x[0][1][0].plagiarism_percent > 0.9:
                print(
                    f"{filename_a.split('/')[-1]}",
                    f"{filename_b.split('/')[-1]}",
                )
