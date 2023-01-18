from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
    tg_id: int
    nick: str = None
    create_date: datetime
    wallet: 'Wallet'
    sended_transactions: list['Transaction'] = None
    receivered_transactions: list['Transaction'] = None


class Wallet(BaseModel):
    id: int
    balance: float = 0.0
    private_key: str
    address: str
    user: 'User'
    sended_transactions: list['Transaction'] = []
    received_transaction: list['Transaction'] = []


class Transaction(BaseModel):
    id: int
    sender: User
    receiver: User
    sender_wallet: Wallet = None
    receiver_wallet: Wallet = None
    receiver_address: str
    sender_address: str
    amount_btc_with_fee: float
    amount_btc_without_fee: float
    fee: float
    date_of_transaction: datetime
    tx_hash: str

class User_to_update(BaseModel):
    id:int 
    tg_id: int = None 
    nick: str = None 
    create_date: datetime = None 
    wallet: "Wallet" = None 

class User_to_create(BaseModel):
    tg_id: int = None 
    nick: str = None 

