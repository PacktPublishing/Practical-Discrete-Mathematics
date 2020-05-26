#Type of algorithm - inserting new element to pre-existing list

fruit_name = ["Jackfruit", "Honeydew", "Grapes"]
user_input1 = input("Please enter a fruit name: ")
fruit_name.append(user_input1)
print('The updated list is: ' + str(fruit_name))


#Type of algorithm - deleting element from list

user_input2 = input("Please enter the name of the fruit you want to delete: ")
fruit_name.remove(user_input2)
print('The updated list is: ' + str(fruit_name))


