import csv

class Expense:
    dept_name: str
    expense_amount: float

    def __init__(self, dept_name, expense_amount):
        self.dept_name = dept_name
        self.expense_amount = expense_amount

# open the csv file
with open("city-of-seattle-2012-expenditures-dollars.csv") as file:
    # delimiter is the character that separates each column
    reader = csv.reader(file, delimiter=",")
    expense_list = []
    row_num = 1
    for list in reader:
        if row_num != 1:
            expense = Expense(list[0], list[3])
            expense_list.append(expense)
            row_num += 1
        else:
            row_num += 1

expense_dict = {}
for item in expense_list:
    #Dictionary using dept_name as a key and list of expenses as values
    if item.expense_amount == '':
        continue

    temp_amt = int(item.expense_amount)

    if not(item.dept_name in expense_dict):
        expense_dict[item.dept_name] = [temp_amt]
    else:
        expense_dict[item.dept_name].append(temp_amt)

for department in expense_dict.keys():
    total_expenses = sum(expense_dict.get(department))
    print(department + ": $" + str(total_expenses))
