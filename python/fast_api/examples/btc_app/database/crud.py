import pydantic_models as pyd
import bit
import config
from datetime import datetime
from database.db import *
from pony.orm import * 



@db_session # pony.orm - автоматом коммитит и что то другое
def create_wallet(user: pyd.User=None, private_key: str = None, testnet:bool = True):
    '''
    Функция создания кошелька.
    '''
    # Проверка на тестовость
    if testnet: 
        raw_wallet = bit.PrivateKeyTestnet(private_key)
    else:
        raw_wallet = bit.Key(private_key)
        
    if user:
        wallet = Wallet(user=user, private_key=raw_wallet.to_wif(), adress=raw_wallet.address)
    else:
        wallet = Wallet(private_key=raw_wallet.to_wif(), address=raw_wallet.address)
    flush() # Сохраняет изменения в бд
    return wallet


@db_session 
def create_user(tg_id: int, nick: str= None) -> User:
    '''
    Функция созданию юзера(сразу создает ему кошелек)
    '''
    if nick:
        user = User(tg_id=tg_id,
                     nick=nick,
                     create_date=datetime.now(),
                     wallet=create_wallet())
    else:
        user = User(tg_id=tg_id,
                     create_date=datetime.now(),
                     wallet=create_wallet())
    flush()
    return user


@db_session
def create_transaction(
    sender: User,
    amount_btc_without_fee: float,
    receiver_address: str,
    fee: float = None,
    testnet: bool = True 
):
    """
    :param amount_btc_without_fee:  количество биткоинов исключая комиссию, значение в сатоши
    :param receiver_address: адрес получателя, строка с адресом
    :param amount_btc_with_fee: количество биткоинов включая комиссию, значение в сатоши
    :param fee: абсолютная комиссия, исчисляем в сатоши - необязательно.
    :param testnet: в тестовой сети ли мы работаем
    :return: Transaction object
    """
    print('hello')
    if testnet: 
        wallet_of_sender = bit.PrivateKeyTestnet(sender.wallet.private_key)
    else:
        wallet_of_sender = bit.Key(sender.wallet.private_key)

    print('check balance')
    sender.wallet.balance = wallet_of_sender.get_balance()
    print('balance coming')

    if not fee:
        # Стоимость транзакции
        fee = bit.network.fees.get_fee() * 1000 
        
    amount_btc_with_fee = amount_btc_without_fee + fee

    if amount_btc_with_fee > sender.wallet.balance:
        return f"Too low balance: {sender.wallet.balance}"

    print('посчитали коммиссию')
    output = [(receiver_address, amount_btc_without_fee, 'satoshi')]
    print('prepare tuple')


    tx_hash = wallet_of_sender.send(output, fee, absolute_fee=True)

    transaction = Transaction(
        sender=sender,
        sender_wallet=sender.wallet,
        sender_address=sender.wallet.address,
        receiver_address=receiver_address,
        amount_btc_with_fee=amount_btc_with_fee,
        amount_btc_without_fee=amount_btc_without_fee,
        date_of_transaction=datetime.now(),
        tx_hash=tx_hash
    )
    return transaction


@db_session
def update_wallet_balance(wallet: pyd.Wallet):
    testnet = True if wallet.private_key.startswith('c') else False
    if testnet:
        bit_wallet = bit.PrivateKeyTestnet(wallet.private_key)
    else:
        bit_wallet = bit.Key(wallet.private_key)
    wallet.balance = bit_wallet.get_balance()
    return wallet 

@db_session 
def update_all_wallets():
    for wallet in select(w for w in Wallet)[:]:
        update_wallet_balance(wallet)
        print(wallet.address, wallet.balance)
    return True

@db_session 
def get_user_by_id(id:int) -> User:
    return User[id]


@db_session
def get_user_by_tg_id(tg_id: int):
    return User.select(lambda u: u.tg_id == tg_id).first()

@db_session
def get_transaction_info(t: pyd.Transaction):
    return {"id": t.id,
            "sender": t.sender if t.sender else None,
            "receiver": t.receiver if t.receiver else None,
            "sender_wallet": t.sender_wallet if t.sender_wallet else None,
            "receiver_wallet": t.receiver_wallet if t.receiver_wallet else None,
            "sender_address": t.sender_address,
            "receiver_address": t.receiver_address,
            "amount_btc_with_fee": t.amount_btc_with_fee,
            "amount_btc_without_fee": t.amount_btc_without_fee,
            "fee": t.fee,
            "date_of_t": t.date_of_transaction,
            "tx_hash": t.tx_hash}

@db_session
def get_wallet_info(w: pyd.Wallet):
    w = update_wallet_balance(w)
    return {"id": w.id if w.id else None,
            "user": w.user if w.user else None,
            "balance": w.balance if w.balance else None,
            "private_key": w.private_key if w.private_key else None,
            "address": w.address if w.address else None,
            "sended_transactions": w.sended_transactions if w.sended_transactions else [],
            "received_transactions": w.received_transaction if w.received_transaction else []}


@db_session
def get_user_info(u:pyd.User):
    return {"id": u.id,
            "tg_id": u.tg_id if u.tg_id else None,
            "nick": u.nick if u.nick else None,
            "create_date": u.create_date,
            # получаем все данные по кошельку
            "wallet": get_wallet_info(u.wallet),
            "sended_transactions": u.sended_transactions if u.sended_transactions else [],
            "received_transactions": u.receivered_transactions if u.receivered_transactions else []}

@db_session
def update_user(user: pyd.User_to_update):
    user_to_update = User[user.id]
    if user.tg_id:
        user_to_update.tg_id = user.tg_id
    if user.nick:
        user_to_update.nick = user.nick
    if user.create_date:
        user_to_update.create_date = user.create_date
    if user.wallet:
        user_to_update.wallet = user.wallet
    return user_to_update