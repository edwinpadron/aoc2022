stacks = [
  [],
  ['Z', 'T', 'F','R', 'W', 'J', 'G'],
  ['G', 'W', 'M'],
  ['J', 'N', 'H', 'G'],
  ['J', 'R', 'C', 'N', 'W'],
  ['W', 'F', 'S', 'B', 'G', 'Q', 'V', 'M'],
  ['S', 'R', 'T', 'D', 'V', 'W', 'C'],
  ['H', 'B', 'N', 'C', 'D', 'Z', 'G', 'V'],
  ['S', 'J', 'N', 'M', 'G', 'C'],
  ['G', 'P', 'N', 'W', 'C', 'J', 'D', 'L']
]

def directions(line):
  moves = int(line.split('from')[0].split()[1])
  fr = int(line.split('from')[1].split('to')[0])
  to = int(line.split('from')[1].split('to')[1])
  return [moves, fr, to]

def make_moves(moves, fr, to):
  while moves > 0:
    stacks[to].append(stacks[fr].pop())
    moves -= 1

data = [line.strip() for line in open("data.txt")]
for line in data:
  moves, fr, to = directions(line)
  make_moves(moves, fr, to)

answer = ''
index = 1
while index < len(stacks):
  answer += stacks[index][-1]
  index += 1

print(answer)
