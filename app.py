# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentinel.scanner import scan_secrets
from sentinel.vault import Vault

app = FastAPI()
vault = Vault()

class ScanRequest(BaseModel):
    file_content: str

@app.post("/scan/")
async def scan(request: ScanRequest):
    secrets = scan_secrets(request.file_content)
    if secrets:
        return {"secrets": secrets}
    return {"message": "No secrets found"}

@app.post("/vault/add/")
async def add_secret(label: str, secret: str):
    vault.add_secret(label, secret)
    return {"message": f"Secret '{label}' added to vault."}

@app.get("/vault/")
async def list_secrets():
    secrets = vault.list_secrets()
    return {"secrets": secrets}

@app.get("/vault/{label}/")
async def get_secret(label: str):
    secret = vault.get_secret(label)
    if secret:
        return {"secret": secret}
    raise HTTPException(status_code=404, detail="Secret not found")
