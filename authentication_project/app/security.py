from fastapi import Depens, HTTPExeption, status
from fastapi.security import APIKeyHeader
from dotev import load_dotenv
import os

load_dotenv()

API_KEY_NAME = "api-key"

api_key_header =APIKeyHeader(name=API_KEY_NAME, auto_error =False)

def get_api_key(api_key:str =Depens(api_key_header)):
    allowed_api_keys =os.getenv("API_KEYS", "").split(",")

    print("Recieved API Key:" api_key)
    print("Allowed API Keys:", allowed_api_keys)

    if api_key not in allowed_api_keys:
        print("API Key is invalid.")
        raise HTTPExeption(
            status_code =status.HTTP_401_UNATHORIZED,
            detail="Invalid API Key"
        )
    print("API Key is valid.")
    return api_key