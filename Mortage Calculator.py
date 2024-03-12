def calculate_mortgage(purchase_price):
    down_payment_percentage = 0.10
    annual_interest_rate = 0.12
    monthly_payment_percentage = 0.05
    down_payment = purchase_price * down_payment_percentage
    
    balance = purchase_price - down_payment
    monthly_payment = balance * monthly_payment_percentage
    monthly_interest_rate = annual_interest_rate / 12

    print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format(
        "Month", "Balance", "Interest Owed", "Principal Paid", "Payment", "Remaining Balance"))

    month = 1
    while balance > 0:
        interest_payment = balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        
        if principal_payment > balance:
            principal_payment = balance
            
        payment = interest_payment + principal_payment        
        
        print("{:<10} ${:<19.2f} ${:<19.2f} ${:<19.2f} ${:<19.2f} ${:<19.2f}".format(
            month, balance, interest_payment, principal_payment, payment, balance - principal_payment))
        
        balance -= principal_payment

        month += 1

purchase_price = float(input("Enter the purchase price: $"))

calculate_mortgage(purchase_price)

