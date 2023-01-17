# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 12:25:35 2023

@author: Nalian Lu
Update: define get_savings function
        The same as test cases.
"""

# get_savings function ===========================================================
# Function name should not be the same of any variable name, or it will result in 
# TypeError: 'float' object is not callable
def get_savings(current_savings, annual_salary, portion_saved, annual_r, semiannual_raise, period):
    # initialize
    savings = current_savings
    # save increase
    for t in range(period):
        if t%6==0 and t!=0:
            annual_salary = annual_salary*(1+semiannual_raise)
        savings = savings*(1+annual_r/12)+portion_saved*annual_salary/12
    # return
    return savings

# input ======================================================================
# savings
current_savings = 0
annual_r = 0.04
semiannual_raise = 0.07
period = 36
annual_salary = int(input('Enter your starting annual salary: '))
# costs
total_cost = 1000000
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment

# optimal portion_saved ======================================================
low = 0
high = 10000
ans = (low+high)//2 # integer division
epsilon = 100

# largest savings (savings rate = 100% <=> high/10000)
largest_savings = get_savings(current_savings, annual_salary, high/10000, annual_r, semiannual_raise, period)

if largest_savings < down_payment:
    print('It is not possible to pay the down payment in three years.')

else:
    # first guess
    numGuesses = 1 # initialize
    savings = get_savings(current_savings, annual_salary, ans/10000, annual_r, semiannual_raise, period)
    print(numGuesses,savings)
    while abs(savings-down_payment) > epsilon:
        if savings < down_payment:
            low = ans
        else:
            high = ans
        ans = (low+high)//2 # We need to put new ans before new savings or the result will print (true_ans+high/low)//2 rather than true_ans
        savings = get_savings(current_savings, annual_salary, ans/10000, annual_r, semiannual_raise, period)
        numGuesses += 1
        print(numGuesses,savings,ans/10000)

    print('Best savings rate:', ans/10000)
    print('Steps in bisection search:', numGuesses)