from brownie import FundMe
from scripts.helpful_scripts import  get_account
def fund():
    print("test FundMe[0]",FundMe[-1])
    fund_me = FundMe[-1]
    print("fund_me has some thing? ",fund_me)
    print('test owner, ',fund_me.owner())
    print("price_feed()= ",fund_me.priceFeed())
    account = get_account()
    version = fund_me.getVersion()
    print("version ",version)
    entrance_fee = fund_me.getPrice()
    print("price: ",entrance_fee)
    
def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print(fund_me.withdraw({'from':account}))

def main():
    fund()
    withdraw()

