import json


def open_json(file):
    """
    Open a json file and return the users and deals
    :param file:
    :return: two lists of dictionaries
    """
    with open(file, "r") as f:
        data = json.load(f)
    users = data["users"]
    deals = data["deals"]
    return users, deals


def save_to_json(destination, file):
    """
    Save the users commissions to a json file
    :param file:
    :return:
    """
    with open(destination, "w") as f:
        json.dump(file, f, indent=2)


def adding_keys(users):
    """
    Adding the keys necessary to calculate the commission to the users dictionary
    :param users: users list from the input data
    :return: users list with new keys (num_sales, total_sales and commission)
    """
    for el in users:
        el["num_sales"] = 0
        el["total_sales"] = 0
        el["commission"] = 0
    return users


def calculate_user_sales_from_deals(user, deal):
    """
    Calculates the number of sales and the total sales for each user
    :param user: dictionary of a user's information
    :param deal: dictionary of a deal's information
    :return: dictionary of user's information updated with his number of sales and total sales amount
    """
    if user["id"] == deal["user"]:
        user["num_sales"] += 1
        user["total_sales"] += deal["amount"]
    return user


def calculate_commission_from_sales(user):
    """
    Calculates the commission for each user
    :param user: dictionary of a user's information
    :return: dictionary of a user's information updated with his sales' commission
    """
    if user["num_sales"] <= 2:
        user["commission"] = str(user["total_sales"] * 0.1)
    elif user["num_sales"] >= 3:
        user["commission"] = str(user["total_sales"] * 0.2)
    if user["total_sales"] >= 2000:
        user["commission"] = str(float(user["commission"]) + 500)
    return user


# level 2
def commission_from_objective(num_brackets, sales_amount, objective):
    """
    Calculates the commission for a deal based on the number of brackets, the sales amount and the objective
    :param num_brackets: the number of commission brackets (depending if the sales amount is above or below the objective)
    :param sales_amount:
    :param objective:  the sales objective of the user
    :return: the commission for the deal (as a float)
    """
    bracket1 = 0.5 * objective
    if num_brackets == 1:
        return 0.05 * sales_amount
    elif num_brackets == 2:
        return (0.05 * bracket1) + (0.1 * (sales_amount - bracket1))
    elif num_brackets == 3:
        return 0.15 * bracket1 + (0.15 * (sales_amount - objective))


# level 3
def deal_commission(previous_sales, current_deal_amount, target):
    """
    Calculates the commission for a deal based on the previous cumulated sales amount, the current deal amount and the objective (target)
    :param previous_sales: the cumulated sales amount of the user
    :param current_deal_amount: the amount of the current deal
    :param target: the sales objective of the user
    :return: the commission associated to the deal (as a float)
    """
    bracket1 = 0.5 * target
    total_sales_amount = previous_sales + current_deal_amount

    if total_sales_amount <= 0.5 * target:
        deal_commission = 0.05 * current_deal_amount
    elif total_sales_amount <= target:
        # 2 cases : (1) previous sales > 0.5 * target (2) previous sales < 0.5 * target
        if previous_sales <= bracket1:  # ex: target 1'000, previous sales 400, current deal 300
            first_amount = bracket1 - previous_sales  # (1'000 / 2) - 400 = 100
            second_amount = total_sales_amount - bracket1  # (400 + 300) - 500 = 200
            deal_commission = first_amount * 0.05 + second_amount * 0.1

        else:  # ex: target 1'000, previous sales 600, current deal 200
            deal_commission = current_deal_amount * 0.1

    else:  # total_sales_amount > target
        # 2 cases: (1) previous sales <= 0.5 * target (2) previous sales > 0.5 * target

        if previous_sales <= bracket1:  # ex: target 1'000, previous sales 400, current deal 700
            last_amount = total_sales_amount - target  # (400 + 700) - 1000 = 100
            second_amount = bracket1
            lower_amount = bracket1 - previous_sales  # (1'000 / 2) - 400 = 100
            deal_commission = lower_amount * 0.05 + second_amount * 0.1 + last_amount * 0.15

        elif bracket1 < previous_sales <= target:  # ex: target 1'000, previous sales 600, current deal 500
            first_amount = previous_sales - bracket1  # 600 - 500 = 100
            last_amount = total_sales_amount - target  # (600 + 500) - 1'000 = 100
            lower_amount = current_deal_amount - last_amount  # 500 - 100 = 400
            deal_commission = 0.15 * last_amount + 0.1 * lower_amount
        else:
            deal_commission = 0.15 * current_deal_amount

    return deal_commission
