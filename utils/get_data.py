from schema import ClientData
from config import token_contracts


def get_client_data(data: ClientData) -> tuple:
    data = data.model_dump()

    private_key = data['private_key']
    token = data['token']
    amount = data['amount']
    proxy = data['proxy']

    token_contract = get_token_contract(token)

    return private_key, token_contract, amount, proxy


def get_token_contract(token):
    return token_contracts[token]
