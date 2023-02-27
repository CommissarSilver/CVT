import os


def paths_list(dir_path):
    path_list = []
    for file_name in os.listdir(dir_path):
        code_path = dir_path + "/" + file_name
        path_list.append(code_path)
    
    return path_list

for q in range(1,5):
    q_num = 'q' + str(q)
    code_path = os.path.join(
        os.getcwd(),
        "Questions",
        q_num,
        "",
        )
    dst_path= os.path.join(
        os.getcwd(),
        "Answers",
        q_num,
        "",
        )

    path_list = []
    path_list = paths_list(code_path)

    token = '======='
    chunks = {}
    current_chunk = []
    i=1
    file_name_hlp = "Copilot_code_"+q_num+"_"
    for path in path_list:
        with open (path, "r") as myfile:
            data=myfile.readlines()

    for line in data:
        if line.startswith(token):
            file_name = file_name_hlp + str(i)
        i=i+1
        current_chunk = []
        #current_chunk.append(line)
        chunks[file_name] = current_chunk
    else:
        current_chunk.append(line)

print (chunks)

for name, storage in chunks.items():
    print(name)
    with open(os.path.join(dst_path, name + '.py'), 'w') as file:
        file.write("".join(storage))
        file.close()