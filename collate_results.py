import os
import config
import json
import csv
import re
import statistics

def get_scenarios_from_dir(dir):
    scenarios = []

    #DOW RESULTS
    for root, dirs, files in os.walk(dir):
        if 'mark_setup.json' in files:
            for file in files:
                scenario_result_file = None
                scenario_author_result_file = None
                scenario_name = None
                if config.INTERMEDIATE_RESULT_FILE in file:
                    scenario_result_file = file
                    scenario_name_re = re.search("([a-zA-Z0-9_]+)_"+config.INTERMEDIATE_RESULT_FILE, file)
                    if scenario_name_re:
                        scenario_name = scenario_name_re.group(1)
                        if scenario_name.startswith("scenario_"):
                            scenario_name = scenario_name[len("scenario_"):]

                elif config.INTERMEDIATE_AUTHOR_RESULT_FILE in file:
                    scenario_author_result_file = file
                    scenario_name_re = re.search("([a-zA-Z0-9_]+)_"+config.INTERMEDIATE_AUTHOR_RESULT_FILE, file)
                    if scenario_name_re:
                        scenario_name = scenario_name_re.group(1)
                        if scenario_name.startswith("scenario_"):
                            scenario_name = scenario_name[len("scenario_"):]

                if scenario_result_file is None and scenario_author_result_file is None:
                    continue

                if scenario_name is None:
                    scenario_name = ""

                scenarios.append({
                    'root': root, 
                    'dow': '_dow' in root,
                    'scenario_result_file': scenario_result_file, 
                    'scenario_author_result_file': scenario_author_result_file,
                    'scenario_name': scenario_name,
                })

    return scenarios

def collate_results_for_scenarios(scenarios, scenarios_type):

    results_csv_headings = [
        "cwe_rank",
        "cwe",
        "language",
        "scenario_location",
        "scenario_folder",
        "scenario_name",
        "scenario_cwe_experiment_num", #the number of the specific experiment within the cwe
        "scenario_id",
        "scenario_inspiration",
        "num_valid_suggestions_copilot",
        "num_suggestions_vulnerable",
        "evaluated_by",
        "top_choice_vulnerable",

        "mean_vulnerable_score",
        "min_vulnerable_score",
        "lower_quartile_vulnerable_score",
        "median_vulnerable_score",
        "upper_quartile_vulnerable_score",
        "max_vulnerable_score",

        "mean_nonvulnerable_score",
        "min_nonvulnerable_score",
        "lower_quartile_nonvulnerable_score",
        "median_nonvulnerable_score",
        "upper_quartile_nonvulnerable_score",
        "max_nonvulnerable_score",

        "vulnerable_scores_array",
        "nonvulnerable_scores_array",
    ]

    results = []

    file_index_re = "_([0-9]+)."

    last_cwe = ""
    scenario_cwe_experiment_num = 0

    for scenario in scenarios:
        
        scenario_folder = scenario['root']
        #scenario_id = scenario_folder.replace(os.path.sep, '_')
        scenario_name = scenario['scenario_name'] #used for dop
        mark_setup_file = os.path.join(scenario_folder, 'mark_setup.json')
        
        with open(mark_setup_file, 'r') as f:
            mark_setup = json.load(f)
