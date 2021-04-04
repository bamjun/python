def solution(n, jinsu):
    a = ''
    while n :
        n, b = divmod(n, jinsu)
        a += str(b)
    return a[::-1]

n = 125
#십진수
ss = 3
#변환진수
print(solution(n, ss))




