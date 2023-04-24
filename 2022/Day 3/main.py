from string import ascii_lowercase, ascii_uppercase

input_file = "input.txt"
input = []


def read_input_file(input_file):
    with open(input_file) as f:
        for line in f:
            if (len(line.strip()) > 0):
                line = line.replace("\n", "")
                line = line.replace(" ", "")
                input.append(line)


def part_1():
    total = 0
    for line in input:
        counter = len(line)
        # print(line)

        compartment_1 = line[:int((counter / 2))]
        compartment_2 = line[int(counter / 2):]

        same_item_list = set(compartment_1).intersection(compartment_2)

        for item in same_item_list:
            if item in ascii_lowercase:
                total += ascii_lowercase.index(item) + 1
            else:
                total += ascii_uppercase.index(item) + 27

    return total


def part_2():
    rucksack_lists = []
    total = 0
    for line in input:
        if len(rucksack_lists) != 3:
            rucksack_lists.append(line)
        else:
            same_item_list = set(rucksack_lists[0]).intersection(rucksack_lists[1]).intersection(rucksack_lists[2])

            for item in same_item_list:
                if item in ascii_lowercase:
                    total += ascii_lowercase.index(item) + 1
                else:
                    total += ascii_uppercase.index(item) + 27

        rucksack_lists = []
    return total


read_input_file(input_file)

print(part_1())
print(part_2())
