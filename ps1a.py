print("This program will calculate how many months it will take to save up enough money for a down payment.")
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

monthly_salary = annual_salary / 12
portion_down_payment = 0.25
current_savings = 0
r = 0.04
months = 0

while current_savings < total_cost * portion_down_payment:
# for months in range(5):
#     print(f"Month {months}")
#     print(f"Savings beginning of month: {current_savings}")
    current_savings = current_savings + current_savings * r/12  # annual return of r
    # print(f"Savings end of month: {current_savings}")
    current_savings = current_savings + monthly_salary * portion_saved
    months += 1
print("Number of months: {}".format(months))
