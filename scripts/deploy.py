from brownie import FundMe,accounts,network,MockV3Aggregator,config
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS
)


def deploy_fund_me():
    account = get_account()
    print("account to transact: ",account)
    # fundMe_contract = FundMe.deploy({'from':account})
    # run only rinkeby 
    #other, deploy mocks.
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        # price_feed_address='0x8A753747A1Fa494EC906cE90E9f37563A8AF630e'
        price_feed_address=config['networks'][network.show_active()]['eth_usd_price_feed']
    else:
        deploy_mocks(account)
        print("this is the mock address: ",MockV3Aggregator[-1].address)
        price_feed_address = MockV3Aggregator[-1].address
    print("what is price feed address:",price_feed_address)
    # if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
    #     fundMe_contract = FundMe.deploy(price_feed_address,{'from':account},publish_source=True)
    # else:
    #     fundMe_contract = FundMe.deploy(price_feed_address,{'from':account},publish_source=False)
    print("is veriry?",config['networks'][network.show_active()].get("verify"))
    fundMe_contract = FundMe.deploy(price_feed_address,{'from':account},publish_source=config['networks'][network.show_active()].get("verify"))
    print("get fund me contract: ",FundMe[-1])
    print("fundMe deploy contract with address: ",fundMe_contract.address)
    return fundMe_contract
def main():
    deploy_fund_me()