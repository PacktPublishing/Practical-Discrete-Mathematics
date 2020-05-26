def linear_search(input):
    lists = [1, 2, 3, 4, 5, 6, 7, 8]
    number = int(input)

    for i in range(len(lists)):
        if lists[i] == number:
            print("True", end='  ')
        else:
            print("False", end='  ')
    print()

INPUT = input("Please input a number of your choice: ")
linear_search(INPUT)


