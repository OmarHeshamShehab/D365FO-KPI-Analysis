import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

TENANT_ID = os.getenv("AZURE_TENANT_ID")
CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")
BASE_URL = os.getenv("D365_BASE_URL")

AUTH_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
SCOPE = BASE_URL + "/.default"


def get_access_token():
    data = {
        "client_id": CLIENT_ID,
        "scope": SCOPE,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials",
    }
    response = requests.post(AUTH_URL, data=data)
    response.raise_for_status()
    return response.json()["access_token"]


def fetch_odata_entity(entity_name: str, top: int = 100):
    token = get_access_token()
    url = f"{BASE_URL}/data/{entity_name}"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"$top": top}

    response = requests.get(url, headers=headers, params=params, verify=False)
    response.raise_for_status()
    data = response.json().get("value", [])
    return pd.DataFrame(data)
