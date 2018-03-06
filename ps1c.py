print("This program will calculate how many months it will take to save up enough money for a down payment.")
annual_salary = float(input("Enter your starting salary: "))

total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
savings_needed = portion_down_payment * total_cost
r = 0.04  # interest rate
months = 0

upper_sr_limit = 10000
lower_sr_limit = 0
saving_rate_times_100 = 5000  # some value between 0 and 10,000 where portion_saved = x / 100

searching = True
bis_count = -1

while searching:
    bis_count += 1
    current_savings = 0
    monthly_salary = annual_salary / 12
    for months in range(0, 36):
        current_savings = current_savings + current_savings * r/12  # savings accrued from return on current savings
        current_savings = current_savings + monthly_salary * (saving_rate_times_100 / 10000)  # savings accrued from salary

        if (months + 1) % 6 == 0:
            monthly_salary = monthly_salary * (1 + semi_annual_raise)  # calculate semi-annual increase in salary

        if current_savings > 100 + savings_needed:  # saving too much
            upper_sr_limit = saving_rate_times_100
            saving_rate_times_100 = (upper_sr_limit + lower_sr_limit) / 2
            print(f"[{lower_sr_limit/10000}, {upper_sr_limit/10000}] : {saving_rate_times_100/10000}")
            break

    if -100 < current_savings - savings_needed < 100:
        print(f"You saving juuuuuust right!, {current_savings} upper: {upper_sr_limit}, lower: {lower_sr_limit}")
        searching = False

    elif current_savings < savings_needed - 100:  # not saving enough
        lower_sr_limit = saving_rate_times_100
        saving_rate_times_100 = (upper_sr_limit + lower_sr_limit) / 2
        print(f"{saving_rate_times_100/10000} : [{lower_sr_limit/10000}, {upper_sr_limit/10000}]")
        # print(f"You saving too little!! savings: {current_savings} upper: {upper_sr_limit}, lower: {lower_sr_limit}, now trying: {saving_rate_times_100}")


print("Savings rate is : {}".format(saving_rate_times_100 / 100))
print("Steps in bisection search: {}".format(bis_count))
