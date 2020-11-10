x = 100
y = 200

while x != y:
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x > y:
        print("Decrescente")
    elif x < y:
        print("Crescente")
