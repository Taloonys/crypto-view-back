from src.http_client import CMCHTTPClient
from src.config import API_KEY


cmc_client = CMCHTTPClient(
    base_url = "https://pro-api.coinmarketcap.com",
    api_key  = API_KEY
)