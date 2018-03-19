"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of income_period."""
    income_period = int(input("How many income_period? "))
    return income_period


def income_records(income_period):
    incomes = []
    for month in range(1, income_period + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)
    return incomes


def statement(income_period, incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, income_period + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


income_period = main()
incomes = income_records(income_period)
statement(income_period, incomes)