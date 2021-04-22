# Sam's house has an apple tree and an orange tree that yield an abundance of fruit, where 's' is the start point, and 't' is the endpoint. The apple tree is to the left of his house, and the orange tree is to its right. You can assume the trees are located on a single point, where the apple tree is at point 'a', and the orange tree is at point 'b' .
# When a fruit falls from its tree, it lands 'd' units of distance from its tree of origin along the -axis. A negative value of 'd' means the fruit fell 'd' units to the tree's left, and a positive value of 'd' means it falls 'd' units to the tree's right.
# Given the value of 'd' for 'm' apples and 'n' oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range [s,t] )?


def countApplesAndOranges(s, t, a, b, m, n, apples, oranges):
    apples_distance = [(apples[i] + a) for i in range(m) if (s <= apples[i] + a) and (apples[i] + a) <= t]
    oranges_distance = [(oranges[i] + b) for i in range(n) if (s <= oranges[i] + b) and (oranges[i] + b) <= t]
    return str(len(apples_distance))+"\n"+str(len(oranges_distance))

print(countApplesAndOranges(7,11,5,15,3,2,[-2,2,1],[5,-6]))
print(countApplesAndOranges(2,3,1,5,1,1,[-2],[-1]))

