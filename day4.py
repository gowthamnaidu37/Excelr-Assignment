# 4) Write a Python program to calculate the sum of all even numbers between 1 and a given positive integer n
a = int(input("Enter a number: "))
sum = 0
for i in range(1, a+1):
    if i % 2 == 0:
        sum += i    
print("Sum of all even numbers between 1 and", a, "is", sum)
