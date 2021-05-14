import os
from dotenv import load_dotenv

load_dotenv()

# By default the jupyter notebook will be run on port 8888
PAPERMILL_NOTEBOOK_REPORT_PORT = "8888"

# https://www.alphavantage.co
API_KEY_ALPHAVANTAGE = os.getenv("GT_API_KEY_ALPHAVANTAGE") or "TRUE"

# https://financialmodelingprep.com/developer
API_KEY_FINANCIALMODELINGPREP = (
    os.getenv("GT_API_KEY_FINANCIALMODELINGPREP") or "TRUE"
)

# https://www.quandl.com/tools/api
API_KEY_QUANDL = os.getenv("GT_API_KEY_QUANDL") or "TRUE"

# https://www.reddit.com/prefs/apps
API_REDDIT_CLIENT_ID = os.getenv("GT_API_REDDIT_CLIENT_ID") or "TRUE"
API_REDDIT_CLIENT_SECRET = os.getenv("GT_API_REDDIT_CLIENT_SECRET") or "TRUE"
API_REDDIT_USERNAME = os.getenv("GT_API_REDDIT_USERNAME") or "TRUE"
API_REDDIT_USER_AGENT = os.getenv("GT_API_REDDIT_USER_AGENT") or "TRUE"
API_REDDIT_PASSWORD = os.getenv("GT_API_REDDIT_PASSWORD") or "TRUE"

# https://polygon.io
API_POLYGON_KEY = os.getenv("GT_API_POLYGON_KEY") or "TRUE"

# https://developer.twitter.com
API_TWITTER_KEY = os.getenv("GT_API_TWITTER_KEY") or "TRUE"
API_TWITTER_SECRET_KEY = os.getenv("GT_API_TWITTER_SECRET_KEY") or "TRUE"
API_TWITTER_BEARER_TOKEN = os.getenv("GT_API_TWITTER_BEARER_TOKEN") or "TRUE"

# https://fred.stlouisfed.org/docs/api/api_key.html
API_FRED_KEY = os.getenv("GT_API_FRED_KEY") or "TRUE"

# https://newsapi.org
API_NEWS_TOKEN = os.getenv("GT_API_NEWS_TOKEN") or "TRUE"

# Robinhood
RH_USERNAME = os.getenv("GT_RH_USERNAME") or "TRUE"
RH_PASSWORD = os.getenv("GT_RH_PASSWORD") or "TRUE"

# Degiro
DG_USERNAME = os.getenv("GT_DG_USERNAME") or "TRUE"
DG_PASSWORD = os.getenv("GT_DG_PASSWORD") or "TRUE"

# https://developer.oanda.com
OANDA_ACCOUNT = os.getenv("GT_OANDA_ACCOUNT") or "TRUE"
OANDA_TOKEN = os.getenv("GT_OANDA_TOKEN") or "TRUE"

# https://tradier.com/products/market-data-api
TRADIER_TOKEN = os.getenv("GT_API_TRADIER_TOKEN") or "TRUE"

# Selenium Webbrowser drivers can be found at https://selenium-python.readthedocs.io/installation.html
WEBDRIVER_TO_USE = "chrome"
PATH_TO_SELENIUM_DRIVER = None  # Replace with "PATH"

# https://coinmarketcap.com/api/
API_CMC_KEY = os.getenv("GT_API_CMC_KEY") or "TRUE"

# https://www.binance.com/en/
API_BINANCE_KEY = os.getenv("GT_API_BINANCE_KEY") or "TRUE"
API_BINANCE_SECRET = os.getenv("GT_API_BINANCE_SECRET") or "TRUE"

# https://finnhub.io
API_FINNHUB_KEY = os.getenv("GT_API_FINNHUB_KEY") or "TRUE"
