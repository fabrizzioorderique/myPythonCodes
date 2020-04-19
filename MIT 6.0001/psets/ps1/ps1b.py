# # #####################
# # ps1b
# # PSET 1B
# # #####################

#inputs
annual_salary = float(input("Annual salary: "))
portion_saved = float(input("Monthly portion saved: "))
total_cost = float(input("Cost of your dream home: "))
semi_annual_raise = float(input("Enter semi-annual raise:"))

#knowns
portion_down_payment = 0.25
current_savings = 0
monthly_salary = annual_salary/12
r = 0.04

#calculates months
months = 0
while current_savings <= portion_down_payment*total_cost:
    months+=1
    current_savings+=(current_savings*r/12)
    current_savings+=portion_saved*monthly_salary
    if months%6 == 0:
        annual_salary+=semi_annual_raise*annual_salary
        monthly_salary = annual_salary/12

print("Number of months:",months)