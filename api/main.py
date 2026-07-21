from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.recommendation import recommend

app = FastAPI(
    title="Smart Retail Recommendation API",
    version="1.0.0"
)

# Allow Streamlit to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Smart Retail Recommendation API is Running"
    }


@app.get("/recommend")
def get_recommendation(items: str):

    products = [item.strip() for item in items.split(",")]

    recommendations = recommend(products)

    return {
        "products": products,
        "recommendations": recommendations
    }