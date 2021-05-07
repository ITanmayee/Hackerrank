# Two cats and a mouse are at various positions on a line. You will be given their starting positions. Your task is to determine which cat will reach the mouse first, assuming the mouse doesn't move and the cats travel at equal speed. If the cats arrive at the same time, the mouse will be allowed to move and it will escape while they fight.

def catAndMouse(x, y, z):
    catA = abs(z - x)
    catB = abs(z - y)
    if catA < catB :
        return "Cat A"
    if catB < catA:
        return "Cat B"
    return "Mouse C"

print(catAndMouse(1, 2, 3))
print(catAndMouse(1, 3, 2))

