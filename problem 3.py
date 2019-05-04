#!/usr/bin/env python3

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump

def main():
    num = 600851475143
    factor = 0;
    while(int(num) != 1):
        for i in frange(2,num,1):
            # print(i)
            # print(i % 2 != 0 or i == 2)
            # print(i % 3 != 0 or i == 3)
            # print(i % 5 != 0 or i == 5)
            # print(num % i == 0)
            if((i % 2 != 0 or i == 2) and (i % 3 != 0 or i == 3) and (i % 5 != 0 or i == 5) and num % i == 0 and factor < i):
                factor = i
                num = num / i
                print("------")
                print(factor)
                # break
        print(num)
    print(factor)
main()
