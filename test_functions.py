from functions import *


def test_calculate_commission_from_sales():
    # 2 or less deals, no bonus
    assert calculate_commission_from_sales({"num_sales": 0, "total_sales": 0}) == {'commission': '0.0', 'num_sales': 0, 'total_sales': 0}
    assert calculate_commission_from_sales({"num_sales": 1, "total_sales": 1000}) == {'commission': '100.0', 'num_sales': 1, 'total_sales': 1000}
    # 2 or less deals, bonus
    assert calculate_commission_from_sales({"num_sales": 2, "total_sales": 2000}) == {'commission': '700.0', 'num_sales': 2, 'total_sales': 2000}
    # 3 or more deals, no bonus
    assert calculate_commission_from_sales({"num_sales": 3, "total_sales": 1500}) == {'commission': '300.0', 'num_sales': 3, 'total_sales': 1500}
    # 3 or more deals, bonus
    assert calculate_commission_from_sales({"num_sales": 4, "total_sales": 2000}) == {'commission': '900.0', 'num_sales': 4, 'total_sales': 2000}


"""
Your objective is to calculate the compensation of each user, knowing that they are commissioned as such:
- 10% of what they sell if they sold 1 or 2 deals during the month
- 20% of what they sold if they sold 3 deals or more
- 500 euros bonus if they sold more than 2000 euros in the month

"""
"""
# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
"""