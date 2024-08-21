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

print("a 3 digit code: " + str(a) + str(b) + str(c))
print("a 4 digit code is: " + str(t) + str(x) + str(y) + str(z))