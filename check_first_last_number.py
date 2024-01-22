def check_first_last_same(numbers):
    if not numbers:  
        return False

    return numbers[0] == numbers[-1]

list1 = [1, 2, 3, 4, 1]
list2 = [1, 2, 3, 4, 5]

print(check_first_last_same(list1))  
print(check_first_last_same(list2))  
