import requests 
import json 
import time 
from datetime import datetime , timedelta
from typing import Dict, Lists , Tuple , Optional
import sqlite3
import hashlib
import os 
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
from matplotlib.pyplot import FuncAnimation 

try:
    from plyer import notification 
    NOTIFICATIONS_AVAILABLE = True
except ImportError:
    NOTIFICATIONS_AVAILABLE = False

import threading

class BitcoinTracker:
    def __init__(self , db_path:  str = "bitcoin_tracker.db"):
        self.db_path = db_path 
        self.apis = {
            'coindesk': 'https://api.coindesk.com/v1/bpi/currentprice.json',
            'coinbase': 'https://api.coinbase.com/v2/prices/BTC-{currency}/spot',
            'blockchain': 'https://blockchain.info/ticker',
            'coingecko': 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies={currency}'

        }

        self.supported_currencies = ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY', 'HKD', 'NZD', 'INR']
        self.current_currency = 'USD'
        self.currency_symbols = {
            'USD': '$', 'EUR': '€', 'GBP': '£', 'JPY': '¥',
            'AUD': 'A$', 'CAD': 'C$', 'CHF': 'Fr', 'CNY': '¥', 'INR': '₹'
        }
        