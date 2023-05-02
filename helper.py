def read_input_file(input_file, remove_space = True):
    input=[]
    with open(input_file) as f:
        for line in f:
            # print(line)
            if (remove_space == True):
                line.strip()
                line = line.replace("\n", "")
                line = line.replace(" ", "")
                
            if (len(line) > 0):
                input.append(line)
    return input