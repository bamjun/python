def solution(n):
    a = ''
    while n > 0:
        n, b = divmod(n, 3)
        a += str(b)
    return int(a, 3)



    for x in range(len(answers)):
        ax = a[x%5]
        bx = b[x%8]
        cx = c[x%10]
def solution(A, B):
    c = []

    for i in A:

        y = B.pop(B.index(min(B)))
        c.append(i * y)
        print(i, y)


    return sum(c)


>>> for i in range(1, 5):
...     print(i)
...
1
2
3
4
>>> for i in range(1, 5, 2):
...     print(i)
...
1
3
>>> for i in range(1, 10, 3):
...     print(i)
...
1
4
7
>>>
