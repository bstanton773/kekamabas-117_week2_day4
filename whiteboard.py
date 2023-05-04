# Given a list of Integers
# Create and Return a new list of integers where all the numbers from the original list
# are replaced with "Fizz" if the number is divisible by 3
# "Buzz" if the number is divisible by 5
# and "FizzBuzz" if the number is divisible by BOTH 3 and 5
# And if its not any of those cases just add the number to the new list
# For example
# If you start with the list: [2,3,4,5,12,14,17]
# The output would be: [2, 'Fizz', 4, 'Buzz', 'Fizz', 14, 'FizzBuzz', 17]


# def solution(nums):
#     output = []
#     for num in nums:
#         if num % 3 == 0 and num % 5 == 0:
#             output.append('FizzBuzz')
#         elif num % 3 == 0:
#             output.append('Fizz')
#         elif num % 5 == 0:
#             output.append('Buzz')
#         else:
#             output.append(num)
#     return output

def solution(nums):
    return ['FizzBuzz' if num % 3 == 0 and num % 5 == 0 else 'Fizz' if num % 3 == 0 else 'Buzz' if num % 5 == 0 else num for num in nums]
