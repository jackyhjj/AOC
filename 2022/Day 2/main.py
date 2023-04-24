input_file = "input.txt"

oppo = {
    "A": {
        "lose": "Z",
        "win": "Y",
        "draw": "X"
    },
    "B": {
        "lose": "X",
        "win": "Z",
        "draw": "Y"
    },
    "C": {
        "lose": "Y",
        "win": "X",
        "draw": "Z"
    },
}

hand_point = {"X": 1, "Y": 2, "Z": 3}
input = []

def read_input_file(input_file):
  with open(input_file) as f:
    for line in f:
      if (len(line.strip()) > 0):
        line = line.replace("\n", "")
        line = line.replace(" ", "")
        input.append(line)

# function to return key for any value
def get_key(val, my_dict):
  for key, value in my_dict.items():
    if val == value:
      return key

  return "key doesn't exist"


def part_1(total_score):
  for line in input:
    opponent = oppo.get(line[0])
    our_hand = hand_point.get(line[1])
    total_score += our_hand

    result = get_key(line[1], opponent)

    if (result == 'win'):
      total_score += 6
    elif (result == 'draw'):
      total_score += 3

  return total_score


def part_2(total_score):
  for line in input:
    opponent = "test"
    opponent = oppo.get(line[0])
    ending = line[1]

    if ending == 'X':
      our_hand = opponent.get('lose')
    elif ending == 'Y':
      our_hand = opponent.get('draw')
      total_score += 3
    else:
      our_hand = opponent.get('win')
      total_score += 6

    total_score += hand_point.get(our_hand)

  return total_score

total_score = 0

read_input_file(input_file)

total_score = 0
print("Part 1:" + str(part_1(total_score)))
total_score = 0
print("Part 2:" + str(part_2(total_score)))
