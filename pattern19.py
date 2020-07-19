n=int(input("Enter the number of rows"))
for i in range(n):
    print(chr(64+n-i)*(n-i))