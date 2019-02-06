# ex4-TipTaxCalc

###############################################################################

# Create a program that
# accepts input for a meal "Enter your meal amount: "
# accepts input for a tip % (of your choice, use between 15 and 25),
# adds NJ sales tax (to meal amount), of NJ which currently is 6.625 percent
# totals everything up.
# prints the tip amount
# prints the meal total with tax
# prints the meal total with tax pus the tip (your total out of pocket)

###############################################################################

# inputs and tax amount
tax = .06625
meal_total = float(input('How much was your meal? '))
tip = float(input('How much tip would you like to give (between 15 and 25)? '))

# make sure the input is between 15 and 25, unnecessary but messing around
if tip > 25:
    print('You are being too generous. Please input between 15 and 25.')
    tip = float(input('How much tip would you like to give: '))
elif tip < 15:
    print("Don't be so stingy, input between 15 and 25.")
    tip = float(input('How much tip would you like to give: '))
else:
    print('Your tip and meal calculations are as follows:')

# calculations
tip_amount = meal_total * (tip / 100)
total_tax = meal_total * tax
meal_and_tax = meal_total + total_tax
total_cost = meal_and_tax + tip_amount

# tried to find out how to round properly simply
print(f'You will tip ${round(tip_amount, 2)}.')
print(f'Your meal with tax comes to ${round(meal_and_tax, 2)}.')
print(f'Your total out of pockets is ${round(total_cost, 2)}.')
