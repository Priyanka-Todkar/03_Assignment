# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
# Explanation:
# Summation should like 8+2+3+0+7 = 20

def sum_list(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
my_list = [8, 2, 3, 0, 7]
result = sum_list(my_list)
print(result)