# student ID : 1201201544
# Student Name : LIM FANG YONG

def get_bonus(unit_sold,salary):
    if (unit_sold > 1000):
        bonus = (salary * 0.2)
    elif (unit_sold > 500 & unit_sold <= 1000):
        bonus = (salary * 0.1)
    else :
        bonus = 0
    return bonus

def get_nett_salary(salary, bonus):
    nett_salary = salary + bonus
    return nett_salary

def display(id,salary,unit_sold,bonus,nett_salary):

    print("\n==========================")
    print("        Salary Slip       ")
    print("==========================")
    print("Staff ID \t :",id)
    print("Staff Salary \t : RM {:.2f}".format(salary))
    print("Unit Sold \t :",unit_sold)
    print("Bonus   \t : RM {:.2f}".format(bonus))
    print("Nett Salary \t : RM {:.2f}".format(nett_salary))

print("==========================")
print("         DATA ENTRY       ")
print("==========================")
id = int(input("Enter Staff ID   \t : "))
salary = float(input("Enter Staff Salary \t : RM "))
unit_sold = int(input("Enter Total Unit Sold \t : "))

bonus = get_bonus(unit_sold,salary)
nett_salary = get_nett_salary(salary, bonus)

display(id,salary,unit_sold,bonus,nett_salary)