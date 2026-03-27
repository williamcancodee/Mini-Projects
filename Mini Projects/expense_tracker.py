def add_expense(expenses, amount, category, note=""):
    """
    Adds a single expense entry to the expenses list.

    Args:
        expenses (list): A list that stores expense dictionaries.
        amount (int or float): Expense amount, must be greater than 0.
        category (str): Expense category (e.g., food, transport).
        note (str): Optional note for the expense.

    Returns:
        str: Success or error message.
    """

    if not isinstance(expenses, list):
        return "Expenses must be a list."
    if not isinstance(amount, (int, float)) or amount <= 0:
        return "Amount must be a number greater than 0."
    if not isinstance(category, str) or not category.strip():
        return "Category must be a non-empty string."
    if not isinstance(note, str):
        return "Note must be a string."

    expense = {
        "amount": round(float(amount), 2),
        "category": category.strip().lower(),
        "note": note.strip()
    }
    expenses.append(expense)
    return f"Expense added: {expense['category']} - {expense['amount']:.2f}"


def total_spent(expenses):
    """
    Calculates the total amount spent.

    Args:
        expenses (list): List of expense dictionaries.

    Returns:
        float or str: Total spent rounded to 2 decimals, or an error message.
    """

    if not isinstance(expenses, list):
        return "Expenses must be a list."

    total = 0
    for item in expenses:
        if not isinstance(item, dict) or "amount" not in item:
            return "Each expense must be a dictionary with an 'amount' key."
        if not isinstance(item["amount"], (int, float)):
            return "Expense amount values must be numeric."
        total += item["amount"]

    return round(total, 2)


def category_breakdown(expenses):
    """
    Summarizes spending by category.

    Args:
        expenses (list): List of expense dictionaries.

    Returns:
        dict or str: Mapping of category to total spent, or an error message.
    """

    if not isinstance(expenses, list):
        return "Expenses must be a list."

    summary = {}
    for item in expenses:
        if not isinstance(item, dict):
            return "Each expense must be a dictionary."
        category = item.get("category")
        amount = item.get("amount")

        if not isinstance(category, str) or not category.strip():
            return "Each expense must include a valid 'category'."
        if not isinstance(amount, (int, float)):
            return "Each expense must include a numeric 'amount'."

        key = category.strip().lower()
        summary[key] = round(summary.get(key, 0) + amount, 2)

    return summary


def budget_status(expenses, budget):
    """
    Compares spending against a monthly budget.

    Args:
        expenses (list): List of expense dictionaries.
        budget (int or float): Monthly budget amount.

    Returns:
        dict or str: Budget report with total, remaining, and percentage used.
    """

    if not isinstance(budget, (int, float)) or budget <= 0:
        return "Budget must be a number greater than 0."

    spent = total_spent(expenses)
    if isinstance(spent, str):
        return spent

    remaining = round(budget - spent, 2)
    used_percent = round((spent / budget) * 100, 2)

    return {
        "budget": round(float(budget), 2),
        "spent": spent,
        "remaining": remaining,
        "used_percent": used_percent,
        "status": "over budget" if spent > budget else "within budget"
    }


if __name__ == "__main__":
    monthly_expenses = []

    print(add_expense(monthly_expenses, 12.5, "Food", "Lunch"))
    print(add_expense(monthly_expenses, 45, "Transport", "Fuel"))
    print(add_expense(monthly_expenses, 22.75, "Food", "Groceries"))

    print("Total spent:", total_spent(monthly_expenses))
    print("Category breakdown:", category_breakdown(monthly_expenses))
    print("Budget status:", budget_status(monthly_expenses, 200))
