#!/usr/bin/env python3

def main():
    for i in range(1000):
        for j in range(1000):
            for k in range(1000):
                if(i + j + k == 1000):
                    arr = [i,j,k]
                    m = max(arr)
                    index = arr.index(m)
                    arr.remove(m)
                    if((arr[0] ** 2) + (arr[1] ** 2) == m ** 2):
                        print(i * j * k)
                        print(i)
                        print(j)
                        print(k)

main()
