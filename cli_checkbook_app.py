#!/usr/bin/env python
# coding: utf-8

# In[24]:


import csv
import datetime
import pandas as pd

def log_transaction(amount, balance, transaction_type):
    with open("transactions.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - {transaction_type}: {amount}, balance: {balance}\n")

def selection_menu(choices):
    print("~~~ Welcome to your Terminal Check Book! ~~~")
    print(' ')
    print("Check Book Menu")
    print(' ')
    while True:
        for i, choice in enumerate(choices):
            print(f"{i + 1}. {choice}")
        print(' ')
        choice = input("Enter Your Choice: ")
        print(' ')
        if choice.isdigit() and int(choice) in range(1, len(choices) + 1):
            return choices[int(choice) - 1]
        print("Invalid Choice, Try Again.")

def stored_balance(balance):
    with open("balance.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["balance"])
        writer.writerow([balance])

def retrieve_balance():
    try:
        with open("balance.csv", "r") as f:
            reader = csv.reader(f)
            next(reader) # skip header
            return float(next(reader)[0])
    except (FileNotFoundError, StopIteration):
        return 0.0

def view_historical_transactions():
    try:
        df = pd.read_csv("transactions.txt", header=None, names=["Date", "Transaction"])
        print(df)
    except FileNotFoundError:
        print("Query Result, No Transactions Found.")

def main():
    balance = retrieve_balance()
    print(' ')
    while True:
        choices = ["Deposit Funds", "Withdraw Funds", "View Current Balance", "View Historical Transactions", "Quit"]
        selected_choice = selection_menu(choices)

        print(' ')
        if selected_choice == "Deposit Funds":
            amount = float(input("Enter Amount to Deposit: "))
            balance += amount
            log_transaction(amount, balance, "Deposit")
        elif selected_choice == "Withdraw Funds":
            amount = float(input("Enter Amount to Withdraw: "))
            balance -= amount
            log_transaction(amount, balance, "Withdrawal")
        elif selected_choice == "View Current Balance":
            print(' ')
            print(f"Current Balance: {balance}")
            print(' ')
        elif selected_choice == "View Historical Transactions":
            print(' ')
            view_historical_transactions()
        else:
            stored_balance(balance)
            print(' ')
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()


# In[ ]:




