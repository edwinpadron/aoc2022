input_file = open("data.txt", "r")
input_text = input_file.readlines()
all_elves = []
elf_total = 0
for calorie in input_text:
  if len(calorie) > 1:
    num_calories = int(calorie.strip())
    elf_total += num_calories
  else:
    all_elves.append(elf_total)
    elf_total = 0

sorted_arr = sorted(all_elves)
elf1, elf2, elf3 = sorted_arr[-1], sorted_arr[-2], sorted_arr[-3]
print(elf1 + elf2 + elf3)
