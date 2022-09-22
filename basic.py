print('hello! python')
#declear variable
num  = 50
num2 = 20
#oparator
#addition
addition = num+num2
print('addition', addition)
#substraction
substraction = num - num2
print('Substraction:', substraction)
#multyply
print('Multiply: ', num*num2)
print('division: ', num/num2)
#modulus
print('modulus: ', num%num2)
#list
li = []
#append method
li.append(21)
li.append(24.5)
li.append('this is list')
print(li)
#input
greeting = 'Hello! '
name = input('Enter Your Name: ')
print(greeting, name)
#convert to int
v1 = int(input('Enter first number: '))
v2 = int(input('Enter Second number: '))
mul = v1*v2
print('Multiplication is: ', mul)
#selection or condition
age = 52
if(age>50):
    print('This man is older')
elif(age==50):
    print('This man is a middle age person')
else:
    print('This man is young')
#function
def hello():
    print('This is hello function')
hello()
#more in function
def multiply():
    first = int(input('Enter first number for function: '))
    second = int(input('Enter Second number for second function: '))
    result = first*second
    return result
def Main():
    print('Start from main function')
    result = multiply()
    print(result)
if __name__ == "__main__":
    Main()

#Iteration/Loop
for step in range(5):
    print(step)

#module
import math
def Main():
    num = -70
    num = math.fabs(num)
    print(num)
if __name__ == "__main__":
    Main()


