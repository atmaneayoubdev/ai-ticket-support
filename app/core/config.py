# # Correct way to import after migration
# from pydantic_settings import BaseSettings
# from pydantic import Field

# class Settings(BaseSettings):
#     # Google Cloud credentials
#     OPENAI_API_KEY: str = Field(..., env='OPENAI_API_KEY')

#     class Config:
#         env_file = ".env"
#         env_file_encoding = 'utf-8'

# # Instantiate the settings
# settings = Settings()
