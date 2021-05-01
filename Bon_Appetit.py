# Anna and Brian are sharing a meal at a restuarant and they agree to split the bill equally. Brian wants to order something that Anna is allergic to though, and they agree that Anna won't pay for that item. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.
# k: an integer representing the zero-based index of the item Anna doesn't eat
# b: the amount of money that Anna contributed to the bill

def bonAppetit(bill, k, b):
    bill.pop(k)
    Anna_bill = sum(bill) // 2
    if Anna_bill == b:
        return "Bon Appetit"
    else :
        return abs(Anna_bill - b)

print(bonAppetit([3, 10, 2, 9], 1, 12))
print(bonAppetit([3, 10, 2, 9], 1, 7))
