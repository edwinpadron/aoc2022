data = open("data.txt", "r").readlines()[0]

def process(data, chars):
  counter = 0
  index = None
  while counter < len(data) - chars:
    # Creates a group of characters whose length is equal to the argument 'chars'
    # This is a sliding window that starts from the beginning of 'data' and for each
    # iteration, it moves 1 char to the right.
    window = data[counter:counter + chars]
    # Creates an array of each chars from window which is a string of length 'chars'
    # and 'set()' will convert this array into a set which contains only unique chars 
    unique = set([*window])
    # if length of unique chars is equal to the window then there are no duplicates and
    # we found our target
    if len(unique) == chars:  
      index = counter + chars
      break
    counter += 1
  return index

print(f"The answer to part 1 is: {process(data, 4)}")
print(f"The answer to part 2 is: {process(data, 14)}")

