H, M = map(int, input().split())

if M-45 < 0:
    if H >= 1:
        H = H-1
        M = 60+(M-45)
        print(H, M)
    elif H == 0:
        H = 23
        M = 60+(M-45)
        print(H, M)
else:
    print(H, M-45)