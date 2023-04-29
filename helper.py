def read_input_file(input_file):
    input=[]
    with open(input_file) as f:
        for line in f:
            # print(line)
            if (len(line.strip()) > 0):
                line = line.replace("\n", "")
                line = line.replace(" ", "")
                input.append(line)
    return input