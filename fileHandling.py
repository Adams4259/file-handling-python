import csv

#Step 1: Define initial transactions
transactions = [
    ["ID","Amount","Type"],
    [1,500,"Deposit"],
    [2, 1000, "Withdrawal"],
    [3, 500, "deposit"],
    [4, 10000, "deposit"]
]

#Step 2: Write transaction to CSV
with open("transaction.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(transactions)


#Step 3: Append a new transaction
new_transaction = [5, 15000, "Deposit"]

with open("transaction.csv", mode="a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_transaction)


print("Transactions saved to transaction.csv")