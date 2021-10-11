# student ID : 1201201544
# Student Name : LIM FANG YONG

def rectangle(width, length):
    area_rectangle = width * length
    
    return area_rectangle

def triangle(width, length):
    area_triangle = (width * length) / 2
    
    return area_triangle

i = 0
while(i<2):
    width = int(input("Enter width : "))
    length = int(input("Enter length : "))

    area_rectangle = rectangle(width, length)
    area_triangle = triangle(width, length)

    print("Rectangle area : {:.2f}".format(area_rectangle))
    print("Triangle area : {:.2f}".format(area_triangle))
i += 1