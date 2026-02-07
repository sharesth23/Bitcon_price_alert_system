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

## Module Responsibilities

### Core Package (`bitcoin_tracker/`)

#### `config.py` (60 lines)
- API endpoints
- Supported currencies & symbols
- Alert thresholds
- Chart styling settings
- Database configuration

#### `tracker.py` (180 lines)
**Main orchestrator class that coordinates all components**
- Currency management
- Price monitoring loop
- Status display
- Component integration

### Core Modules (`core/`)

#### `database.py` (240 lines)
**All database operations**
- Schema initialization (4 tables)
- Price data storage
- Portfolio CRUD operations
- Statistics calculations
- Historical data queries

#### `api_client.py` (120 lines)
**External API integration**
- CoinDesk API client
- Coinbase API client
- CoinGecko API client
- Multi-source price aggregation
- Automatic failover

#### `portfolio.py` (140 lines)
**Portfolio management**
- Add/manage holdings
- Calculate total BTC
- Compute current value
- Profit/loss calculations
- Format portfolio summaries

#### `lightning.py` (160 lines)
**Lightning Network integration**
- BOLT11 invoice generation
- Payment hash creation
- Payment verification
- Routing fee estimation
- Channel balance (mock)

#### `alerts.py` (80 lines)
**Alert system**
- Price change detection
- Threshold checking
- Desktop notifications
- Alert history logging

### Utilities (`utils/`)

#### `charts.py` (180 lines)
**Data visualization**
- Static price charts
- Live updating charts
- Portfolio performance charts
- Matplotlib configuration
- Chart export (PNG)

### User Interface (`ui/`)

#### `menu.py` (200 lines)
**Interactive menu system**
- Main menu loop
- User input handling
- Feature navigation
- Error messages
- Banner display