#!/usr/bin/env python3

def main():
    primes = [2,3,5,7,11,13]
    num = 14
    while(len(primes) != 10001):
        miniC = 0
        for i in range(len(primes)):
            if(num % primes[i] != 0):
                miniC += 1
            if(miniC == len(primes)):
                primes.append(num)
                # print(num)
                if(len(primes) % 1000 == 0):
                    print(len(primes))
                break
        num += 1
    print(primes[-1])

main()
