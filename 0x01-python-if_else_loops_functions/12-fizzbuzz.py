#!/usr/bin/python3
# 12-fizzbuzz.py

"""Print the number from 1 to 100 in separate"""
def fizzbuzz():
for number in range(1, 101):
if number % 3 == 0 and number % 5 == 0:
print("FizzBuzz ", end="")
elif number % 5 == 0:
print("Fizz ", end="")
elif number % 5 == 0:
print("Buzz ", end="")
else:
print("{}".format(number), end="")
