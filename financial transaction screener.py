# In this project, we are building a system that scans
# a list of customer transactions to flag potential fraud
#  or high-priority accounts.

transactions = [
    {'customer': 'Lawan', 'amount': 5000, 'type': 'deposit', 'location': 'Local'},
    {'customer': 'Amina', 'amount': 20000, 'type': 'withdrawal', 'location': 'Local' 'International'},
    {'customer': 'John', 'amount': 1500, 'type': 'deposit', 'location': 'Local'},
    {'customer': 'Sara', 'amount': 30000, 'type': 'withdrawal', 'location': 'International'},
    {'customer': 'Mike', 'amount': 7000, 'type': 'deposit', 'location': 'Local'},   
    {'customer': 'Nina', 'amount': 25000, 'type': 'withdrawal', 'location': 'International'},
    {'customer': 'Tom', 'amount': 1200, 'type': 'deposit', 'location': 'Local'},
    {'customer': 'Lucy', 'amount': 40000000, 'type': 'withdrawal', 'location': 'International'},
    {'customer': 'Eve', 'amount': 8000, 'type': 'deposit', 'location': 'Local'},
]

fraudulent_transactions = []  # list to hold flagged transactions
vip_customers = []  # list to hold high-priority customers
for transaction in transactions:
    if transaction['location'] == 'International' and transaction['amount'] > 1000000:
        fraudulent_transactions.append(transaction['customer'])
        print(f"""FRAUD ALERT: '{transaction['customer']}'
               has a suspicious transaction of {transaction['amount']:,}
                 and is {transaction['location']} transaction.""")
    elif transaction['amount'] > 10000:
        vip_customers.append(transaction['customer'])
        print(f"VIP CUSTOMER : '{transaction['customer']}' made a high transaction of {transaction['amount']:,}")
        
print(f"Total fraudulent transactions detected: {len(fraudulent_transactions)}")
print(f"Total VIP customers detected: {len(vip_customers)}")
