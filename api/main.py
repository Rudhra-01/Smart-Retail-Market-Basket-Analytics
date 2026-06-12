from fastapi import FastAPI

from src.recommendation import recommend

app = FastAPI()

@app.get("/")
def home():

    return {
        "message":
        "Smart Retail Analytics API"
    }

@app.get("/recommend")
def get_recommendation(
    items: str
):

    products = items.split(",")

    result = recommend(products)

    return {
        "products": products,
        "recommendations": result
    }