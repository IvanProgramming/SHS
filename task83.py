a = int(input())
r = 0
while a > 0:
    r *= 10
    r += a % 10
    a //= 10
while r > 0:
    print(r % 10)
    r //= 10
