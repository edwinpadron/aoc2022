rucksacks = open("data.txt", "r").readlines()
grouped_sacks = []
sum_priorities = 0
priorities = '^abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Loops through rucksacks and build groups of 3 elves
index = 0
while index <= len(rucksacks) - 3:
  group = [rucksacks[index].strip(), rucksacks[index + 1].strip(), rucksacks[index + 2].strip()]
  grouped_sacks.append(group)
  index += 3

# Loops through grouped_sacks and for each group, find the 1 item
# that is present in all 3 members of the group
for group in grouped_sacks:
  index = 0
  first, second, third = group
  while index < len(first):
    if first[index] in second and first[index] in third:
      sum_priorities += priorities.index(first[index])
      break
    index += 1
    
print(sum_priorities)
