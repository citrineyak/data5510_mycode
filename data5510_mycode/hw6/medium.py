import random


array = []

# ChatGPT "how to make array of 7 random numbers"
for num in range(7):
    array.append(random.randint(1,100))

print(array)

def largest_number(nums):
    largest = 0
    second_largest = 0

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num

    return(second_largest)

print("Second Largest: ", largest_number(array))

# ChatGPT debugged the code (I copy and pasted my code into the Chat)

"""
Big O Notation
I'd say this one is O(n)
We're still only looping through the array one time, so regardless of how many numbers are in the array, it won't take longer than O(n)
"""