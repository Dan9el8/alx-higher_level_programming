#!/usr/bin/python3
# 2-print_alphabet.py
"""print_alphabet in lowercase, not followed by a new line."""
for letter in range(ord('a'), ord("z")+1):
print("{0}" .format(chr(letter)),end="")
