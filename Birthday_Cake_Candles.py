# You are in charge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age. When she blows out the candles, she will only be able to blow out the tallest ones. Your task is to find out how many candles she can successfully blow out.


def birthdayCakeCandles(ar):
    return ar.count(max(ar))


print(birthdayCakeCandles([4,4,4,5,7,3,2,4]))
print(birthdayCakeCandles([7,4,5,3,5,4,4,9,9,4,6,9]))
