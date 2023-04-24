input_file = "input.txt"

all_sum = []
with open(input_file) as f:
    lv_maximum = 0
    lv_total = 0
    for line in f:
        if (len(line.strip()) > 0):
            lv_total += int(line.strip())
        else:
            all_sum.append(lv_total)
            lv_total = 0

# part 1
all_sum.append(lv_total)
print("Part 1:" + str(max(all_sum)))

#part 2
all_sum = sorted(all_sum, reverse=True)
print("Part 2:"+ str(all_sum[0]+all_sum[1]+all_sum[2]))
