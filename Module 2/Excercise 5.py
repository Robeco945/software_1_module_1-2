print("PART 5\n")
ta_str = input("enter the weight in talents: ")
po_str = input("enter the weight in pounds: ")
lot_str = input("enter the weight in lots: ")
ta = float(ta_str)
po = float(po_str)
lot = float(lot_str)
kgw = lot * 0.0133 + ta * 8.512 + po * 0.4256
kilograms = int(kgw)
grams = (kgw - kilograms) * 1000
print(f"the weight in modern units:\nkilograms: {kilograms}  grams: {grams:5.2f}")
# |kg=lots×0.0133 | kg=talents×8.512 | kg=lbs×0.4256
