#This file is the free addtive open tration into the general unility tool
import sys

def add_add(x,y):
    sum = 0
    for i in range(x, y+1):
        sum = sum + 1/i
        print(sum)

def exit_program(a):
    a = input("Are you sure you want to exit?(yes/no): ")
    if a == "yes":
        sys.exit()
    elif a == "no":
        pass

print('''This file is the free addtive open tration into the general unility tool
You must follow the following steps:
1. Enter a number what you wang to run to additive openration
2. This file Only simple calculations can be run
3.Only two operands can be operated on at a time(specially 2 + 2/2 + 2/3 +... + 2/n)
    e.g:
    1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 +... + 1/1000
    2 + 2/2 + 2/3 + 2/4 + 2/5 + 2/6 +... + 2/1000
    .....

We have some modles to help you do this.
part1:
1. simple additive openration(Only two operands can be operated on at a time)
    e.g
        >>>1 + 2
        3
        >>>5 + 6
        11
part2:
2. Complex majority addition operations involving a variety of operators
    e.g
    1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 +... + 1/1000
    2 + 2/2 + 2/3 + 2/4 + 2/5 + 2/6 +... + 2/1000
    ...... 
    
    Have fun!!
''')
s = input("Select a modle(part1 or 2): ")
while True:
    if s == "part1":
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        print(a + b)
        exit_program(1)
    elif s == "part2":
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        add_add(a, b)
        exit_program(2)
    else:
        print("Wrong input")