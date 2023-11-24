from pydantic import BaseModel

class ClientData(BaseModel):
    private_key: str
    token: str 
    amount: float
    proxy: str
