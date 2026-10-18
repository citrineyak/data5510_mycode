array = [1,2,3,4,5,6,7]

def sum_calc(nums):
    total = 0
    for num in nums:
        total += num

    return total

print("Sum: ", sum_calc(array))

""" Big O notation
O(n)
Because the function will only loop through the array one time, so with n numbers, it runs n times. The more numbers, the slower the function

"""

