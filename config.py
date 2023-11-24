from sqlalchemy import create_engine


proxy_url = "http://212.220.13.98:4153"

TOKEN = '6761149221:AAGCsTGS8ApaeFwIBjXV-dzFIAMSusFGEgs'

# RPC 
RPC_ONE = 'https://1rpc.io/linea'
RPC_TWO = 'https://linea.drpc.org'
RPC_THREE = 'https://linea.blockpi.network/v1/rpc/public'

# Account information
ADDRESS = 0xFbA9D2bd53D3D542bBccB03522e9406E51d4cc08
PRIVATE_KEY = '234ca219d0620d274c3d15a3004461a28a5be58dfea01a8a3ce58ac1089247e5'

# Sushiswap Router address
SUSHI_CONTRACT  =     '0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F'

# Token addresses
WETH_CONTRACT   =     '0xe5D7C2a44FfDDf6b295A15c148167daaAf5Cf34f' # ETH
DAI_CONTRACT    =     '0x4AF15ec2A0BD43Db75dd04E62FAA3B8EF36b00d5'
USDC_CONTRACT   =     '0x176211869cA2b568f2A7D4EE941E073a821EE1ff'
USDT_CONTRACT   =     '0xA219439258ca9da29E9Cc4cE5596924745e12B93'
WBTC_CONTRACT   =     '0x3aAB2285ddcDdaD8edf438C1bAB47e1a9D05a9b4'
LDO_CONTRACT    =     '0x0e076AAFd86a71dCEAC65508DAF975425c9D0cB6'
HAPI_CONCTRACT  =     '0x0e5F2ee8C29e7eBc14e45dA7FF90566d8c407dB7'
PEPE_CONTRACT   =     '0x7da14988E4f390C2E34ed41DF1814467D3aDe0c3'
KNC_CONTRACT    =     '0x3b2F62d42DB19B30588648bf1c184865D4C3B1D6'
LINK_CONTRACT   =     '0x5B16228B94b68C7cE33AF2ACc5663eBdE4dCFA2d'

token_contracts = {
    'weth': WETH_CONTRACT,
    'dai': DAI_CONTRACT,
    'usdc': USDC_CONTRACT,
    'usdt': USDT_CONTRACT,
    'wbtc': WBTC_CONTRACT,
    'ldo': LDO_CONTRACT,
    'hapi': HAPI_CONCTRACT,
    'pepe': PEPE_CONTRACT,
    'knc': KNC_CONTRACT,
    'link': LINK_CONTRACT
}

login, password = "postgres", "master"
engine = create_engine(url=f"postgresql://{login}:{password}@localhost:5432/linea_base", echo=True)
