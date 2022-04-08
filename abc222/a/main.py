#!/usr/bin/env python3

input = input()

if len(input) < 4:
    short_digit = 4 - len(input)
    for _ in range(short_digit):
        input = "0" + input

print(input)