DB_PATH = "bitcoin_tracker.db"

APIS = {
    "coindesk": "https://api.coindesk.com/v1/bpi/currentprice.json",
    "coinbase": "https://api.coinbase.com/v2/prices/BTC-USD/spot",
    "blockchain": "https://blockchain.info/ticker",
}
ALERT_THRESHOLD = {
        "minor" : 2.0,
        "major" : 5.0,
        "critical" : 10.0
}

DEFAULT_INTERVAL_SECONDS  = 60 
CURRECY_SYMBOLS = {
     "USD": "$",
    "EUR": "€",
    "INR": "₹",
    "GBP": "£",
    "JPY": "¥",
}
