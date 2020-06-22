#how can we calculate a more accurate fixed monthly payment than we did in Problem 2
#without running into the problem of slow code?
#We can make this program run faster using a technique introduced in lecture - bisection search!
#The following variables contain values as described below:

#balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal

#Write a program that uses these bounds and bisection search such that we can pay off the debt within a year.
#Produce the same return value as you did in Problem 2.

def payment(balance, annualInterestRate):

    monthlypayment = 10
    init_balance = balance

    epsilon = 0.01
    low = balance/12
    high = (init_balance * (1 + annualInterestRate/12)**12)/12

    while abs(balance) > epsilon:
        monthlypayment = (high + low)/2
        balance = init_balance

        for i in range(12):
            unpaidbalance = balance - monthlypayment
            interest = unpaidbalance * (annualInterestRate/12)
            balance = unpaidbalance + interest

        if balance > epsilon:
            low  = monthlypayment
        
        elif balance < - epsilon:
            high = monthlypayment
    
    return (monthlypayment)

balance = 197575
annualInterestRate = 0.21

print ("Lowest Payment: {}".format(round((payment(balance, annualInterestRate)), 2)))
