import os

import dotenv

dotenv.load_dotenv()

# Check if we are backtesting or not
is_backtesting = os.environ.get("IS_BACKTESTING")
if not is_backtesting or is_backtesting.lower() == "false":
    IS_BACKTESTING = False
else:
    IS_BACKTESTING = True

# Discord credentials
DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

# Database connection string
ACCOUNT_HISTORY_DB_CONNECTION_STR = os.environ.get("ACCOUNT_HISTORY_DB_CONNECTION_STR")

POLYGON_CONFIG = {
    # Add POLYGON_API_KEY and POLYGON_IS_PAID_SUBSCRIPTION to your .env file or set them as secrets
    "API_KEY": os.environ.get("POLYGON_API_KEY"),
    "IS_PAID_SUBSCRIPTION": os.environ.get("POLYGON_IS_PAID_SUBSCRIPTION").lower()
    == "true"
    if os.environ.get("POLYGON_IS_PAID_SUBSCRIPTION")
    else False,
}

ALPACA_CONFIG = {  # Paper trading!
    # Add ALPACA_API_KEY, ALPACA_API_SECRET, and ALPACA_IS_PAPER to your .env file or set them as secrets
    "API_KEY": os.environ.get("ALPACA_API_KEY"),
    "API_SECRET": os.environ.get("ALPACA_API_SECRET"),
    "PAPER": os.environ.get("ALPACA_IS_PAPER").lower() == "true"
    if os.environ.get("ALPACA_IS_PAPER")
    else True,
}

TRADIER_CONFIG = {
    # Add TRADIER_ACCESS_TOKEN, TRADIER_ACCOUNT_NUMBER, and TRADIER_IS_PAPER to your .env file or set them as secrets
    "ACCESS_TOKEN": os.environ.get("TRADIER_ACCESS_TOKEN"),
    "ACCOUNT_NUMBER": os.environ.get("TRADIER_ACCOUNT_NUMBER"),
    "PAPER": os.environ.get("TRADIER_IS_PAPER").lower() == "true"
    if os.environ.get("TRADIER_IS_PAPER")
    else True,
}

KRAKEN_CONFIG = {
    # Add KRAKEN_API_KEY and KRAKEN_API_SECRET to your .env file or set them as secrets
    "exchange_id": "kraken",
    "apiKey": os.environ.get("KRAKEN_API_KEY"),
    "secret": os.environ.get("KRAKEN_API_SECRET"),
    "margin": True,
    "sandbox": False,
}

COINBASE_CONFIG = {
    # Add COINBASE_API_KEY and COINBASE_API_SECRET to your .env file or set them as secrets
    "exchange_id": "coinbase",
    "apiKey": os.environ.get("COINBASE_API_KEY"),
    "secret": os.environ.get("COINBASE_API_SECRET"),
    "margin": False,
    "sandbox": False,
}
