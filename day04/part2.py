def process(pair):
  first, second = pair
  first_elf = first.split('-')
  second_elf = second.split('-')
  one, two = first_elf
  three, four = second_elf
  one = int(one)
  two = int(two)
  three = int(three)
  four = int(four)
  if three <= two and four >= one: # Looks for any overlap
    overlaps['value'] += 1
    
file = open("data.txt", "r").readlines()
overlaps = {'value': 0}
for item in file:
  pair = item.strip().split(',')
  process(pair)

print(overlaps)