# Student ID : 1201201544
# Student Name : LIM FANG YONG

BANANA = 1.5
GRAPES = 5.6

print("Invoice for fruits Purchase")
print("---------------------------------")

banana = int(input("Enter the quantity (comb) of bananas bought : "))
grapes = float(input("Enter the amount (kg) of grapes bought : "))

banana_price = banana * BANANA
grapes_price = grapes * GRAPES
total_price = banana_price + grapes_price

print("\nItem\t\t Qty\t Price\t Total")
print("Bananas (combs)\t {}\t RM {:.2f}\t RM {:.2f}".format(banana, BANANA, banana_price))
print("Graps (kg)\t {:.2f}\t RM {:.2f}\t RM {:.2f}".format(grapes, GRAPES, grapes_price))
print("Total : RM {:.2f}".format(total_price))