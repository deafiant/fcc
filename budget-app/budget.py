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
    def get_balance(self):
        return self.balance
    def get_amounts(self):
        amounts = []
        for entry in self.ledger:
            amounts.append(entry["amount"])
        return amounts
    def check_funds(self, amount):
        return self.balance >= amount
    def deposit(self, amount, description=""):
        transaction = {}
        transaction["amount"], transaction["description"] = amount, description
        self.ledger.append(transaction)
        self.balance += amount
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
    grand_total = 0
    items = []
    spending = []
    for expense in categories:
        items.append(expense.get_name())
        amounts = expense.get_amounts()
        total = 0
        for nbr in amounts:
            if nbr < 0:
                total += nbr
                grand_total += nbr
        spending.append(total)
    percents = [int((i/grand_total*100)//10*10) 
                for i in spending]
    chart = "Percentage spent by category\n"
    for row in range(11):
        chart += f"{(10 - row) * 10:>3}|"
        for percent in percents:
            if (10 - row) * 10 <= percent:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"
    chart += f"    {'-' * ((len(categories) * 3) + 1)}\n"
    longest = max([ len(i) for i in items ])
    padded = [ i.ljust(longest) for i in items ]
    for row in range(longest):
        chart += "    "
        for column in range(len(categories)):
            chart += f" {padded[column][row]} "
        if row + 1 != longest:
            chart += " \n"
        else:
            chart += " "
    # Sigh! Each row of the expected had an extra space. 
    # Had to get a diff tool to see this.
    return chart

if __name__ == "__main__":
    food = Category("Food")
    entertainment = Category("Entertainment")
    business = Category("Business")
    food.deposit(900, "deposit")
    entertainment.deposit(900, "deposit")
    business.deposit(900, "deposit")
    food.withdraw(105.55)
    entertainment.withdraw(33.40)
    business.withdraw(10.99)
    print(repr(create_spend_chart([business, food, entertainment])))
    print(create_spend_chart([business, food, entertainment]))
