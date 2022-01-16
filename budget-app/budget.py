class Category:
    def __init__(self, category):
        self.name = category
        self.ledger = []
        self.balance = 0
    def __str__(self):
        rep = self.name.center(30, "*") + "\n"
        for entry in self.ledger:
        # Notes: "<23.23" = left align, pad to 23 &
        # truncate to 23. ">7.2f" = right align,
        # pad to 7 & convert to float with 2 decimal
        # places.
            rep += f'{entry["description"]:<23.23}'
            rep += f'{entry["amount"]:>7.2f}\n'
        rep += "Total: " + str(self.balance)
        return rep
    def get_name(self):
            return self.name
    def deposit(self, amount, description=""):
        transaction = {}
        transaction["amount"], transaction["description"] = amount, description
        self.ledger.append(transaction)
        self.balance += amount
    def get_balance(self):
        return self.balance
    def check_funds(self, amount):
        return self.balance >= amount
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            transaction = {}
            transaction["amount"], transaction["description"] = -amount, description
            self.ledger.append(transaction)
            self.balance -= amount
            return True
        else:
            return False
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.get_name()}")
            category.deposit(amount, f"Transfer from {self.get_name()}")
            return True
        else:
            return False

def create_spend_chart(categories):
    pass

if __name__ == "__main__":
    beer = Category("Beer")
    beer.deposit(50, "Wage")
    print(beer.get_balance())
    beer.withdraw(20, "Beer")
    beer.withdraw(10, "More beer, more beer, more beer")
    print(beer.get_balance())
    print(beer.check_funds(10))
    print(beer.check_funds(30))
    print(beer)