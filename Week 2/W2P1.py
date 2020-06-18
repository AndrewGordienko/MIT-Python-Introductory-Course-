balance = 1000
annualInterestRate = 0.2
monthlyPaymentRate = 0.2

monthlyInterestRate = annualInterestRate/12

for i in range(12):
    minimumMonthlyPayment = monthlyPaymentRate * balance
    balance -= minimumMonthlyPayment
    balance = balance + (monthlyInterestRate * balance)


print("Remaining balance: {}".format(round(balance, 2)))