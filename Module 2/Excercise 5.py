print("PART 5\n")
ta_str = input("enter the weight in talents: ")
po_str = input("enter the weight in pounds: ")
lot_str = input("enter the weight in lots: ")
ta = float(ta_str)
po = float(po_str)
lot = float(lot_str)
kg = (ta*20+po)*0.454+lot*13.3
print("the weight in modern units:\n" + str(kg),"kg")
