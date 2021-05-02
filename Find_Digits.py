# An integer 'd' is a divisor of an integer 'n' if the remainder of n / d = 0 .
# Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.

def is_divisible(num , div) :
    if num % div == 0:
        return True
    return False

def findDigits(n):
    num = str(n)
    digits = [int(i) for i in num if i != "0"]
    divisors = [i for i in digits if is_divisible(n, i)]
    return len(divisors)

print(findDigits(1012))
print(findDigits(114108089))
print(findDigits(110110015))
