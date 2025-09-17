N = int(input())

for i in range(N):
    for j in range(N-1-i):
        print(" ", end='')
    for j in range(1+i):
        print("*", end='')
    print("")