import time
number = 1000000

# Check the current time
startTime = time.time()

# Create a list of 1000000 zeros
list = [None]*number

# Add items to the list one by one
for counter in range(number):
  list[counter] = counter

# Display the run time
print(time.time() - startTime)