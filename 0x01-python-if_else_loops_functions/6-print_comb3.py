#!/usr/bin/python3
# 6-print_comb3.py

"""Print different combination in decsending order
two digits considered identical."""

for digit1 in range(10):
for digit2 in range(digit1+1, 10):
print("{}{}".format(digit1, digit2))
if digit1 != 8 or digit2 != 9:
print(", ", end="")
print()
