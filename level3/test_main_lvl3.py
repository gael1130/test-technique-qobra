from functions import *

with open("../level3/data/output.json", "r") as f:
    data = json.load(f)
commissions = data["commissions"]
deals = data["deals"]


# users' commissions
def test_user1_commission():
    assert commissions[0]["user_id"] == 1
    assert list(commissions[0]["commission"].keys()) == ['2018-05', '2018-06']
    assert list(commissions[0]["commission"].values()) == ["225.0", "185.0"]


def test_user2_commission():
    assert commissions[1]["user_id"] == 2
    assert list(commissions[1]["commission"].keys()) == ['2018-05', '2018-06', '2018-07']
    assert list(commissions[1]["commission"].values()) == ["112.5", "105.0", "45.0"]

# deals' commissions


def test_deal_commission1():
    assert deals[0]["id"] == 1
    assert deals[0]["commission"] == "25.0"


def test_deal_commission2():
    assert deals[1]["id"] == 2
    assert deals[1]["commission"] == "112.5"


def test_deal_commission3():
    assert deals[2]["id"] == 3
    assert deals[2]["commission"] == "95.0"


def test_deal_commission4():
    assert deals[3]["id"] == 4
    assert deals[3]["commission"] == "105.0"


def test_deal_commission5():
    assert deals[4]["id"] == 5
    assert deals[4]["commission"] == "105.0"


def test_deal_commission6():
    assert deals[5]["id"] == 6
    assert deals[5]["commission"] == "150.0"


def test_deal_commission7():
    assert deals[6]["id"] == 7
    assert deals[6]["commission"] == "45.0"


def test_deal_commission8():
    assert deals[7]["id"] == 8
    assert deals[7]["commission"] == "35.0"
