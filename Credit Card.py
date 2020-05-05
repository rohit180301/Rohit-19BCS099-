class CreditCard:
    def __init__(self,customer,bank, card_number,balance):
        self.customer_name = customer
        self.bank_name = bank
        self.balance = balance
        self.credit_card_number = card_number
    def get_customer(self):
        return self.customer_name
    def get_bank(self):
        return self.bank_name
    def get_creditcard(self):
        return self.credit_card_number
    def get_balance(self):
        return self.balance
    def recharge(self):
        self.balance = 20000 + int(self.balance)
        return self.balance
if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('ROHIT','ICICI Bank','1245 7896 8574 3214',55000))
    wallet.append(CreditCard( 'RAM' , 'ANZ Bank' ,'3656 5487 9685 4512' , 40000))
    wallet.append(CreditCard( 'LAKHAN' , 'ICICI Bank' , '4565 8597 6985 3256' , 50000))
    for c in range(3):
        print( 'Customer=' , wallet[c].get_customer())
        print( 'Bank =' , wallet[c].get_bank())
        print('creditcard=',wallet[c].get_creditcard())
        print('balance=',wallet[c].get_balance())
        wallet[c].recharge()
        print("balance after recharge= ",wallet[c].get_balance() )