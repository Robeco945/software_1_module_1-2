print("PART 2\n")
try:
    radius_str: int = input('enter the radius: ')
    radius = float(radius_str)
except:
    radius_str: int = input('please enter a number: ')
    radius = float(radius_str)

area = radius*radius*3.14
print('the area of your circle is: ' + str(area),"\n")
