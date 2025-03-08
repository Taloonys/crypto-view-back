from fastapi import FastAPI
from src.http_client import CMCHTTPClient
from src.config import settings


app = FastAPI()


cmc_client = CMCHTTPClient(
    base_url="https://pro-api.coinmarketcap.com",
    api_key=settings.CMC_API_KEY
)


@app.get("/cryptocurrencies")
async def get_currencies():
    return await cmc_client.get_listenings()


@app.get("/cryptocurrencies/{currency_id}")
async def get_currencies(currency_id: int):
    return await cmc_client.get_currency(currency_id)