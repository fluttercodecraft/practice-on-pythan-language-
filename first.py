"""Create a program that takes two numbers 
and prints their sum,
subtraction, multiplication,
 and division."""

input1=int(input("Enter first number: "))
input2=float(input("Enter second number: "))
addition=input1+input2
subtraction=input1-input2
multiplication=input1*input2 
Divsion=input1/input2
print("Addition:", addition)
print("Subtraction:", subtraction)  
print("Multiplication:", multiplication)
print("Division:", Divsion)
"""Write a program that checks 
whether a number is even or odd."""
if input1%2==0:
    print("The first number is even")
else:
    print("The number is odd")    

list1 = [1, 2, 3]
maximum = list1[0]

for i in list1:
    if i > maximum:
        maximum = i

print("The largest number is:", maximum)