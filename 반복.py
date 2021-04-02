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
