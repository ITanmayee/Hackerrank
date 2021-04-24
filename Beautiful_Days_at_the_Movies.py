""" Given a range of numbered days,[i....j]  and a number 'k' , determine the number of days in the range that are beautiful. Beautiful numbers are defined as numbers where |i - reverse(i)|  is evenly divisible by 'k'. If a day's value is a beautiful number, it is a beautiful day. Print the number of beautiful days in the range.
# Lily will look at a numbered range of days and will only go to a movie on a beautiful day.
"""

def beautifulDays(start_day, end_day, divisor):
    return len([ num for num in range(start_day, end_day+1) if (abs(num - int(str(num)[::-1]))) % divisor == 0])

print(beautifulDays(20, 23, 6))
print(beautifulDays(1, 2000000, 23047885))
