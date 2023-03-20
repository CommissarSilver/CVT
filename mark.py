#!/usr/bin/env python3

"""
Author: M. Joshua Bishop
 - based on a script by Hammond Pearce et al.
"""

import copy
import json
import os
import re
import subprocess


def get_mark_setups(src_dir: str) -> [dict[str, str]]:
    mark_setups = []

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file == "mark_setup.json":
                mark_setup_dict = json.load(open(os.path.join(root, file), "r"))

                for dir_path in dirs:
                    if "gen" in dir_path:
                        re_str = "gen_([a-zA-Z0-9_]+)"
                        mat = re.search(re_str, dir_path)
                        if mat and mat.group(1) != "scenario":
                            scenario_name = "scenario_" + mat.group(1)
                        else:
                            scenario_name = "scenario"

                        mark_dict = copy.deepcopy(mark_setup_dict)
                        mark_dict["root"] = root
                        mark_dict["setup_file_name"] = file
                        mark_dict["dir_path"] = dir_path
                        mark_dict["scenario_name"] = scenario_name

                        mark_setups.append(mark_dict)

    return mark_setups


def main():
    # get files to test
    mark_setups = get_mark_setups("./CWE_replication")
    print(mark_setups)

    for mark_setup in mark_setups:
        if "query" not in mark_setup:
            continue

        db_name = "codeql_db"
        results_csv_name = "codeql_results.csv"
        if mark_setup.get("scenario_name", "") != "":
            db_name = mark_setup.get("scenario_name") + f"_{db_name}"
            results_csv_name = mark_setup.get("scenario_name") + f"_{results_csv_name}"

        results_path = os.path.join(mark_setup["root"], results_csv_name)
        if os.path.isfile(os.path.join(results_path)):
            print(f"Results file exists, skipping: {results_path}")
            continue

        root = mark_setup["root"]
        db_path = os.path.join(root, db_name)
        src_root = os.path.join(root, mark_setup["dir_path"])
        query_src = mark_setup["query"]
        csv_path = os.path.join(root, results_csv_name)

        # build codeql command
        ql_cmd = "codeql database create {db_name} --language=python --overwrite --source-root ./{src_root} && codeql database analyze {db_name} {query_src} --format=csv --output={dest_path} --download"

        ql_cmd = ql_cmd.format(
            db_name=db_path, src_root=root, query_src=query_src, dest_path=csv_path
        )

        print(ql_cmd)
        # open a subprocess to run the command
        p = subprocess.Popen(
            ql_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        r = p.stdout.read().decode("utf-8") + p.stderr.read().decode("utf-8")
        print(r)
        # redirect output to stdout


if __name__ == "__main__":
    main()
