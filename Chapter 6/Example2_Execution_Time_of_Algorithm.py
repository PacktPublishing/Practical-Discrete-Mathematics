# a is a list containing some numbers
#We will compare the number input by user with the numbers in this list

import timeit
tic=timeit.default_timer()

a=[1,2,3,4,5,6,7,8]
INPUT = input("Please input a number of your choice: ")
number = int(INPUT)

for i in range(len(a)):
    if a[i]== number:
        print("Yes", end='  ')
    else:
        print("No", end='  ')
print()

toc=timeit.default_timer()
time_elapsed = toc - tic
print("The time elapsed for this computation is: " + str(time_elapsed) + " seconds")

