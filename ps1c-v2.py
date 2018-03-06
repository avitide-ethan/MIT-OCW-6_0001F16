def search(initial_savings_rate, salary):
    # CONSTANTS
    semi_annual_raise = 0.07
    annual_return = 0.04
    down_payment_percent = 0.25
    total_house_cost = 1000000

    # VARIABLES TO UPDATE
    savings_rate_try = 0.5
    search_count = 0
    savings_rate_lower = 0
    savings_rate_upper = 1

    # DERIVED VARIABLES
    monthly_return = annual_return / 12

    down_payment = down_payment_percent * total_house_cost

    def single_search_attempt(savings_rate_try):
        # output total amount saved minus down_payment
        current_savings = 0
        monthly_salary = salary / 12
        for months in range(36):
            current_savings += current_savings * monthly_return
            current_savings += monthly_salary * savings_rate_try
            if (months + 1) % 6 == 0:
                monthly_salary += monthly_salary * semi_annual_raise
        return current_savings - down_payment

    if single_search_attempt(1) < -100:
        print("Impossible to save that much!")
        return

    while True:
        difference = single_search_attempt(savings_rate_try)

        if difference > 100:
            savings_rate_upper = savings_rate_try
            savings_rate_try = (savings_rate_lower + savings_rate_upper) / 2
        elif difference < -100:
            savings_rate_lower = savings_rate_try
            savings_rate_try = (savings_rate_lower + savings_rate_upper) / 2
        else:
            print(f"Optimal savings rate: {savings_rate_try} after {search_count} searches.")
            break
        search_count += 1


salary = int(input("Input starting salary: "))
search(0.5, salary)