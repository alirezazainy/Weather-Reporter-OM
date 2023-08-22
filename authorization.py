from fastapi import Depends, status, HTTPException, Security
from fastapi.security import (
    OAuth2AuthorizationCodeBearer,
)
from jose import JWTError
from Modules.token_checker import check_token

from schemas import UserBase
# Authorization Processor

# Generate OAuth2 Bearer Instance
oauth2_scheme = OAuth2AuthorizationCodeBearer(tokenUrl="/", authorizationUrl="https://admin.samacontrol.com/#/auth/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    check user validation in Authenticate system
    """
    user = UserBase

    error_credential = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                     detail='invalid credentials',
                                     headers={'WWW-authenticate': 'bearer'})

    try:
        user.id = check_token(token)
        user.token = token
    except JWTError:
        raise error_credential
         
    return user