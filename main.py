import requests
from loguru import logger
from web3.middleware import geth_poa_middleware
from web3 import HTTPProvider, Web3
from config import *
from utils.get_data import get_token_contract
from fake_useragent import UserAgent
from models import CRUD


def get_abi():
    with open('sushi_abi.json', 'r') as f:
        abi = f.read()
    return abi


def get_session(proxy_url):
    session = requests.Session()
    session.proxies = {
        'http': proxy_url,
        'https': proxy_url,
    }
    session.headers = {
        'User-Agent': UserAgent().random
    }
    return session


async def swap_weth_to_token(key, token, amount, proxy_url=None):
    # Connect to Ethereum node
    try:    
        token_contract = get_token_contract(token.lower())

        if proxy_url:
            session = get_session(proxy_url)
            w3 = Web3(HTTPProvider(endpoint_uri=RPC_ONE, session=session))
        else:
            w3 = Web3(HTTPProvider(RPC_ONE))

        w3.middleware_onion.inject(geth_poa_middleware, layer=0)

        # Set account
        account = w3.eth.account.from_key(private_key=PRIVATE_KEY).address 

        # Sushiswap Router address
        router_address = SUSHI_CONTRACT  # Mainnet
        router_abi = get_abi()  # Fill this with Sushiswap Router's ABI

        # Initialize contract
        router_contract = w3.eth.contract(address=router_address, abi=router_abi)

        # Token addresses
        token0_address = WETH_CONTRACT
        token1_address = token_contract

        # Amounts
        amount_in = w3.to_wei(amount, 'ether') 
        amount_out_min = 0  # We accept any amount of the other token

        path = [token0_address, token1_address]
        

        # Deadline
        deadline = w3.eth.get_block('latest')['timestamp'] + 300  # 5 minutes from the latest block

        # Build transaction
        transaction = router_contract.functions.swapExactTokensForETH(
            amount_in,
            amount_out_min,
            path,
            account,
            deadline
        ).build_transaction({
            'from': account,
            'gas': 21000,
            'gasPrice': w3.to_wei('50', 'gwei'),
            'nonce': w3.eth.get_transaction_count(account),
        })

        # Sign transaction
        signed_txn = w3.eth.account.sign_transaction(transaction, PRIVATE_KEY)

        # Send transaction
        txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

        print(f'Transaction sent with hash: {txn_hash.hex()}')
    
    except Exception as e:
        logger.info('------------------------------------------------------ERROR')
        crud = CRUD()
        await crud.create_status(key, token, amount, str(e), proxy_url)
        raise e



# asyncio.run(swap_weth_to_token('234ca219d0620d274c3d15a3004461a28a5be58dfea01a8a3ce58ac1089247e5', 'USDT', 20, 'http://dkhalidovstt:VBNsY2BRZW@103.80.87.117:59100'))


# if __name__ == '__main__':

#     app = FastAPI()

#     @app.post("/")
#     async def root(request_data: ClientData):    
#         private_key, token_contract, amount, proxy = get_client_data(request_data)

#         await swap_weth_to_token(private_key, token_contract, amount, proxy)
#         return private_key, token_contract, amount, proxy

    # uvicorn.run(app, host="0.0.0.0", port=8000)
