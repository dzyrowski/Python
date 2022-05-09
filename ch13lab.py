#!/usr/env python3.7

#fizz buzz

value = (int(input("Enter an integer value: "))) #define value

if value % 5 == 0 and value % 3 == 0: #if a number is divisible by 3 AND 5, print FizzBuzz
    print("FizzBuzz")
elif value % 3 == 0: #if a number is divisible by 3 only, print Fizz
    print("Fizz")
elif value % 5 == 0: #if a number is divisible by 5 only, print Buzz
    print("Buzz")
else: #if not divisible by 3 or 5, print the number
    print(value)