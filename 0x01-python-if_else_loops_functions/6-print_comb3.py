#!/usr/bin/python3
for x in range(9):
    for y in range(x+1, 10):
            print(f"{x}{y}", end=', ' if x < 8 else '\n')