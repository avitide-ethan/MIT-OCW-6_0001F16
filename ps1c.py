print("This program will calculate how many months it will take to save up enough money for a down payment.")
annual_salary = float(input("Enter your starting salary: "))

monthly_salary = annual_salary / 12
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
current_savings = 0
r = 0.04
months = 0
x = 5000  # some value between 0 and 10,000 where portion_saved = x / 1000
searching = True
#  test savings rate

#
while searching:
    for months in range(0, 36):
        print(f"Month {months}, monthly salary {monthly_salary} savings beginning of month: {current_savings}")
        current_savings = current_savings + current_savings * r/12  # annual return of r
        current_savings = current_savings + monthly_salary * (x / 1000)
        print(f"Savings end of month: {current_savings}")
        months += 1
        if (months - 1) % 6 == 0 and months != 1:
            monthly_salary = monthly_salary * (1 + semi_annual_raise)

        if months < 36 and current_savings > total_cost * portion_down_payment:  # saving too much
            print("You saving too much!!")
            x = x/2
            current_savings = 0
            monthly_salary = annual_salary / 12
            break
        if months == 36 and current_savings < total_cost * portion_down_payment:  # not saving enough
            x = x + (10000-x)/2


print("Savings rate is : {}".format(x/1000))
