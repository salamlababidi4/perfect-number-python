# In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisors,
# excluding the number itself. For instance, 6 has divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, so
# 6 is a perfect number.
# Write a function named is_perfect, that takes an integer and returns True if the given integer is perfect,
# and False otherwise.
# Hint: You can define a helper function to decide a number is divisor of another number.

def is_divisor(a, b):
    return a % b == 0
def is_perfect(n):
    if n <=1:
        return False
    sum_pos= sum(i for i in range(1,n) if is_divisor(n,i))
    return sum_pos == n

s = 6
if(is_perfect(s)):
    print(s, " is perfect!")
else:
    print(s, " is not perfect")