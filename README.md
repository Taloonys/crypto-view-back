# General
* Project is just a own research of how to work with FastAPI & how to connect it with frontend.
* Project is based on tutorials https://artemshumeiko.ru/

# Used modules
* pydantic -> for grabbing api key from `.env`
* aiohttp -> for async http requests to `https://coinmarketcap.com/`'s api
* uvicorn -> for simple server launch
* fastapi -> for api routing
* async_lru -> for requests caching

# Run
* Optional & Recomended (venv) `py -m venv <venv-create-folder-name>`
* `pip install -r requirements.txt`
* create `.env` file (there is `.env-template` example)
* insert your api-key for `https://coinmarketcap.com/` right after `CMC_API_KEY=`
* start server by running `uvicorn src.main:app --port=<desired port, by default it's 8000>
