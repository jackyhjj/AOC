def part_1(first_list, second_list):
    tmp1 = first_list[:];
    tmp2 = second_list[:];
    tmp1.sort()
    tmp2.sort()
    total_distance = 0
    for i in range(len(tmp1)):
        total_distance += abs(int(tmp1[i]) - int(tmp2[i]))

    return total_distance

def part_2(first_list, second_list):
    total_similiraty = 0
    for i in range(len(first_list)):
        total_similiraty += int(first_list[i]) * second_list.count(first_list[i])

    return total_similiraty

first_list = []
second_list = []
f = open("input.txt", "r")

for line in f.readlines():
    first_list.append(line.strip().split("  ")[0])
    second_list.append(line.strip().split("   ")[1])    
f.close()

print('part 1:', part_1(first_list, second_list))
print('part 2:', part_2(first_list, second_list))

