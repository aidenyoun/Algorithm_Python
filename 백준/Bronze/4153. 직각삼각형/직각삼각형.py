while(True):
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if pow(a, 2) + pow(b, 2) == pow(c, 2):
        print("right")
    elif pow(a, 2) + pow(c, 2) == pow(b, 2):
        print("right")
    elif pow(b, 2) + pow(c, 2) == pow(a, 2):
        print("right")
    else:
        print("wrong")