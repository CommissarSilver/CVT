import os
import re

def paths_list(dir_path):
    path_list = []
    for file_name in os.listdir(dir_path):
        code_path = dir_path + "/" + file_name
        path_list.append(code_path)
    
    return path_list

def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

CWE_list= ['cwe-20']
for cwe in CWE_list:
    code_path = os.path.join(
        os.getcwd(),
        "CWE_replication",
        cwe,
        "",
        )
    
               
    print(code_path)
    imediate_dir= get_immediate_subdirectories(code_path)
    for dir in imediate_dir:
        print(dir)
        raw_dir = os.path.join( code_path,
                               dir, "copilot_raw",
                               "", )
        print(raw_dir)
        dst_path = os.path.join( code_path, dir, "gen_scenario", "", )

        with open (os.path.join(code_path, dir, "scenario.py"), "r") as myfile:
            scenario = myfile.read()
        path_list = []
        path_list = paths_list(raw_dir)

        token_1 = '===='
        token_2="Synthesizing"
        chunks = {}
        current_chunk = []
        file_name_hlp = "Copilot_" + dir 
        i=1
        for path in path_list:
            with open (path, "r") as myfile:
                #file_name = code_path.split("/")[-1]
                data=myfile.readlines()
            for line in data:
                if line.startswith(token_1):
                   file_name = file_name_hlp + "_" +str(i)
                   i=i+1
                   current_chunk = []
                   chunks[file_name] = current_chunk
                else:
                   if not (line.startswith(token_2)):
                       current_chunk.append(line)

        for name, storage in chunks.items():
            
            if len(storage)>0 and not (all(elem == '\n' for elem in storage)):
                content = scenario + "\n".join(storage)
                print(name)
                #print(storage)
                with open(os.path.join(dst_path, name+'.py'), 'w') as file:
                    file.write("".join(content))
                    file.close()
                


    

    