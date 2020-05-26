#Complex function complexity

def complex_func (list):
    count = 0
    for i in range(6):
        count += 1
        print("Step: " + str(count) +  " \t Hello World!")

    for j in list:
        count += 1
        print("Step: " + str(count) +  " \t " + str(j))

    for k in list:
        count += 1
        print("Step: " + str(count) +  " \t " + str(k))

complex_func([1,2,3,4])


