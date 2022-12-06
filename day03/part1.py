rucksacks = open("data.txt", "r").readlines()
split_rucksacks = []
sum_priorities = 0
priorities = '^abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Loops through rucksacks and split each item into 2 equal compartments
for rucksack in rucksacks:
  # int() is necessary to make 'middle' an integer because division results in a float
  # and 'middle' is going to be used as an index and floats cannot be used as index.  
  middle = int(len(rucksack.strip()) / 2) 
  comp1 = rucksack[:middle]
  comp2 = rucksack[middle:]
  split_sack = [comp1, comp2.strip()]
  split_rucksacks.append(split_sack)

# Loops through split_rucksacks and find any 1 item that is present in both
# compartments.
for item in split_rucksacks:
  index = 0
  first, second = item
  while index < len(first):
    if first[index] in second:
      sum_priorities += priorities.index(first[index])
      break
    index += 1
    
print(sum_priorities)
