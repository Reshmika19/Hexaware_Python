from .accounts import accounts

def deposit(account_no, amount):
    if account_no not in accounts:
        return "Account not found!"
    accounts[account_no]["balance"] += amount
    return f"Deposited {amount} to Account {account_no}. New Balance: {accounts[account_no]['balance']}"

def withdraw(account_no, amount):
    if account_no not in accounts:
        return "Account not found!"
    if accounts[account_no]["balance"] < amount:
        return "Insufficient balance!"
    accounts[account_no]["balance"] -= amount
    return f"Withdrew {amount} from Account {account_no}. New Balance: {accounts[account_no]['balance']}"

def transfer(from_acc, to_acc, amount):
    if from_acc not in accounts or to_acc not in accounts:
        return "One or both accounts not found!"
    if accounts[from_acc]["balance"] < amount:
        return "Insufficient balance for transfer!"
    accounts[from_acc]["balance"] -= amount
    accounts[to_acc]["balance"] += amount
    return f"Transferred {amount} from {from_acc} to {to_acc}. New Balance: {accounts[from_acc]['balance']}, {to_acc}: {accounts[to_acc]['balance']}"
