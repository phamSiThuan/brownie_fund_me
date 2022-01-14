from scripts.fund_and_withdraw import fund
from scripts.helpful_scripts import get_account,LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me
from brownie import network,accounts,exceptions
import pytest
def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    #new Method -- 'x`()
    entrance_fee = 1000000000000000000
    print("ether value to usd: ",fund_me.getConvertRate(fund_me.getPrice()))
    print("my money convert: ",fund_me.getConvertRate(entrance_fee))
    print("[] entrance fee",entrance_fee)
    tx = fund_me.fund({"from":account,"value":entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address)==entrance_fee
    tx2 = fund_me.withdraw({'from':account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address)==0
def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for testing please!")
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    #tell test that i want this error when running this fund_me... line.
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({'from':bad_actor})