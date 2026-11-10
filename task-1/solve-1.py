n = int(input())
s = 0
for i in range(n):
    x = int(input())
    if x % 10 == 3:
        s += x
print(s)