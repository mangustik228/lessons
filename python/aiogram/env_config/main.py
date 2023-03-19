# var 1 
# import os
# import dotenv

# dotenv.load_dotenv()

# print(os.getenv('BOT_TOKEN'))
# print(os.getenv('ADMIN_ID'))

# var 2
# from environs import Env 

# env = Env()
# env.read_env()
# bot_token = env('BOT_TOKEN')
# admin_id = env.int('ADMIN_ID')

# print(bot_token)
# print(admin_id)
from configparser import ConfigParser
from dataclasses import dataclass

config = ConfigParser()
config.read('config.ini')
DEBUG = config.getboolean('DEFAULT', 'debug')
# MY_ID = config.getint('BOT', 'my_id')



@dataclass
class Config:
    bot: 'Bot'
    debug: bool = config.getboolean('DEFAULT', 'debug')
    db: 'Database' | 'DatabaseSQLITE'

@dataclass
class Database:
    port: int = 3306
    host: str = "1234"

@dataclass
class DatabaseSQLITE:
    path: str = 'this is path'


@dataclass
class Bot:
    token: str = 'This is my token'
    bla: str | None = None


config = Config(Bot())

print(config.db)
print(config)
print(config.debug)