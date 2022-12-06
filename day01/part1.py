data = open("data.txt", "r").readlines()
all_elves = []
elf_total = 0
for calorie in data:
  if len(calorie) > 1:  # To pick out all entries that is not just '\n' or a blank line
    num_calories = int(calorie.strip())  # Remove whitespace then convert string to integer
    elf_total += num_calories
  else:
    all_elves.append(elf_total)  # If we found an '\n', we append total to all_elves array
    elf_total = 0  # Reset elf_total to 0 for the next set of calorie entries for the next elf

sorted_arr = sorted(all_elves)  # Sort all_elves array from smallest to largest

print(sorted_arr[-1])  # Print the last entry which is the largest