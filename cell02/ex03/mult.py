print("Enter the first number")
num1 = int(input())
print("Enter the second number")
num2 = int(input())
result = num1*num2

print(num1,"x",num2,"=",num1*num2)
if result > 0 :
    print("This number is positive.")
elif result == 0:
    print("This number is both positive and negative.")
else :
    print("This number is negative.")