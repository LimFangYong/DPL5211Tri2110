# Student ID : 1201201544
# Student Name : LIM FANG YONG

PRICE = 0.15

print("Nature Minaral Water Dispenner")
print("------------------------------------")

litres = int(input("\nEnter amount of litres : "))
print("\nPrice per litre   = RM {:.2f}".format(PRICE))
print("Number of litres  = {}".format(litres))

total_price = litres * PRICE

print("Total : RM {:.2f}".format(total_price))