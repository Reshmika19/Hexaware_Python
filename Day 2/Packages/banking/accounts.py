# Store accounts in a dictionary
accounts = {}

def create_account(account_no, name, initial_balance=0):
    if account_no in accounts:
        return f"Account {account_no} already exists!"
    accounts[account_no] = {"name": name, "balance": initial_balance}
    return f"Account {account_no} created for {name} with balance {initial_balance}"

def get_balance(account_no):
    if account_no not in accounts:
        return "Account not found!"
    return accounts[account_no]["balance"]
