# from pydantic import BaseSettings
#
#
# class Settings(BaseSettings):
#     database_hostname = str
#
#     database_port = str
#     database_password = str
#     database_name = str
#     database_username = str
#     screate_key = str
#     algorithm = str
#     access_token_expire_minutes = int
#
#
#
#
# class Config:
#     env_file = ".env"
#
#
# settings = Settings()
# print(settings.database_port)
#
from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    screate_key:str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()