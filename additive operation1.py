#This file is used to figure up 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 +... + 1/1000
sum = 0
for i in range(1, 1001):
    sum = sum + 1/i
print(sum)