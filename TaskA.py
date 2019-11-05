import random
import string


class Bank:
    def __init__(self):
        self.name = input("Enter the name for your Bank: ")
        self.address = input("Enter the address of your Bank: ")
        self.branch_code = input("Enter the branch code of Bank: ")
        self.accounts = {}

    def __repr__(self):
        return self.name + "  " + self.address

    def create_account(self):
        acc = BankAccount()
        acc.bank_name = self.name
        self.accounts.update({acc.get_acc_no() : acc})

    def accounts_in_bank(self):
        for acc in self.accounts.values():
            print(acc)

    def deposit_money(self):
        acc_no = input("Enter the Account No#: ")
        if (acc_no in self.accounts ):
            self.accounts[acc_no].deposit_money_acc()
        else:
            print("Incorrect Account NO#")

    def draw_money(self):
        acc_no = input("Enter the Account No#: ")
        if (acc_no in self.accounts):
            self.accounts[acc_no].draw_money_acc()
        else:
            print("Incorrect Account NO#")

    def deposit_bill(self):
        acc_no = input("Enter the Account No#: ")
        if (acc_no in self.accounts):
            self.accounts[acc_no].deposit_bill_acc()
        else:
            print("Incorrect Account NO#")

    def recent_transactions(self):
        acc_no = input("Enter the Account No#: ")
        if (acc_no in self.accounts):
            self.accounts[acc_no].recent_transactions_acc()
        else:
            print("Incorrect Account No#")

    def transfer_fund(self):
        acc_no = input("Enter Your Account No#: ")
        if (acc_no in self.accounts):
            recv = input("Enter the Account Number of receiver: ")
            if (recv in self.accounts):
                fund = int(input("Enter the amount you want to transfer: "))
                if (fund > 0 and fund <= self.accounts[acc_no].get_balance()):
                    self.accounts[acc_no].update_balance(-fund)
                    self.accounts[acc_no].update_balance(fund)
                else:
                    print("Incorrect Amount!!")
            else:
                print("Invalid Reveiver Account No#!!")
        else:
            print("Incorrect Account No#")

    def compare_accounts(self):
        acc_no = input("Enter the Account No#: ")
        if (acc_no in self.accounts):
            my_bal = self.accounts[acc_no].get_balance()
            accounts = self.accounts.values()
            equal = []
            larger = []
            smaller = []
            for acc in accounts:
                if (my_bal == acc.get_balance()):
                    equal.append(acc)
                elif(my_bal < acc.get_balance()):
                    larger.append(acc)
                else:
                    smaller.append(acc)
            print("Smaller accounts: ")
            for i in smaller:
                print(i)
            print("Equal accounts: ")
            for i in equal:
                print(i)
            print("Larger accounts: ")
            for i in larger:
                print(i)

        else:
            print("Incorrect Account NO#")


class BankAccount:
    def __init__(self):
        self.bank_name = None
        self.name = input("Enter the FULLNAME: ")
        self.cnic = input("Enter the CNIC#: ")
        self.accountNo =  ''.join(random.choice(string.digits) for _ in range(3))
        self.typ = input("Enter the account type (CURRENT or SAVINGS): ").title()
        self.address = input("Enter the address: ")
        self.phone = input("Enter the phone#: ")
        self.balance = 0
        self.transactions = []
        print("Account created!")

    def __repr__(self):
        return "Account Name: " + self.name + "Account Number: " + self.accountNo

    def check_balance(self):
        return self.balance

    def type_acc(self):
        print(self.typ)

    def deposit_money_acc(self):
        deposit_amount = float(input("Enter amount to be Deposited: "))
        self.balance += deposit_amount
        self.transactions.append(+deposit_amount)
        print("New Balance: " + str(self.balance))

    def draw_money_acc(self, limit=1000):
        withdraw_ammount = float(input("Enter amount to be Withdrawn: "))
        if (self.balance >= withdraw_ammount and withdraw_ammount <= limit):
            self.balance -= withdraw_ammount
            self.transactions.append(-withdraw_ammount)
            print("Remaining Balance: " + str(self.balance))
        else:
            print("Insufficient Balance or Limit Exceeded!!")

    def deposit_bill_acc(self):
        bill_amount = float(input("Enter amount to be paid for Bill: "))
        if (self.balance >= bill_amount):
            self.balance -= bill_amount
            self.transactions.append(-bill_amount)
            print("Bill has been paid.\nRemaining Balance: " + str(self.balance))
        else:
            print("Insufficient Balance!!")

    def recent_transactions_acc(self):
        if len(self.transactions) < 1:
            return "No Transaction made!"
        else:
            return self.transactions.pop()

    def get_balance_acc(self):
        return self.balance

    def update_balance(self, bal):
        self.balance += bal

    def get_acc_no(self):
        return self.accountNo


flag = True
while flag:
    print("Press \"1\" for Creating a Bank or \"q\" for Exit")
    choice = input("Enter the choice: ")
    if (choice == "1"):
        b = Bank()
        while flag:
            print("Press \"1\" for creating a bank Account")
            print("Press \"2\" for Deposit Money")
            print("Press \"3\" for Withdraw Money")
            print("Press \"4\" for Deposit the Bill")
            print("Press \"5\" for Recent Transaction")
            print("Press \"6\" for Tranfer Funds")
            print("Press \"7\" for Comparing with other accounts")
            print("Press \"q\" for Exit")
            choice = input("Enter the choice: ")
            if (choice == "1"):
                b.create_account()
            elif (choice == "2"):
                b.deposit_money()
            elif (choice == "3"):
                b.draw_money()
            elif (choice == "4"):
                b.deposit_bill()
            elif (choice == "5"):
                b.recent_transactions()
            elif (choice == "6"):
                b.transfer_fund()
            elif (choice == "7"):
                b.compare_accounts()
            elif (choice == "q" or choice == "Q"):
                flag = False
            else:
                print("Invalid Input!!")
    elif (choice == "q" or choice == "Q"):
        flag = False
    else:
        print("Invalid Input!!")