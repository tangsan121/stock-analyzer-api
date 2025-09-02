from fastapi import FastAPI
from pydantic import BaseModel
from utils.analysis import analyze_stock
from utils.price_fetcher import fetch_prices

app = FastAPI()

class StockRequest(BaseModel):
    symbols: list[str]

@app.post("/analyze")
def analyze(request: StockRequest):
    results = []
    for symbol in request.symbols:
        prices = fetch_prices(symbol)
        analysis = analyze_stock(prices)
        results.append({
            "symbol": symbol,
            "analysis": analysis
        })
    return results