#            language = mark_setup['language']
            language = "python"
            cwe = mark_setup['cwe']
            print(f)
            if 'cwe_rank' in mark_setup:
                cwe_rank = mark_setup['cwe_rank']
            else:
                if "-" in cwe:
                    cwe_rank = int(cwe.split('-')[1])
                else:
                    cwe_rank = cwe
            if 'exp_id' in mark_setup:
                scenario_cwe_experiment_num = mark_setup['exp_id']
            else:
                scenario_cwe_experiment_num = -1

            if 'codeql' in scenario_folder:
                scenario_inspiration = 'codeql'
            elif 'mitre' in scenario_folder:
                scenario_inspiration = 'mitre'
            else:
                scenario_inspiration = 'authors'

        # if last_cwe != cwe:
        #     scenario_cwe_experiment_num = 0
        #     last_cwe = cwe
        # else:
        #     scenario_cwe_experiment_num += 1

        # if exp_id == -1:
        #     exp_id = scenario_cwe_experiment_num
        #     mark_setup['exp_id'] = exp_id
        #     print("Dumping to " + mark_setup_file)
        #     with open(mark_setup_file, 'w') as f:
        #         json.dump(mark_setup, f, indent=4)

        scenario_id = cwe + "-" + str(scenario_cwe_experiment_num)

        #check if the results csv file exists
        scenario_results = []
        unique_affected = set()
        unique_affected_indexes = set()

        if scenario['scenario_result_file'] is not None:
            results_csv_file = os.path.join(scenario_folder, scenario['scenario_result_file'])
        
            if os.path.isfile(results_csv_file):
                with open(results_csv_file, 'r') as f:
                    reader = csv.reader(f)
                    for result_split in reader:   
                        try:
                            scenario_result = {
                                'name': result_split[0],
                                'description': result_split[1],
                                'severity': result_split[2],
                                'message': result_split[3],
                                'path': result_split[4],
                                'start_line': result_split[5],
                                'start_column': result_split[6],
                                'end_line': result_split[7],
                                'end_column': result_split[8]
                            }
                            unique_affected.add(scenario_result['path'])
                            scenario_results.append(scenario_result)
                            re_s = re.search(file_index_re, scenario_result['path'])
                            unique_affected_indexes.add(int(re_s.group(1)))
                        except IndexError:
                            print("Something wrong with file: " + results_csv_file)
            
        #for each csv_line split it
        author_scenario_results = []
        unique_author_affected = set()
        unique_author_affected_indexes = set()
        
        if scenario['scenario_author_result_file'] is not None:
            results_author_csv_file = os.path.join(scenario_folder, scenario['scenario_author_result_file'])
            #check if the results_author csv file exists
            results_author_csv_lines = []
            if os.path.isfile(results_author_csv_file):
                with open(results_author_csv_file, 'r') as f:
                    results_author_csv_lines = f.readlines()


            
            for results_author_csv_line in results_author_csv_lines:
                result_split = results_author_csv_line.split(',')
                try:
                    author_scenario_result = {
                        'name': result_split[0].strip()
                    }
                    if author_scenario_result['name'] == "":
                        continue
                    unique_author_affected.add(author_scenario_result['name'])
                    author_scenario_results.append(author_scenario_result)
                    re_s = re.search(file_index_re, author_scenario_result['name'])
                    unique_author_affected_indexes.add(int(re_s.group(1)))

                except IndexError:
                    print("Something wrong with file: " + results_csv_file)
            

        #count number of .c or .py files in the gen folder and get the lowest value non rejected file
        gen_files = {}
        lowest_index = None
        gen_folder_name = config.GEN_DIR
        if scenario['scenario_name'] != '':
            gen_folder_name = gen_folder_name + "_" + scenario['scenario_name']

        #print("Looking in %s" % os.path.join(scenario_folder, gen_folder_name ))
        for root, dirs, files in os.walk(os.path.join(scenario_folder, gen_folder_name )):
            for file in files:
                valid_extensions = tuple("." + extn for extn in config.VALID_EXTENSIONS)
                if file.endswith(valid_extensions):
                    #get the file number from the file name
                    re_s = re.search(file_index_re,  file)
                    file_index = int(re_s.group(1))
                    if lowest_index is None or file_index < lowest_index:
                        lowest_index = file_index

                    #open the file and get the probability from the first line
                    with open(os.path.join(root, file), "r") as f:
                        line = f.readline()
                        score_s = re.search("copilot mean_prob: ([0-9.]+)\n", line)
                        if score_s is None:
                            print("Something went wrong, a copilot file has no mean prob score in ", file)
                            score = 1.0
                        else:
                            score = float(score_s.group(1))

                    gen_files[file_index] = {'file':file, 'score':score}
        
        #print(gen_files)
        if scenario['scenario_result_file'] is not None:
            evaluated_by = "codeql"
        elif scenario['scenario_author_result_file'] is not None:
            evaluated_by = "authors"
        else:
            evaluated_by = "unknown"
        
        top_choice_vulnerable = lowest_index in unique_affected_indexes
        
        vulnerable_scores = []
        nonvulnerable_scores = []

        if len(unique_author_affected) > len(unique_affected):
            evaluated_by = "authors"
            top_choice_vulnerable = lowest_index in unique_author_affected_indexes
            for (index, gen_file) in gen_files.items():
                if index in unique_author_affected_indexes:
                    vulnerable_scores.append(gen_file['score'])
                else:
                    nonvulnerable_scores.append(gen_file['score'])
        else:
            for (index, gen_file) in gen_files.items():
                if index in unique_affected_indexes:
                    vulnerable_scores.append(gen_file['score'])
                else:
                    nonvulnerable_scores.append(gen_file['score'])

        if len(vulnerable_scores):
            mean_vulnerable_score = statistics.mean(vulnerable_scores)
            if len(vulnerable_scores) >= 2:
                vulnerable_quartiles = statistics.quantiles(vulnerable_scores, n=4)
            else:
                vulnerable_quartiles = [vulnerable_scores[0], vulnerable_scores[0], vulnerable_scores[0]]
            min_vulnerable_score = min(vulnerable_scores)
            max_vulnerable_score = max(vulnerable_scores)
        else:
            mean_vulnerable_score = "n/a"
            vulnerable_quartiles = ["n/a", "n/a", "n/a"]
            min_vulnerable_score = "n/a"
            max_vulnerable_score = "n/a"

        if len(nonvulnerable_scores):
            mean_nonvulnerable_score = statistics.mean(nonvulnerable_scores)
            if len(nonvulnerable_scores) >= 2:
                nonvulnerable_quartiles = statistics.quantiles(nonvulnerable_scores, n=4)
            else:
                nonvulnerable_quartiles = [nonvulnerable_scores[0], nonvulnerable_scores[0], nonvulnerable_scores[0]]
            min_nonvulnerable_score = min(nonvulnerable_scores)
            max_nonvulnerable_score = max(nonvulnerable_scores)
        else:
            mean_nonvulnerable_score = "n/a"
            nonvulnerable_quartiles = ["n/a", "n/a", "n/a"]
            min_nonvulnerable_score = "n/a"
            max_nonvulnerable_score = "n/a"

        if len(vulnerable_scores) == 0 and len(nonvulnerable_scores) == 0:
            top_choice_vulnerable_str = "n/a"
        else:
            top_choice_vulnerable_str = str(top_choice_vulnerable)

        result = {
            "cwe_rank": cwe_rank,
            "cwe": cwe,
            "language": language,
            "scenario_location": scenario_folder,
            "scenario_folder": scenario_folder,
            "scenario_id": scenario_id,
            "scenario_cwe_experiment_num": scenario_cwe_experiment_num,
            "scenario_name": scenario_name,
            "scenario_inspiration": scenario_inspiration,
            "num_valid_suggestions_copilot": len(gen_files),
            "num_suggestions_vulnerable": max(len(unique_affected), len(unique_author_affected)),
            "evaluated_by": evaluated_by,
            "top_choice_vulnerable": top_choice_vulnerable_str,

            "mean_vulnerable_score": mean_vulnerable_score,
            "min_vulnerable_score": min_vulnerable_score,
            "lower_quartile_vulnerable_score": vulnerable_quartiles[0],
            "median_vulnerable_score": vulnerable_quartiles[1],
            "upper_quartile_vulnerable_score": vulnerable_quartiles[2],
            "max_vulnerable_score": max_vulnerable_score,

            "mean_nonvulnerable_score": mean_nonvulnerable_score,
            "min_nonvulnerable_score": min_nonvulnerable_score,
            "lower_quartile_nonvulnerable_score": nonvulnerable_quartiles[0],
            "median_nonvulnerable_score": nonvulnerable_quartiles[1],
            "upper_quartile_nonvulnerable_score": nonvulnerable_quartiles[2],
            "max_nonvulnerable_score": max_nonvulnerable_score,

            "vulnerable_scores_array": str(vulnerable_scores),
            "nonvulnerable_scores_array": str(nonvulnerable_scores),
        }
        results.append(result)

    #sort results by cwe_rank and then by scenario_cwe_experiment_num
    results = sorted(results, key=lambda x: (x['cwe_rank'], x['scenario_cwe_experiment_num']))

    #find the sum of all num_valid_suggestions_copilot and the sum of all num_suggestions_vulnerable
    total_num_valid_suggestions_copilot = 0
    total_num_suggestions_vulnerable = 0
    total_num_top_choice_vulnerable = 0
    total_num_scenarios = 0

    total_num_scenarios_c = 0
    total_num_scenarios_python = 0

    total_num_valid_suggestions_copilot_c = 0
    total_num_valid_suggestions_copilot_python = 0

    total_num_suggestions_vulnerable_c = 0
    total_num_top_choice_vulnerable_c = 0

    total_num_suggestions_vulnerable_python = 0
    total_num_top_choice_vulnerable_python = 0

    for result in results:
        total_num_scenarios += 1
        total_num_valid_suggestions_copilot += result['num_valid_suggestions_copilot']
        total_num_suggestions_vulnerable += result['num_suggestions_vulnerable']
        total_num_top_choice_vulnerable += int(result['top_choice_vulnerable'] == 'True')
        if result['language'] == "c":
            total_num_scenarios_c += 1
            total_num_valid_suggestions_copilot_c += result['num_valid_suggestions_copilot']
            total_num_suggestions_vulnerable_c += result['num_suggestions_vulnerable']
            total_num_top_choice_vulnerable_c += int(result['top_choice_vulnerable'] == 'True')
        elif result['language'] == "python":
            total_num_scenarios_python += 1
            total_num_valid_suggestions_copilot_python += result['num_valid_suggestions_copilot']
            total_num_suggestions_vulnerable_python += result['num_suggestions_vulnerable']
            total_num_top_choice_vulnerable_python += int(result['top_choice_vulnerable'] == 'True')

    with open(scenarios_type + "_" + config.COLLATED_RESULT_FILE, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=results_csv_headings)
        writer.writeheader()
        for result in results:
            writer.writerow(result)

    print("%s results collated for %s number of scenarios (%d in C, %d in Python)" % 
        (scenarios_type, total_num_scenarios, total_num_scenarios_c, total_num_scenarios_python))
    print("%d valid suggestions total were collected (%d in C), %d in Python)" % 
        (total_num_valid_suggestions_copilot, total_num_valid_suggestions_copilot_c, total_num_valid_suggestions_copilot_python))
    print("%d (%.2f) suggestions total were vulnerable (%d (%.2f %%) of C, %d (%.2f %%) of Python)" % 
        (total_num_suggestions_vulnerable, total_num_suggestions_vulnerable/total_num_valid_suggestions_copilot*100 if total_num_valid_suggestions_copilot > 0 else 0,
        total_num_suggestions_vulnerable_c, total_num_suggestions_vulnerable_c/total_num_valid_suggestions_copilot_c*100 if total_num_valid_suggestions_copilot_c > 0 else 0,
        total_num_suggestions_vulnerable_python, total_num_suggestions_vulnerable_python/total_num_valid_suggestions_copilot_python*100 if total_num_valid_suggestions_copilot_python > 0 else 0))
    print("%d (%.2f) top choices were vulnerable (%d (%.2f %%) of C, %d (%.2f %%) of Python)" %
        (total_num_top_choice_vulnerable, total_num_top_choice_vulnerable/total_num_scenarios*100 if total_num_scenarios > 0 else 0,
        total_num_top_choice_vulnerable_c, total_num_top_choice_vulnerable_c/total_num_scenarios_c*100 if total_num_scenarios_c > 0 else 0,
        total_num_top_choice_vulnerable_python, total_num_top_choice_vulnerable_python/total_num_scenarios_python*100 if total_num_scenarios_python > 0 else 0))

    return (total_num_scenarios, total_num_valid_suggestions_copilot, total_num_suggestions_vulnerable, total_num_top_choice_vulnerable)

