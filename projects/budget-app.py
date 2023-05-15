class Category:
    def __init__(self, category):
        self.category_name = category
        self.ledger = list()

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False

        self.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self):
        income_funds = sum([item["amount"]
                           for item in self.ledger if item["amount"] > 0])
        expense_funds = sum([item["amount"]
                            for item in self.ledger if item["amount"] < 0])

        return income_funds + expense_funds

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False

        self.withdraw(amount, f"Transfer to {category.category_name}")
        category.deposit(amount, f"Transfer from {self.category_name}")

        return True

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False

        return True

    def __str__(self):
        class_name = self.category_name
        title_length = 30
        gap_title = (title_length - len(class_name)) // 2

        first_line = str(gap_title * '*') + class_name + str(gap_title * '*')

        if len(first_line) < title_length:
            first_line += '*'

        itens_line = ""

        for item in self.ledger:
            amount, description = ["{:.2f}".format(
                item["amount"]), item["description"]]
            gap_item = len(description) + len(str(amount))

            if len(description) > 23:
                itens_line += description[:23] + \
                    str((7 - len(str(amount))) * ' ') + \
                    str(amount) + "\n"
            else:
                itens_line += item["description"] + \
                    str((30 - gap_item) * ' ') + str(amount) + "\n"

        last_line = "Total: {:.2f}".format(self.get_balance())

        return first_line + "\n" + itens_line + last_line


def create_spend_chart(categories):
    title = "Percentage spent by category\n"

    categories_name = list(categorie.category_name for categorie in categories)
    categories_percentage_spent = list()
    max_categories_name = max(len(name) for name in categories_name)

    all_categories_expense = 0

    for categorie in categories:
        all_categories_expense += sum([item["amount"]
                                      for item in categorie.ledger if item["amount"] < 0])

    graph = ""

    for categorie in categories:
        expense_funds = sum([item["amount"]
                            for item in categorie.ledger if item["amount"] < 0])

        if all_categories_expense == 0:
            percentage_spent = 0
        else:
            percentage_spent = (-expense_funds / -all_categories_expense) * 100
        percentage_spent_by_ten = percentage_spent - (percentage_spent % 10)

        categories_percentage_spent.append(percentage_spent_by_ten)

    for line in range(100, -10, -10):
        points = ""
        for percentage in categories_percentage_spent:
            if percentage >= line:
                points += "o  "
            else:
                points += "   "

        graph += "{:>3d}| {}\n".format(line, points)

    graph += "    {}\n".format("-" * (len(categories) * 3 + 1))

    for i in range(max_categories_name):
        category_line = "    "
        for category_name in categories_name:
            if i < len(category_name):
                category_line += " {} ".format(category_name[i])
            else:
                category_line += "   "

        if i < max_categories_name - 1:
            category_line += " \n"
        if i == max_categories_name - 1:
            category_line += " "

        graph += category_line

    return title + graph
