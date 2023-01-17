# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 20:02:29 2023

@author: Nalian Lu
"""

# monthly_save
annual_salary = float(input('Enter your starting annual salary: '))
monthly_salary = annual_salary/12
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
monthly_save = portion_saved*monthly_salary

# monthly_return
r = 0.04
monthly_r = r/12

# cost
total_cost = float(input('Enter the cost of your dream home: '))
portion_down_payment = 0.25
down_payment = portion_down_payment*total_cost

# semi-annual_increase
semi_annual_raise = float(input('Enter the semiannual raise, as a decimal: '))

# period
current_savings = 0
t=0 # initialize
#print(t, monthly_save)
while current_savings<down_payment:
    
    if t%6==0 and t != 0:
        monthly_save = monthly_save*(1+semi_annual_raise)
        #print(t, monthly_save)
    
    current_savings = current_savings*(1+monthly_r)+monthly_save
    t += 1

print('Number of months:',t)