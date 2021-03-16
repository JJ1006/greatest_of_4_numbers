num1=input("Enter Number 1 : ") #take input of first number
num2=input("Enter Number 2 : ") #take input of second number
num3=input("Enter Number 3 : ") #take input of third number
num4=input("Enter Number 4 : ") #take input of fourth number

if(num1>=num2): #check greater of first two numbers and save it in another variable (n1).
    n1=num1 
else:
    n1=num2

if(num3>=num4): #check greater of last two numbers and save it in another variable (n2).
    n2=num3
else:
    n2=num4

if(n1>n2): #check the greater of the two new variables (n1 and n2) and print the greatest
    print(n1 + ' is greatest number from the given numbers.')
else:
    print(n2 + ' is greatest number from the given numbers.')    
    