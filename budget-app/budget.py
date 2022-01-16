class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0
    def deposit(self, amount, description=""):
        transaction = {}
        transaction["amount"], transaction["description"] = amount, description
        self.ledger.append(transaction)
        self.balance += amount
    def get_balance(self):
        return self.balance
    def check_funds(self, amount):
        return self.balance > amount
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            transaction = {}
            transaction["amount"], transaction["description"] = -amount, description
            self.ledger.append(transaction)
            self.balance -= amount
            return True
        else:
            return False
    def transfer(self, amount, catergory):
        pass




def create_spend_chart(categories):
    pass

if __name__ == "__main__":
    pass