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