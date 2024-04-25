#Samuel Rodriguez
#04/19/24
#P4LAB2
#Using the range function with while and for loops

num1= int(input("Enter num1: "))
num2= int(input("Enter num2: "))

while num1 >= num2:
    print("Num1 must be smaller")
    num1= int(input("Enter num1: "))
    num2= int(input("Enter num2: "))

for number in range (num1, num2+1, 5):
    print(number)
