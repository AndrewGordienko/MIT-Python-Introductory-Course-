balance =
annualInterestRate =

init_balance = balance
monthlyPayment = 0
monthlyInterestRate = annualInterestRate/12

while balance > 0:
    for i in range(12):
        unpaidBalance = balance - monthlyPayment
        balance = unpaidBalance + unpaidBalance * monthlyInterestRate
        
    if balance > 0:
        monthlyPayment += 10
        balance = init_balance
        
    elif balance <= 0:
        break

print("Lowest Payment: {}".format(monthlyPayment))