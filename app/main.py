from fastapi import FastAPI

from app.routers import items

app = FastAPI(title="pg-admin", version="0.1.0")

app.include_router(items.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
