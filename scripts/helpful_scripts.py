from brownie import accounts, MockV3Aggregator, config, network, FundMe

from web3 import Web3

FORK_LOCAL_ENVIRONMENT = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development", "ganache-local"]
DECIMALS = 18
STARTING_PRICE = 3000


def get_accounts():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT
        or network.show_active() in FORK_LOCAL_ENVIRONMENT
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallet"]["from_key"])


def deploy_mocks():
    account = get_accounts()
    print("Active network is ::: ", network.show_active())
    print("Deploying Mocks....")

    # change to web3 covert if using live  Web3.toWei(STARTING_PRICE, "ether")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": account}
        )
    MockV3Aggregator[-1].address
    print("Mock Deployed! ")
