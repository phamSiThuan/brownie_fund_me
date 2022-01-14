from brownie import network,accounts,MockV3Aggregator,config
import os
from web3 import Web3
DECIMALS = 18
VALUES = Web3.toWei(2000,'ether')
# VALUES = 2*(10**18)
# VALUES = 200000000
FORK_LOCAL_ENVIRONMENT = ["mainnet-fork","mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['development','ganache-local1','ganache-local2','ganache-local3']
def get_account():
    print("current active network: ",network.show_active())
    if(network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORK_LOCAL_ENVIRONMENT):
        print("account run local block chain: ",accounts[0])
        return accounts[0]
    else:
        # return accounts.add(os.getenv("PRIVAVTE_KEY"))
        print('my account :',os.getenv("PRIVATE_KEY"))
        # return accounts.add('4d14e7236a565033f6c7f71ec9154ee276f494d1beb7a0c6a3c1f23f8bd8e126')
        return accounts.add(config['wallets']['from_key'])
        # return accounts.add(config["wallets"]["from_key"])
#make code better
def deploy_mocks(account):
    print(f"the active network is {network.show_active()}")    
    print(f"deploying mock...")   
    #why ? because mockV3Aggregator is not an object, it's a list, so if it don't have anything,
    # that where you have to create
    # if(len(MockV3Aggregator)<=0):
    mock_aggregator =MockV3Aggregator.deploy(18,VALUES,{'from':account})
    print("mock deploy successfully")
    return MockV3Aggregator[-1].address