#!/usr/bin/env python3
from functools import reduce

def fac(n):
    print((len(list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))))))

def numfactors(n):
    if(n % 2 == 0 and n > 5):
    # count = 0
    # for i in range(1, num + 1):
    #     if(num % i == 0):
    #         #i is a factor of the num
    #         count += 1
        return int(len(list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))))
    return 0

def main():
    #getting triangle numbers
    num = 0
    counter = 1
    while(numfactors(num) <= 500):
        num += counter
        counter += 1
        if(num >= 1000000 and num % 1000000 < 10000):
            print(num)
    print(num)

# fac(10)
main()
