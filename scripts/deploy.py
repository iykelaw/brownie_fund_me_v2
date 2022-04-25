from brownie import accounts, FundMe, MockV3Aggregator, network, config, web3
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENT,
    deploy_mocks,
    get_accounts,
)


def deploy_fund_me():
    account = get_accounts()
    print("Deploying contract at #: ", account)
    #  add account var to fund me
    # we need to check what network we are on so we can pass the right address
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print("Contract deployed !", fund_me.address)
    return fund_me


def main():
    deploy_fund_me()
