# Returns index of target (x) if present in the list
def binary_search(list, l, r, target_value):
    # Check base case
    if r >= l:

        mid_index = l + (r - l) // 2

        # If target element matches with the mid-element of the list
        if list[mid_index] == target_value:
            return mid_index

        # If element is smaller than mid-element, then it can only be present in
        # left sublist
        elif list[mid_index] > target_value:
            return binary_search(list, l, mid_index - 1, target_value)

        # Else the element can only be present in right sub-list
        else:
            return binary_search(list, mid_index + 1, r, target_value)

    else:
        # Element is not present in the array 
            return -1


# Test list
list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target_value = 100

# Function call
result = binary_search(list, 0, len(list) - 1, target_value)

if result != -1:
    print("Target element is present at index " + str(result) + " of the list")
else:
    print("Target element is not present in list")


