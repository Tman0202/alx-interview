#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal triangle
        Returns an empty list if n <= 0
        assumes n will be always an integer

        def pascal_triangle(M):
    a=[[] for i in range(M)]
    for i in range(M):
        for j in range(i+1):
            if(j<i):
                if(j==0):
                    a[i].append(1)
                else:
                    a[i].append(a[i-1][j]+a[i-1][j-1])
            elif(j==i):
                a[i].append(1)
    return a
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
