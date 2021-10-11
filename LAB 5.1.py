# student ID : 1201201544
# Student Name : LIM FANG YONG

def my_function(name, contact_num, salary, overtime):
    print("Hello ",name)
    print("This is my phone number : ",contact_num)
    total = float(salary) + float(overtime)
    print("Your salary this month is RM {:.2f}".format(total))

my_function("Fang Yong", "011-10791578", 4000, 500)