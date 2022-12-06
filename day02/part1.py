def process(other, you):
  round_score = 0
  if other == 'A':
    if you == 'X':
      round_score = 4
    elif you == 'Y':
      round_score = 8
    else:
      round_score = 3
  elif other == 'B':
    if you == 'X':
      round_score = 1
    elif you == 'Y':
      round_score = 5
    else:
      round_score = 9
  else:
    if you == 'X':
      round_score = 7
    elif you == 'Y':
      round_score = 2
    else:
      round_score = 6
  return round_score


input_file = open("data.txt", "r")
input_text = input_file.readlines()
input_array = []
for entry in input_text:
  pair = entry.strip().split(' ')
  input_array.append(pair)
print(input_array)

score = 0

for elem in input_array:
  other, you = elem
  score += process(other, you)

print(score)
