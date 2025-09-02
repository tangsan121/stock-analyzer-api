from fastapi import FastAPI
from pydantic import BaseModel
from utils.analyzer import analyze_stock

app = FastAPI()

class StockRequest(BaseModel):
    symbol: str

@app.post("/analyze")
def analyze(req: StockRequest):
    result = analyze_stock(req.symbol.upper())
    return result

@app.get("/")
def root():
    return {"msg": "📈 Stock Analyzer API is running"}
