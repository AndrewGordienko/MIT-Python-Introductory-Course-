#Write a program to calculate the credit card balance after one year if a person
#only pays the minimum monthly payment required by the credit card company each month.
#The following variables contain values as described below:

#balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal
#monthlyPaymentRate - minimum monthly payment rate as a decimal

#For each month, calculate statements on the monthly payment and remaining balance.
#At the end of 12 months, print out the remaining balance.
#Be sure to print out no more than two decimal digits of accuracy - so print
#Remaining balance: 813.41

balance = 1000
annualInterestRate = 0.2
monthlyPaymentRate = 0.2

monthlyInterestRate = annualInterestRate/12

for i in range(12):
    minimumMonthlyPayment = monthlyPaymentRate * balance
    balance -= minimumMonthlyPayment
    balance = balance + (monthlyInterestRate * balance)


print("Remaining balance: {}".format(round(balance, 2)))
