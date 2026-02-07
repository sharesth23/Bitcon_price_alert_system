
Enhanced readme · MD
Copy

# Enhanced Bitcoin Price Tracker & Portfolio Manager 📊⚡

> A comprehensive Bitcoin price monitoring and portfolio management system with advanced features including multi-currency support, live charts, desktop notifications, and Lightning Network integration.

**Created for:** Summer of Bitcoin 2026 Application  
**Author:** Sharesth  
**Track:** Developer Track

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Bitcoin](https://img.shields.io/badge/Bitcoin-Testnet-orange.svg)](https://bitcoin.org)
[![Lightning](https://img.shields.io/badge/Lightning-Network-blueviolet.svg)](https://lightning.network)

---
## 🎯 Project Overview

This project demonstrates comprehensive understanding of:
- **Multi-API Bitcoin price aggregation** with redundancy and failover
- **Multi-currency support** (USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, INR)
- **Real-time data visualization** using matplotlib
- **Portfolio management** with profit/loss tracking
- **Desktop notifications** for price alerts
- **Lightning Network** integration and payment processing
- **Database design** for historical analysis
- **Professional Python development** practices

---

## ✨ Enhanced Features

### 🔥 New Features Added

#### 1. **Historical Price Charts** 📈
- **Static charts** - Generate beautiful charts for any time period
- **Live updating charts** - Real-time price visualization
- **Customizable timeframes** - View 1hr, 24hr, 7 days, or custom periods
- **Professional styling** - Bitcoin orange theme with statistical overlays
- **High-resolution export** - Save charts as PNG for presentations

```python
# Generate 24-hour chart
tracker.plot_price_chart(hours=24)

# Start live chart (updates every 60 seconds)
tracker.plot_live_chart(interval_seconds=60)
```

#### 2. **Lightning Network Price Feed** ⚡
- **Lightning price oracles** integration
- **BOLT11 invoice generation** with proper formatting
- **Payment verification** system
- **Routing fee estimation** based on network topology
- **Channel balance monitoring**

```python
# Create Lightning invoice
invoice = lightning.create_invoice(
    amount_sats=100000,
    description="BTC Price Alert Subscription"
)

# Estimate routing fee
fee = lightning.estimate_routing_fee(amount_sats=100000, hops=3)
```

#### 3. **Desktop Notifications** 🔔
- **Smart alerts** for price movements (2%, 5%, 10% thresholds)
- **Portfolio updates** when adding/removing holdings
- **Cross-platform support** (Windows, macOS, Linux)
- **Urgency levels** for critical price movements

```python
# Automatic notifications on price alerts
🚨 CRITICAL Alert: BTC $95,234.56 (+10.34% in 1hr)
```

#### 4. **Portfolio Value Tracking** 💼
- **Multiple holdings** management
- **Real-time valuation** in your preferred currency
- **Profit/Loss calculation** with percentage returns
- **Historical performance** charts
- **Portfolio snapshots** saved automatically
- **Per-holding tracking** with purchase dates and notes

```python
# Add to portfolio
tracker.add_to_portfolio(
    btc_amount=0.5,
    purchase_price=45000,
    currency='USD',
    note='First Bitcoin purchase'
)

# View portfolio summary
tracker.display_portfolio()
```

#### 5. **Multi-Currency Support** 💱
- **9 major currencies** supported
- **Real-time conversion** across all features
- **Currency-specific symbols** (€, £, ¥, ₹, etc.)
- **Consistent tracking** across currency changes

Supported: USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, INR

```python
# Switch to Euros
tracker.set_currency('EUR')

# Switch to Indian Rupees
tracker.set_currency('INR')
```

---
## 🚀 Quick Start

### Prerequisites
```bash
# Python 3.8 or higher
python --version

# Install all dependencies
pip install -r requirements.txt
```
