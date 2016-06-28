"""
Kata: Tax Calculator (7 kyu)

Description:
Write a function to calculate compound tax using the following table:

    For $10 and under, the tax rate should be 10%.

    For $20 and under, the tax rate on the first $10 is %10, and the tax on the rest is 7%.

    For $30 and under, the tax rate on the first $10 is still %10, the rate for the next $10 is still 7%, and everything else is 5%.

    Tack on an additional 3% for the portion of the total above $30.

    Return 0 for invalid input(anything that's not a positive real number).

Examples:

    An input of 10, should return 1 (1 is 10% of 10)

    An input of 21, should return 1.75 (10% of 10 + 7% of 10 + 5% of 1)

* Note that the returned value should be rounded to the nearest penny.


URL: https://www.codewars.com/kata/tax-calculator
"""

def tax_calculator(total):
    # Return zero for invalid instances
    if not (isinstance(total, int) or isinstance(total, float)) or total <= 0:
        return 0

    # $10 or less
    if total <= 10:
        return round(0.1*total,2)

    # $20 or less
    elif total <= 20:
        return round(1 + 0.07*(total-10), 2)

    # $30 or less
    elif total <= 30:
        return round(1.7 + 0.05*(total-20), 2)

    # More than $30
    else:
        return round(2.2 + 0.03*(total-30), 2)