from datetime import datetime
from pony.orm import *

db = Database()

class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    tg_id = Required(int, unique=True)  # telegramm id
    nick = Optional(str)
    create_date = Required(datetime)
    wallet = Required('Wallet')
    sended_transactions = Set('Transaction', reverse='sender')
    receivered_transactions = Set('Transaction', reverse='receiver')


class Wallet(db.Entity):
    id = PrimaryKey(int, auto=True)
    balance = Required(float, default="0.0")
    private_key = Required(str, unique=True)
    address = Required(str, unique=True)
    user = Optional(User)
    sended_transactions = Set('Transaction', reverse='sender_wallet')
    received_transaction = Set('Transaction', reverse='receiver_wallet')


class Transaction(db.Entity):
    id = PrimaryKey(int, auto=True)
    sender = Optional(User, reverse='sended_transactions')
    receiver = Optional(User, reverse='receivered_transactions')
    sender_wallet = Optional(Wallet, reverse='sended_transactions')
    receiver_wallet = Optional(Wallet, reverse='received_transaction')
    receiver_address = Optional(str)
    sender_address = Optional(str)
    amount_btc_with_fee = Required(float)
    amount_btc_without_fee = Required(float)
    fee = Required(float)
    date_of_transaction = Required(datetime)
    tx_hash = Required(str)


