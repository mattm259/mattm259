
"""
Created on Wed Dec 20 03:28:42 2023

@author: mattmeadows
"""

import math

# Code to develop a calculator for investment and/or bonds
# Asks for either an investment or bond
# If investment is inputed, user inputs: amount, interest(yearly) and period (years)
# - Choice of simple or compound interest can be calculated
# - Returns amount after interest 
# If bond is inputed, user inputs: amount, interest(monthly) and period (months)
# - Returns the amount needed/month to repay

print("===============================================================================")
print('')
print(" investment - to calculate the amount of interest you'll earn on your investment ")
print('')
print(" bond - to calculate the amount you'll have to pay on a home loan ")
print('')
print("===============================================================================")                  


choice_words = ["investment", "bond"]

while True:
    user_input = input(" Enter either 'investment' or 'bond' from the menu above to proceed:  ")  
    cap_input = user_input.lower()
    if cap_input in choice_words:
        print('')
        print(" You entered: ", user_input)
        break
    else:
        print('')
        print(" Invalid input.")  
    
def simp_interest(dep_input, int_input, years_input): 
    simp = int(dep_input)*( 1 + (int(int_input)/100 * int(years_input)))
    return simp

def com_interest(dep_input, int_input, years_input):
    com = int(dep_input)*( 1 + int(int_input)/100 )**int(years_input)
    return com
 
 
if cap_input == 'investment':
    print('')
    print("===============================================================================")
    print('')
    dep_input = input(" How much money would you like to deposit (£) ? : ")
    print('')
    int_input = input(" What is the interest rate (%) ? : ")
    print('')
    years_input = input(" How many years are you planning to invest for ? : ")
    print('')
    interest = input(" Would you like simple or compound interest ? : ")
    capint_input = interest.lower()
    choiced_words = ["simple", "compound"]
    print('')
    if capint_input in choiced_words:
        print('')
        print(" You entered: ", interest)
    else:
            print('')
            print(" Invalid input. Please enter either 'simple' or 'compound' ") 
    if capint_input == 'simple':
        print('')
        print("===============================================================================")
        print('')
        siminterest_res = simp_interest(dep_input, int_input, years_input)
        print("You will get back : ", "£", round(siminterest_res ))
    if capint_input == 'compound':
        print('')
        print("===============================================================================")
        print('')
        cominterest_res = com_interest(dep_input, int_input, years_input) 
        print("You will get back : ", "£", round(cominterest_res ))





    

        
def bond_repay(house_input, monint_input, month_input): 
    repay = (int(monint_input)/1200 * int(house_input))/(1 - ( 1 + int(monint_input)/1200)**(-1*int(month_input)))
    return repay

    
if cap_input == 'bond':
    print('')
    print("===============================================================================")
    print('')
    house_input = input(" How much money is the current value of your house (£) ? : ")
    print('')
    monint_input = input(" What is the interest rate (%) ? : ")
    print('')
    month_input = input(" How many months are you planning to take before repaying ? : ")
    print('')
    bond_repay_res = bond_repay(house_input, monint_input, month_input)
    print('')
    print("===============================================================================")
    print('')
    print(" You will have to pay approximately : ", "£", round(bond_repay_res), "per month or","£", float(bond_repay_res) ,"exactly")
                              
 
  

    

 