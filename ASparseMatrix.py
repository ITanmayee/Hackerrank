"""

Given a matrix of size N x M. Print whether it is a sparse matrix. A matrix containing 0 value in more than half of its elements, then it is called a sparse matrix.

"""


row , col = list(map(int, input().split()))

matrix = [list(map(int , input().split())) for i in range(row) ]

zero_count = sum([i.count(0) for i in matrix])

if zero_count > ((row * col) // 2):
    print("Yes")
else :
    print("No")
