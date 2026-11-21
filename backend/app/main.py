from fastapi import FastAPI
from app.routes.metals import router as metals_router

app = FastAPI(
    title="Bullion & Stock Market Tracker",
    description="Backend API for Indian financial market tracking",
    version="0.1.0"
)

app.include_router(metals_router)

@app.get("/")
def home():
    return {
        "message": "Bullion & Stock Market Tracker API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "member": "Member 1",
        "module": "Backend"
    }
