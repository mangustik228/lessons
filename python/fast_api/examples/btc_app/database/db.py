from .models import User, Wallet, Transaction, db
from pony.orm import *



db_path = '/home/bacek/lessons/python/fast_api/examples/btc_folder/database/db.sqlite'
db.bind(provider='sqlite', filename='db.sqlite', create_db=False)
db.generate_mapping(create_tables=True)