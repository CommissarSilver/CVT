#!/usr/bin/env python3

import copy
import json
import os
import re
import subprocess

ql_cmd = "codeql database create {db_name} --language=python --overwrite --source-root ./{src_root} && codeql database analyze {db_name} {query_src} --format=csv --output={dest_path}"


def get_mark_setups(src_dir: str) -> [dict[str, str]]:
    mark_setups = []

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file == "mark_setup.json":
                mark_setup_dict = json.load(os.path.join(root, file))

                for dir_path in dirs:
                    if "gen" in dir_path:
                        re_str = "gen_([a-zA-Z0-9_]+)"
                        mat = re.search(re_str, dir_path)
                        if mat and mat.group(1) != "scenario":
                            scenario_name = "scenario_" + mat.group(1)
                        else:
                            scenario_name = "scenario"

                        mark_dict = copy.deepcopy(mark_setup_dict)


def main():
    # get files to test
    # build codeql command
    # open a subprocess to run the command
    # redirect output to stdout
    pass


if __name__ == "__main__":
    main()
