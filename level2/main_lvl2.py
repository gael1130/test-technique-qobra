import json
from functions import *
""" The difference here is the different brackets from the the amount of sales vs Objective, not the number of sales
## Commissioning

Your objective is to calculate the compensation of each user, knowing that they are commissioned as such:
- 5% of what they sell between 0% and 50% of their objective
- 10% of what they sell between 50% and 100% of their objective
- 15% of what they sell above their objective

## Example
Math's objective is 1000 euros and he sold a single deal worth 2000 euros.
He will be commissioned:
+ 5% * 500 => (between 0% and 50% of his objective)
+ 10% * 500 => (between 50% and 100% of his objective)
+ 15% * 1000 => (above his objective)

This means he will be commissioned 25 + 50 + 150 = 225 euros


# ex1: target = 1000 et vendu 500
#     commission = 0.05 * 500
#
# ex2: target = 1000 et vendu 800
#     bracket_1 = 0.05 * 500 = 25
#     bracket_2 = 0.1 * (sales - (target/2)) = 0.1 * (800 - 500) = 0.1 * 300 = 30
#
# ex3: target = 1000 et vendu 1200
#     bracket_1 = 0.05 * 500 = 25
#     bracket_2 = 0.1 * (sales - (target/2)) = 0.1 * (1200 - 500) = 0.1 * 700 = 70
#     bracket_3 = 0.15 * (sales - target) = 0.15 * (1200 - 1000) = 0.15 * 200 = 30
"""

users, deals = open_json("../level2/data/input.json")
users = adding_keys(users)

for user in users:
    for deal in deals:
        calculate_user_sales_from_deals(user, deal)

    if user["total_sales"] <= 0.5 * user["objective"]:
        user["commission"] = \
            commission_from_objective(num_brackets=1, sales_amount=user["total_sales"], objective=user["objective"])
    elif user["total_sales"] <= user["objective"]:
        user["commission"] = \
            commission_from_objective(num_brackets=2, sales_amount=user["total_sales"], objective=user["objective"])
    else:
        user["commission"] = \
            commission_from_objective(num_brackets=3, sales_amount=user["total_sales"], objective=user["objective"])


dictionary_to_save = {"commissions": []}
for user in users:
    dictionary_to_save["commissions"].append({"user_id": user["id"], "commission": str(user["commission"])})

print("********* ↓ dictionary to save ↓ *********")
print(dictionary_to_save)

save_to_json(destination="../level2/data/output.json", file=dictionary_to_save)
