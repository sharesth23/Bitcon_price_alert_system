# Bitcoin Price Tracker - Complete File Tree

```
bitcoin-price-tracker/
│
├── 📄 main.py                              # Application entry point
├── 📄 requirements.txt                     # Python dependencies
├── 📄 README.md                            # Main documentation
├── 📄 SETUP_AND_USAGE.md                   # Setup guide
├── 📄 PROJECT_OVERVIEW.md                  # Project summary
│
└── 📁 bitcoin_tracker/                     # Main package
    │
    ├── 📄 __init__.py                      # Package initialization
    ├── 📄 config.py                        # Central configuration
    ├── 📄 tracker.py                       # Main BitcoinPriceTracker class
    │
    ├── 📁 core/                            # Core functionality modules
    │   ├── 📄 __init__.py                 
    │   ├── 📄 database.py                  # SQLite database operations
    │   ├── 📄 api_client.py                # Bitcoin price API integration
    │   ├── 📄 portfolio.py                 # Portfolio management & P/L
    │   ├── 📄 lightning.py                 # Lightning Network features
    │   └── 📄 alerts.py                    # Alert system & notifications
    │
    ├── 📁 utils/                           # Utility modules
    │   ├── 📄 __init__.py
    │   └── 📄 charts.py                    # Chart generation (matplotlib)
    │
    └── 📁 ui/                              # User interface
        └── 📄 menu.py                      # Interactive menu system

📊 bitcoin_prices.db                        # SQLite database (auto-created)