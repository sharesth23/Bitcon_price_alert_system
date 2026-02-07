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
    
