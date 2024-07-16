from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}


def get_date(promt, allow_default=False):
    date_str = input(promt)
    if allow_default and date_str == "":
        return datetime.now().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Enter date in dd-mm-yyyy")
        return get_date(promt, allow_default)


def get_amount():
    try:
        amount = float(input("Enter amount: "))
        if amount < 0:
            raise ValueError("Amount cannot be 0 or less is")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()


def get_category():
    category = input("Enter category: 'I' for Income or 'E' for Expense: ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]

    print("Invalid category.")
    return get_category()


def get_description():
    return input("Enter a description (optional): ")
