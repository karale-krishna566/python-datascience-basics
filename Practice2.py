unit = float(input("Enter total unit "))
bill = 0
if unit < 100:
bill = 0
print("bill is free")
elif unit >= 100:
bill = (unit 100) * 5 elif unit >= 200:
bill = (unit 200) * 10
elif unit >= 300:
bill = (100 * 5) + (units 200) * 7
else:
bill = (100 * 5) + (100 * 7) + (units 300) * 10
print("Total Electricity Bill = Rs", bill)
