from brownie import FundMe

from scripts.helpful_scripts import get_accounts


def fund():
    fund_me = FundMe[-1]
    account = get_accounts()
    entrance_fee = fund_me.getEntranceFee()

    print(entrance_fee)

    print("Funding account :::", entrance_fee)
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_accounts()
    print("Withdrawing from ::: ", account)
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
