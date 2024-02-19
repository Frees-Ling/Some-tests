def prime_num(x):
    for i in range(2,x):
        if x % i == 0:
            print("%d is not a prime number!" % x)
            break
        else:
            print("%d is a prime number!" % x)
            break