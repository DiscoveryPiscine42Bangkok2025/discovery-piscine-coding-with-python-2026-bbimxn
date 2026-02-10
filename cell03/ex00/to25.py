#!/usr/bin/env python3

num = int(input("Enter number less than 25 \n"))
if num > 25:
    print("error")
else:
    while num != 26 :
        print("Inside the loop,my variable is" ,num)
        num+=1