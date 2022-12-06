data = open("data.txt", "r").readlines()[0]

def process(data, chars):
  counter = 0
  index = None
  while counter < len(data) - chars:
    window = data[counter:counter + chars]
    unique = set([*window])
    if len(unique) == chars:
      index = counter + chars
      break
    counter += 1
  return index

print(f"The answer to part 1 is: {process(data, 4)}")
print(f"The answer to part 2 is: {process(data, 14)}")
