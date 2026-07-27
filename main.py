from tools import (
    get_total_salary,
    get_total_expenses,
    get_balance,
    expense_by_category,
    largest_expense,
)

def main():
    print("Hello from bank-assistant!")


if __name__ == "__main__":
    main()

print(get_total_salary.invoke({}))
print(get_total_expenses.invoke({}))
print(get_balance.invoke({}))
print(expense_by_category.invoke({"category": "Food"}))
print(largest_expense.invoke({}))