# -*- coding: utf-8 -*-
__author__ = 'Nikolay Mamashin (mamashin@gmail.com)'

from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import final


@final
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=('.prod.env', '.dev.env'),  # first search .dev.env, then .prod.env
        env_file_encoding='utf-8')

    debug: bool = True
    redis_url: str = 'redis://localhost:6379/0'
    bot_token: str = '8093597120:AAF1ke50EBqlwofsuJK8qeBT4hFbOj0pZcw'
    base_webhook_url: str = 'https://ai.669.su'
    webhook_path: str = '/'
    telegram_my_token: str = 'AAF1ke50EBqlwofsuJK8qeBT4hFbOj0pZcw'  # Additional security token for webhook


@lru_cache()  # get it from memory
def get_settings() -> Settings:
    return Settings()
