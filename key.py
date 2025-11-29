from fastapi import HTTPException
from fastapi.security import APIKeyHeader

KEY_HEADER_NAME = "X-API-KEY"

USER_KEYS = [
    "4FK23B",
    "E28019",
    "8M0M9D",
    "05V2KC"
]

API_KEY_HEADER = APIKeyHeader(name=KEY_HEADER_NAME)


def validate(key: str) -> None:
    if key not in USER_KEYS:
        raise HTTPException(401, "Invalid API key")
