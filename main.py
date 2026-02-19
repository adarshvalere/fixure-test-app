from fastapi import FastAPI

app = FastAPI()

# SECURITY VULNERABILITY: Hardcoded Secret
SECRET_KEY = "super-secret-key-12345"

@app.get("/")
def read_root():
    return {"message": "Hello Fixure User"}

@app.get("/items/{item_id}")
def read_item(item_id: str):
    # This is where a DAST tool might try to inject SQL or scripts
    return {"item_id": item_id, "internal_key": SECRET_KEY}