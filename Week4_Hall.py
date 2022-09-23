# DSC 510
# Week 4
# Programming Assignment Week 4
# Author Kimberly Hall
# 9/22/2022

# This program is designed to calculate cost of fiber optic cable to be installed

print('Welcome to the price calculator!')

# User will be asked to provide their company name.
company_name = input('Please provide your company name.')
# User will input amount of fiber optic cable needed to be installed, making float for rounding purposes
feet_needed = input('How many feet of cable will you need installed?')
feet_needed = float(feet_needed)

#If statement function to calculate discount rates
def calculator():
    if feet_needed > 500:
        install_cost = 0.50
    elif feet_needed > 250:
        install_cost = 0.70
    elif feet_needed > 100:
        install_cost = 0.80
    else:
        install_cost = 0.87
    return (install_cost)

# Total installation cost is calculated into a function
def total_calc (feet , price):
    return print('Total Cost: $', format((feet * price), '.2f'))

# Program prints receipt
print('Below is your receipt')
print('Company Name:', company_name)
print('Feet of fiber to be installed' , feet_needed , 'feet')
print('Cost per foot $', format(calculator() , '.2f'))
total_calc(feet_needed , calculator())

#Change 1
#Change made: added if else statements to code
#Date of Change: 9/13/2022
#Author: Kimberly Hall
#Change Approved by: Kimberly Hall
#Date moved to production: 9/13/2022

def main():
    pass


if __name__ == '__main__':
    main ()