import random

# Set a random seed so the code is reproducible
random.seed(1)

# Run the random.shuffle() function 5 times and display the outputs
for i in range(0,5):
  numbers = [3, 1, 4, 12, 8, 5, 2, 9]
  random.shuffle(numbers)
  print(numbers)