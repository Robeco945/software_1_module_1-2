print("PART 3\n")
length_str: int = input("enter the length of the rectangle: \n")
width_str: int = input("enter the width of the rectangle: \n")
length = float(length_str)
width = float(width_str)
peri: float = length*2+width*2
area: float = length*width
print("the perimeter of the rectangle is: " + str(peri),"\nthe area of the rectangle is: " + str(area))
