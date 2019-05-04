#!/usr/bin/env python3

def main():
    primes = [2,3,5,7,11,13,17,19]
    for i in range(20, 2000001):
        counter = 0;
        for j in primes:
            if(i % j == 0):
                continue
            else:
                counter += 1
            if(counter == len(primes)):
                primes.append(i)
            # sumN += i
            # print(i)
        if(i % 10000 == 0):
            print(i)
    print(sum(primes))

main()
