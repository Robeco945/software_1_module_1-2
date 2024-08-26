"""
print("PART 1\n")

user = input('what is your name?\n')
print('hello,' + user + '!\n')

print("\n\n PART 2\n")
try:
    radius_str: int = input('enter the radius: ')
    radius = float(radius_str)
except:
    radius_str: int = input('please enter a number: ')
    radius = float(radius_str)

area = radius*radius*3.14
print('the area of your circle is: ' + str(area),"\n")

print("\n\n PART 3\n")
length_str: int = input("enter the length of the rectangle: \n")
width_str: int = input("enter the width of the rectangle: \n")
length = float(length_str)
width = float(width_str)
peri: float = length*2+width*2
area: float = length*width
print("the perimeter of the rectangle is: " + str(peri),"\nthe area of the rectangle is: " + str(area))

print("\n\n PART 4\n")
a_s: int = input("enter the first number: ")
b_s: int = input("enter the second number: ")
c_s: int = input("enter the third number: ")
a = int(a_s)
b = int(b_s)
c = int(c_s)
sum: int = a+b+c
pro: int = a*b*c
ave: float = sum/3
print("the sum is: " + str(sum), "\nthe product is: " + str(pro), "\nthe average is: " + str(ave))

print("\n\n PART 5\n")
ta_str = input("enter the weight in talents: ")
po_str = input("enter the weight in pounds: ")
lot_str = input("enter the weight in lots: ")
ta = float(ta_str)
po = float(po_str)
lot = float(lot_str)
kg = (ta*20+po)*0.454+lot*13.3
print("the weight in modern units:\n" + str(kg),"kg")

#one lot is 13.3g -> one lbs = 32 lots = 32*13.3g
#one talent is 20lbs = 20*32 lots = 20*32*13.3g
#one kg is 1000g   one lbs = 0,454kg

print("\n\n PART 6\n")
#Write a program that draws two random combinations of numbers for a combination lock:
#a 3-digit code where each number is between 0 and 9.
#a 4-digit code where each number is between 1 and 6.

import random
a = random.randint(0,9)
b = random.randint(0,9)
c = random.randint(0,9)
x = random.randint(1,6)
y = random.randint(1,6)
z = random.randint(1,6)
t = random.randint(1,6)

print("a 3 digit code:" + str(a,b,c))
print("a 4 digit code is:" + str(x,y,zh#


print("PART 2\n")
while True:
    radius_str = input("enter the radius: ")
    try:
        #radius_str: float = input('enter the radius: ')
        radius = float(radius_str)
        break
    except ValueError:
        radius_str = input('please enter a number: ')
        radius = float(radius_str)

#while(radius_str != int or float ):
  #  radius_str = input('please enter a number: ')
#if(radius_str == int or float):

area = radius*radius*3.14
print('the area of your circle is: ' + str(area),"\n")

from random import randint, randrange, random
num1 = str(random())
print(f'code 1: {num1[2:5]}')
num4 = randint(1,6)
num5 = randint(1,6)
num6 = randint(1,6)
num7 = randint(1,6)
print(f'code2: {num4}{num5}{num6}{num7}')
"""
age = int(input("Enter age: "))
if 15 <= age < 18:
    weight = float(input("Enter weight (kg): "))
if (age >=18 or age>=15 and weight >=55):
    print("The medicine can be used.")