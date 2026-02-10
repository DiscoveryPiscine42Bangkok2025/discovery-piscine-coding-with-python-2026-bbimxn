#!/usr/bin/env python3
i = 0
while i <= 10:
    print("Table de",i,": ",end=" ")
    j = 0
    while j <= 12:
        print(j*i ,end = " ")
        j+=1
    print()
    i+=1  