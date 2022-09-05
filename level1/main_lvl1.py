from functions import *

"""
When I read everything and looked a the examples I thought: this is a ladder of decision trees.
Each level built on top of each other like with more decision trees inside like russian dolls.
Your code expands and build on top of each other, so make small functions for better readability.

Observations: 
    It is stated that each user has a name, an objective and an id but I do not see any objective. Only name and id.
    Also commission apparently has to be a string, I do not understand why
**** **** **** 

(1) Restate the problem
calculate the commission for each user depending on how much they sold
save the result to a json

(2) Pseudo Code
read the data from input
iterate over the data (dictionary) to calculate how many sales (length)
associate each sale to a user
do the total
calculate each compensation following the rule: 10% of total if number of deals <= 2. (length of deals)
20% of total if length of deals >= 3
bonus of 500€ if their total of sales >=  2000

(3) Code
"""
# 1. I want the information from the input file
users, deals = open_json("../level1/data/input.json")

# 2. I want to calculate the commission
users = adding_keys(users)
for user in users:
    for deal in deals:
        calculate_user_sales_from_deals(user, deal)
    calculate_commission_from_sales(user)

dictionary_to_save = {"commissions": []}
for user in users:
    dictionary_to_save["commissions"].append({"user_id": user["id"], "commission": str(user["commission"])})

print("********* ↓ dictionary to save ↓ *********")
print(dictionary_to_save)

save_to_json(destination="../level1/data/output.json", file=dictionary_to_save)
