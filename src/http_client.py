from aiohttp import ClientSession
from async_lru import alru_cache


class HTTPClient:
    """
    Connection establishing by api key
    """
    def __init__(self, base_url: str, api_key: str):
        self._session = ClientSession(
            base_url=base_url,
            headers={
                'X-CMC_PRO_API_KEY': api_key,
            }
        )


class CMCHTTPClient(HTTPClient):
    @alru_cache
    async def get_listenings(self):
        """
        GET-request for a whole list of currency & pack it into json
        """
        async with self._session.get("/v1/cryptocurrency/listings/latest") as response:
            result = await response.json()
            return result["data"]
            
    @alru_cache
    async def get_currency(self, currency_id: int):
        """
        GET-request for a concrete crypto-currency
        """
        async with self._session.get(
            "/v2/cryptocurrency/quotes/latest", 
            params={"id": currency_id}
        ) as response:
            result = await response.json()
            return result["data"][str(currency_id)]
