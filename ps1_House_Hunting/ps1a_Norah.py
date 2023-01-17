# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 19:11:13 2023

@author: Nalian Lu
"""

# monthly_save
annual_salary = float(input('Enter your annual salary: '))
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

# period
current_savings = 0
t=0 # initialize
# for the following periods
while current_savings<down_payment:
    current_savings = current_savings*(1+monthly_r)+monthly_save
    t += 1

print('Number of months:',t)