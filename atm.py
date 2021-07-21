class Atm:
    def __init__(self, cardnum, pinnum, balance):
        self.pinnum = pinnum
        self.cardnum = cardnum
        self.balance = balance

    def cashWithdrawal(self):
        amount = int(input("Enter the amount you want to withdraw:"))
        pin = int(input('Verify PIN number'))
        if(amount>self.balance):
            print('Not enough money!')
        elif(amount <= self.balance and pin == self.pinnum):
            self.balance = self.balance - amount
            print('Withdrawal successful. New balance is ' + str(self.balance))
        elif(pin != self.pinnum):
            print('Incorrect PIN!')

    def checkBalance(self):
        print(self.balance)

    def cashDeposit(self):
        deposition = int(input("Enter the deposition amount:"))
        pinn = int(input('Verify PIN number'))
        if(pinn == self.pinnum):
            self.balance = self.balance + deposition
            print('Deposit succesful! New balance is ' + str(self.balance))
        elif(pinn != self.pinnum):
            print('Incorrect PIN!')


cardnum = int(input('Enter card number:'))
pinnum = int(input('Enter your PIN number:'))
balance = int(input('Enter your current bank balance:'))
atm = Atm(cardnum, pinnum, balance)
choice = input('What would you like to do today (withdraw, deposit, check balance):')
if(choice == 'withdraw'):
    atm.cashWithdrawal()
elif(choice == 'deposit'):
    atm.cashDeposit()
elif(choice == 'check balance'):
    atm.checkBalance()
    
    
