num = float(input("Give me a num: "))

isFull = (num * 10) % 10

if(isFull != 0) :
    print("This number is a decimal")
else :
    print("This number is an integer")