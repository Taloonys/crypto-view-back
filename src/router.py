from fastapi import APIRouter
from src.target_client import cmc_client


router = APIRouter(
    prefix="/cryptocurrencies"
)


@router.get("")
async def get_currencies():
    return await cmc_client.get_listenings()


@router.get("/{currency_id}")
async def get_currencies(currency_id: int):
    return await cmc_client.get_currency(currency_id)