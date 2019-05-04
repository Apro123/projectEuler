#!/usr/bin/env python3

def main():
    big = 0
    small = 0
    for i in range(101):
        small += i * i
        big += i
    big = big * big
    print(big - small)
main()
