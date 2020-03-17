import time
number = 1000000

# Check the current time
startTime = time.time()

# Create an empty list
list = []

# Add items to the list one by one
for counter in range(number):
  list.append(counter)

# Display the run time
print(time.time() - startTime)