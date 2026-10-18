import random

array = []
# Fill array with random numbers
for num in range(7):
    array.append(random.randint(1,100))

print(array)


def find_max_difference(nums):
    max_difference = 0

# For each number, it subtracts itself from each other number, and then if that's the max difference, it updates the variable.

    for start in range(len(nums)):
        for num in range(len(nums)):
            difference = nums[start] - nums[num]
            if difference > max_difference:
                max_difference = difference

    print(max_difference)

find_max_difference(array)

# ChatGPT debugged my code (The only thing I got wrong was it should be for start in range(len(nums)), for both loops, I got everything else correct)

"""
Big O Notation
This one is O(n^2)
The more numbers you have, the more times it has to run through the loop, but for each extra number, it will run through the loop again.
"""