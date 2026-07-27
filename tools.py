from langchain.tools import tool
import pandas as pd

EXCEL_FILE="bank_data.xlsx"

@tool
def get_total_salary() -> str :
    """
    Returns the total salary recieved from the salary sheet
    """
    
    data_from_sal_sheet = pd.read_excel(EXCEL_FILE,sheet_name="Salary")
    total_salary = data_from_sal_sheet["Amount"].sum()
    return f"Total salary received is rupees {total_salary:,.2f}"

@tool
def get_total_expenses() -> str :
    """
    Returns the total expenses spend from the Expenses sheet
    """
    
    data_from_exp_sheet = pd.read_excel(EXCEL_FILE,sheet_name="Expenses")
    total_expenses = data_from_exp_sheet["Amount"].sum()
    return f"Total expenses is rupees {total_expenses:,.2f}"

@tool
def get_balance() -> str:
    """
    Calculates remaining balance.
    """

    salary_df = pd.read_excel(EXCEL_FILE, sheet_name="Salary")
    expense_df = pd.read_excel(EXCEL_FILE, sheet_name="Expenses")

    salary = salary_df["Amount"].sum()
    expenses = expense_df["Amount"].sum()

    balance = salary - expenses

    return f"Remaining balance is rupees {balance:,.2f}"

@tool
def expense_by_category(category: str) -> str:
    """
    Returns total expense for a given category.
    """

    df = pd.read_excel(EXCEL_FILE, sheet_name="Expenses")

    filtered = df[
        df["Category"].str.lower() == category.lower()
    ]

    total = filtered["Amount"].sum()

    return f"Total spent on {category} is rupees {total:,.2f}"

@tool
def largest_expense() -> str:
    """
    Returns the highest expense transaction.
    """

    df = pd.read_excel(EXCEL_FILE, sheet_name="Expenses")

    row = df.loc[df["Amount"].idxmax()]

    return (
        f"Largest expense was "
        f"{row['Description']} "
        f"for rupees {row['Amount']:,.2f}"
    )

@tool
def total_transactions() -> str:
    """
    Returns the total number of expense transactions.
    """

    df = pd.read_excel(EXCEL_FILE, sheet_name="Expenses")

    return f"You have {len(df)} expense transactions."