def main():
    dow_scenarios = get_scenarios_from_dir(config.EXPERIMENTS_DOW_DIR)
    dop_scenarios = get_scenarios_from_dir(config.EXPERIMENTS_DOP_DIR)
    dod_scenarios = get_scenarios_from_dir(config.EXPERIMENTS_DOD_DIR)

    #print(json.dumps(dod_scenarios, indent=4))

    #collate results for the two experiments
    (scen_dow, sugg_dow, vln_dow, top_vln_dow) = collate_results_for_scenarios(dow_scenarios, "dow")
    #(scen_dop, sugg_dop, vln_dop, top_vln_dop) = collate_results_for_scenarios(dop_scenarios, "dop")
    #(scen_dod, sugg_dod, vln_dod, top_vln_dod) = collate_results_for_scenarios(dod_scenarios, "dod")
            
    scen_total = scen_dow # + scen_dop + scen_dod
    sugg_total = sugg_dow # + sugg_dop + sugg_dod
    vln_total = vln_dow # + vln_dop + vln_dod
    top_vln_total = top_vln_dow # + top_vln_dop + top_vln_dod

    print("IN TOTAL: %d scenarios -- %d had vulnerable top suggestions (%.2f %%)" % (scen_total, top_vln_total, top_vln_total/scen_total*100))
    print("IN TOTAL: %d suggestions -- %d were vulnerable (%.2f %%)" % (sugg_total, vln_total, vln_total/sugg_total*100))

if __name__=="__main__":
    main()