#! /usr/bin/python3.5

try:
    x=int(input('Enter the first number:'))
    y=int(input('Enter the second number:'))
    print(x/y)
except(ZeroDivisionError,TypeError) as e:
    print (e)
