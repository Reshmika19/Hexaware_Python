"""
Scenario: Banking Package
A banking app needs to manage customer accounts and perform transactions.

Modules:
- accounts.py → Create accounts, check balance.
- transactions.py → Deposit, withdraw, transfer money.

Implementation Idea:
When a customer deposits money, the program calls
banking.transactions.deposit() and then updates balance using
banking.accounts.get_balance().
"""

from banking import create_account, get_balance, deposit, withdraw, transfer

def main():
    # Create accounts
    print(create_account(101, "Reshmika", 5000))
    print(create_account(102, "Sai", 3000))

    # Check balance
    print("\nInitial Balances:")
    print("Account 101:", get_balance(101))
    print("Account 102:", get_balance(102))

    # Deposit
    print("\nTransactions:")
    print(deposit(101, 2000))

    # Withdraw
    print(withdraw(102, 1000))

    # Transfer
    print(transfer(101, 102, 1500))

    # Final balances
    print("\nFinal Balances:")
    print("Account 101:", get_balance(101))
    print("Account 102:", get_balance(102))

if __name__ == "__main__":
    main()
