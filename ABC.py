# ---------------------------------------
# DSA 230/CSCI 492/CSCI 593, Intro to DS|
# Lab 2: Income Tax Calculator          |
# Your Name                             |
# Date:                                 |
# ---------------------------------------
# This program calculates the tax owed  |
# by a single (unmarried) individual in |
# the year 2024 based on income.        |
# ---------------------------------------

# Function to calculate the tax for an unmarried individual
def unmarried_individual_tax(income):
    if income <= 11600:
        total_tax = income * 0.10
    elif income <= 47150:
        total_tax = 1160 + (income - 11600) * 0.12
    elif income <= 100525:
        total_tax = 5426 + (income - 47150) * 0.22
    elif income <= 191950:
        total_tax = 17168.50 + (income - 100525) * 0.24
    elif income <= 243725:
        total_tax = 39110.50 + (income - 191950) * 0.32
    elif income <= 609350:
        total_tax = 55678.50 + (income - 243725) * 0.35
    else:
        total_tax = 183647.25 + (income - 609350) * 0.37

    return total_tax

# ---------------------------------------

# Function to display income and tax owed
def process(income):
    print("The 2024 taxable income is ${:.2f}".format(income))
    tax_owed = unmarried_individual_tax(income)
    print("An unmarried individual owes ${:.2f}\n".format(tax_owed))

# ---------------------------------------

# Main function to run test cases
def main():
    process(5000)      # Test case 1
    process(20000)     # Test case 2
    process(50000)     # Test case 3
    process(100000)    # Test case 4
    process(200000)    # Test case 5
    process(400000)    # Test case 6
    process(600000)    # Test case 7

# ---------------------------------------

main()
