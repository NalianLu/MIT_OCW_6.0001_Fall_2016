# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 20:19:53 2023

@author: Nalian Lu
"""
# cost
total_cost = 1000000
portion_down_payment = 0.25
down_payment = total_cost*portion_down_payment

# monthly_save
annual_salary = float(input('Enter your starting annual salary: '))
monthly_salary = annual_salary/12
semiannual_raise = 0.07

# monthly_return
r = 0.04
monthly_r = r/12

# period
t = 36 # in month

# largest savings (savings rate = 100%)
largest_savings = monthly_salary # initialize at the end of 1st month 
for p in range(1,t):
    if (1+p)%6==0:
        monthly_salary = monthly_salary*(1+semiannual_raise)
    largest_savings = largest_savings*(1+monthly_r)+monthly_salary

if largest_savings<down_payment:
    print('It is not possible to pay the down payment in three years.')

else:
# portion_saved
    x = down_payment
    epsilon = 100
    numGuesses = 0
    low = 0
    high = 10000
    ans = (high+low)//2
    monthly_salary = annual_salary/12
    monthly_save = (ans/10000)*monthly_salary
    current_savings = monthly_save # initialize at the end of 1st month 
    
    while abs(current_savings-x) >= epsilon:
        monthly_salary = annual_salary/12
        monthly_save = (ans/10000)*monthly_salary
        current_savings = monthly_save # initialize at the end of 1st month 
        for p in range(1,t):
            if (p+1)%6==0:
                monthly_save = monthly_save*(1+semiannual_raise)
            current_savings = current_savings*(1+monthly_r)+monthly_save
        # bisection search
        if current_savings<x:
            low = ans
        else:
            high = ans
        ans = (high+low)//2
        numGuesses += 1
    print('Best savings rate:', ans/10000)
    print('Steps in bisection search:', numGuesses)