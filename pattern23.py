n = int(input("Enter the number of rows"))
for i in range(n):
    for j in range(n-i):
        print(chr(64+n-i),end='')
    print()