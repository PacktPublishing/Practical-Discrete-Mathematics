#Quadratic complexity

def quadratic_complexity(list):
    count = 0
    for i in list:
        for j in list:
            count += 1
            print(str(count) + "\t|First for loop iteration: " + str(i), '\t|', "Second for loop iteration: " + str(j))

quadratic_complexity([1,2,3,4])


