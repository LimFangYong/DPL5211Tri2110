# student ID : 1201201544
# Student Name : LIM FANG YONG

def cm_to_meter(centimeter):
    meter = centimeter / 100
    return meter

def get_cm():
    cm = float(input("Enter centimeter : "))
    m = cm_to_meter(cm)
    print("{:.2f} centimeter equals to {:.2f} meters ".format(cm,m))

def meter_to_cm(meter):
    centimeter =  meter * 100
    return centimeter

def get_meter():
    m = float(input("Enter meter : "))
    cm = meter_to_cm(m)
    print("{:.2f} meters equal to {:.2f} centimeter ".format(m,cm))

print("======================================")
print("               MENU                   ")
print("======================================")
print("  1.    Convert centimeter to meter   ")
print("  2.    Convert meter to centimeter   ")
print("======================================")
choice = int(input("Enter your choice : "))
if (choice == 1):
    get_cm()
elif (choice == 2):
    get_meter()
else:
    print("Invalid choice")