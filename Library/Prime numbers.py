#This is a file for Prime numbers Operation
n = int(input("Please Enter a number for operation:"))
for i in range(2,n):
    if n % i == 0:
        print("%d is not a Prime number!" %n)
        break
else:
    print("%d is a Prime number!" %n)