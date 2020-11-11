n = int(input())
d = 0
f = 0

for i in range(1, n+1):
    x = int(input())
    if x >= 10 and x <= 20:
        d = d + 1
    else:
        f = f + 1
print("{} in".format (d))
print("{} out".format (f))
