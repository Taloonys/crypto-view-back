from pydantic_settings import BaseSettings, SettingsConfigDict
"""
CMC - stands for CoinMarketCap
It's a data source i would stick to.
"""


class Settings(BaseSettings):
    """
    Just grab API-key from environment variables
    """
    CMC_API_KEY: str
    
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()