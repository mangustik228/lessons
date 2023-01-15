from .models import User, Wallet, Transaction, db
from pony.orm import *

db_path = '/home/bacek/lessons/python/fast_api/examples/btc_folder/database/db.sqlite'

db.bind(provider='sqlite',filename=db_path, create_db=True)
db.generate_mapping(create_tables=True)