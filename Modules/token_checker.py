import json
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
import requests

URL = "https://samacontrol.ir/sama/api/org"

def check_token(token: str):
    """
    give token and get user id
    """
    try:
        headers = {
            "Authorization": f"bearer {token}"
        }
        response = requests.get(URL, headers=headers)
        dic = json.loads(jsonable_encoder(response.text))
        org = dic["org"][0]
        user_id = org["ID_user"]
        return user_id
    except HTTPException:
        HTTPException(403, "you don\'t have acces to this service")