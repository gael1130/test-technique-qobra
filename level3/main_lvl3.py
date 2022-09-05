from functions import *
from datetime import datetime

# Level 3
"""
New elements in deals: close_date & payment_date. Also associate deals with a commission.
Now it gets tricky, you need to focus and do some tests to validate your decision trees.
Hypothesis:
    Objectives are monthly, meaning it starts at 0 again the following month.
"""

users, deals = open_json("../level3/data/input.json")
users = adding_keys(users)

deals_list = []
for user in users:
    user["monthly_sales"] = {}
    user["commission"] = {}
    target = user["objective"]

    for deal in deals:
        # I create the deal_info variable which will hold the commission associated to the deal
        deal_info = {"id": deal["id"], "commission": 0}

        # If there is a match between the user and the deal
        if user["id"] == deal["user"]:

            # I need to have the correct format for time of closing and time of payment
            closing_date = datetime.strptime(deal["close_date"], "%Y-%m-%d")
            year_month_closing = closing_date.strftime("%Y-%m")

            payment_date = datetime.strptime(deal["payment_date"], "%Y-%m-%d")
            year_month_payment = payment_date.strftime("%Y-%m")

            # If it is a new closing period or not
            if year_month_closing not in user["monthly_sales"]:
                user["monthly_sales"][year_month_closing] = deal["amount"]
                # ex: user 1, first element = 500. target = 1000
                sales_amount = user["monthly_sales"][year_month_closing]

                # If it is a new payment period or not
                if year_month_payment not in user["commission"]:
                    the_deal_commission = deal_commission(previous_sales=0, current_deal_amount=deal["amount"],
                                                          target=user["objective"])

                    user["commission"][year_month_payment] = the_deal_commission

                    deal_info["commission"] = the_deal_commission
                    deals_list.append(deal_info)

                else:
                    the_deal_commission = deal_commission(previous_sales=0, current_deal_amount=deal["amount"],
                                                          target=user["objective"])

                    user["commission"][year_month_payment] += the_deal_commission
                    deal_info["commission"] = the_deal_commission
                    deals_list.append(deal_info)

            # the closing month exists => I add the amount
            else:
                # ex: amount = 500 + 1000
                user["monthly_sales"][year_month_closing] += deal["amount"]  # total = 500 + 800 = 1300

                # now I check the new amount in reference to the target
                sales_amount = user["monthly_sales"][year_month_closing]
                previous_sales = user["monthly_sales"][year_month_closing] - deal["amount"]
                the_deal_commission = deal_commission(previous_sales=previous_sales, current_deal_amount=deal["amount"],
                                                      target=user["objective"])

                deal_info["commission"] = the_deal_commission
                deals_list.append(deal_info)

                # now incorporate the payment timing
                if year_month_payment not in user["commission"]:
                    user["commission"][year_month_payment] = the_deal_commission
                else:
                    user["commission"][year_month_payment] += the_deal_commission

dictionary_to_save = {"commissions": [], "deals": []}
for user in users:
    dictionary_to_save["commissions"].append(
        {"user_id": user["id"],
         "commission": {str(k): str(v) for k, v in user["commission"].items()}
         }
    )

sorted_deals = sorted(deals_list, key=lambda d: d['id'])

for deal in sorted_deals:
    dictionary_to_save["deals"].append(
        {"id": deal["id"],
         "commission": str(deal["commission"])
         }
    )

save_to_json(destination="../level3/data/output.json", file=dictionary_to_save)
