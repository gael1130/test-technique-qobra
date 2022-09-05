"""
      "user_id": 1,
      "commission": {
        "2018-05": "240.0",
        "2018-06": "200.0"
"""

"""
      "user_id": 2,
      "commission": {
        "2018-05": "112.5",
        "2018-06": "130.0",
        "2018-07": "45.0"
"""

"""
Example
You have 4 deals (in the chronological order), worth respectively 500, 300, 700 and 200.
The objective of your salesman is 1000
1st deal => Commission: 5% * 500 = 25
2nd deal => Commission: 10% * 300 = 30

3rd deal => Commission: 10% * 200 + 15% * 500 = 95

4th deal => Commission: 15% * 200 = 30
"""

# (1) Test the payment commission flow with 7 exemples

# (1) closing and payment same month
    # (1.1) target = 500 | sale1 = 200 | sale2 = 200
    # (1.2) target = 500 | sale1 = 400 | sale2 = 300
# (2) closing and payment different month


"""
    {"id": 1, "name": "Nicolas", "objective": 1000},
    {"id": 2, "name": "Math", "objective": 500}
  ],
  "deals": [
    {"id": 1, "amount": 500, "user": 1, "close_date": "2018-05-01", "payment_date": "2018-05-20" }, => Nicolas
    {"id": 2, "amount": 1000, "user": 2, "close_date": "2018-05-15", "payment_date": "2018-05-25" }, => Math
    {"id": 3, "amount": 800, "user": 1, "close_date": "2018-05-15", "payment_date": "2018-05-26" }, => Nicolas
    {"id": 4, "amount": 700, "user": 2, "close_date": "2018-05-25", "payment_date": "2018-06-02" }, => Math
    {"id": 5, "amount": 700, "user": 1, "close_date": "2018-05-26", "payment_date": "2018-05-30" }, => Nicolas
    {"id": 6, "amount": 1000, "user": 1, "close_date": "2018-05-30", "payment_date": "2018-06-13" }, => Nicolas
    {"id": 7, "amount": 550, "user": 2, "close_date": "2018-06-02", "payment_date": "2018-07-06" }, => Math
    {"id": 8, "amount": 600, "user": 1, "close_date": "2018-06-15", "payment_date": "2018-06-18" } => Nicolas

Nicolas target 1000 | Math target 500
deal 1 (500), commission = 0.05 * 500 = 25 (Nicolas, closing 5)
Nicolas total 500 | Math total 0
deal 2 (1000), commission = 0.05 * 250 +  0.1 * 250 + 0.15 * 500 = 112.5 (Math, closing 5)
Nicolas total 500 | Math total 1000
deal 3 (800), commission = 0.1 * 500 +  0.15 * 300 =  95.0 (Nicolas, closing 5)
Nicolas total 1300 | Math total 1000
deal 4 (700), commission = 0.15 * 700 = 105 (Math, closing 5)
Nicolas total 1300 | Math total 1700
deal 5 (700), commission = 0.15 * 700 = 105 (Nicolas, closing 5)
Nicolas total 2000 | Math total 1700
deal 6 (1000), commission = 0.15 * 1000 = 150 (Nicolas, closing 5)
Nicolas total 3000 | Math total 1700
deal 7 (550), commission = 0.05 * 250 +  0.1 * 250 + 0.15 * 50 = 45 (Math, closing 6)
Nicolas total 0 | Math total 550
deal 8 (600), commission = 0.05 * 500 +  0.1 * 100 = 35 (Nicolas, closing 6)
Nicolas total 600 | Math total 550
"""
print(0.15 * 700)

import json
from functions import *

with open("../level3/data/output.json", "r") as f:
    data = json.load(f)
commissions = data["commissions"]
deals = data["deals"]



# print(json.dumps(commissions, indent=2))
# print(json.dumps(deals, indent=2))
#
# for deal in deals:
#     print(deal["id"], deal["commission"])

print(list(commissions[0]["commission"].keys()))
print(type(commissions[0]["commission"].keys()))

