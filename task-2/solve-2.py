n = int(input())
s = 0
for i in range(n):
    x = int(input())
    if x % 6 == 0 and x % 10 == 4:
        s += x
print(s)