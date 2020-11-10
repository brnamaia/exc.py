n = int(input())

for i in range(1, n+1):
    x, y = map(int,input().split())
    if y != 0:
        divi = x/y
        print("{}".format (divi))
    elif y == 0:
        print("divisao impossivel")
    
