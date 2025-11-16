from fastapi import HTTPException, Header

FAKE_TOKEN = "abc123"

def auth_required(token: str = Header(None)):
    if token != FAKE_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True
