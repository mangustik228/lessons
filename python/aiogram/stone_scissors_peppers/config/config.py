from dotenv import load_dotenv
import os 
from dataclasses import dataclass

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')

    
@dataclass
class Bot:
    token: str 

@dataclass
class Config:
    bot : "Bot"

config = Config(Bot(os.getenv('BOT_TOKEN')))


