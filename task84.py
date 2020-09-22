a = int(input())
r = 0
alphabet = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
while a > 0:
    if (a % 10) in alphabet:
        alphabet.remove(a % 10)
    a //= 10
for i in alphabet:
    print(i)