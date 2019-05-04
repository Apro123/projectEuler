#!/usr/bin/env python3

def isPalindrome(value):
    vals = []
    temp = value
    while(int(temp) != 0):
        vals.insert(0, temp % 10)
        temp = int(temp/10)
    for i in range(int(len(vals)/2)):
        if(vals[i] != vals[len(vals)-1-i]):
            return False
    return True;

def main():
    product = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            if(isPalindrome(i*j) and product < (i * j)):
                product = i * j
    print(product)


main()
