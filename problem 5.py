#!/usr/bin/env python3

def main():
    num = 21
    test = [1,2,3,5,7,9,11,13,17,19]
    while(True):
        counter = 0
        for i in range(1, 10):
            if(num % test[i] == 0):
                counter += 1
            if(counter == 9):
                print(num)
                return
            if(counter == 8):
                print(num)
        num += 1

main()
