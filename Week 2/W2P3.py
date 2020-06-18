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