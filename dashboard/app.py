import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Smart Retail Analytics",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Smart Retail Analytics & Recommendation System")

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("data/processed/cleaned_data.csv")

# Revenue Column
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# -----------------------------
# Sidebar
# -----------------------------
page = st.sidebar.selectbox(
    "Navigation",
    [
        "Dashboard",
        "Product Analytics",
        "Market Basket Analysis",
        "Recommendations"
    ]
)

# ======================================================
# DASHBOARD PAGE
# ======================================================

if page == "Dashboard":

    st.header("📊 Business Overview")

    total_orders = df["InvoiceNo"].nunique()
    total_products = df["Description"].nunique()
    total_customers = df["CustomerID"].nunique()
    total_revenue = round(df["Revenue"].sum(), 2)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Orders", total_orders)
    col2.metric("Products", total_products)
    col3.metric("Customers", total_customers)
    col4.metric("Revenue (£)", total_revenue)

    st.divider()

    top_products = (
        df.groupby("Description")["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig = px.bar(
        top_products,
        x="Quantity",
        y="Description",
        orientation="h",
        title="Top Selling Products"
    )

    st.plotly_chart(fig, use_container_width=True)

# ======================================================
# PRODUCT ANALYTICS
# ======================================================

elif page == "Product Analytics":

    st.header("📦 Product Analytics")

    top_products = (
        df.groupby("Description")["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig1 = px.bar(
        top_products,
        x="Quantity",
        y="Description",
        orientation="h",
        title="Top Selling Products"
    )

    st.plotly_chart(fig1, use_container_width=True)

    top_revenue = (
        df.groupby("Description")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    fig2 = px.bar(
        top_revenue,
        x="Revenue",
        y="Description",
        orientation="h",
        title="Top Revenue Products"
    )

    st.plotly_chart(fig2, use_container_width=True)

# ======================================================
# MARKET BASKET ANALYSIS
# ======================================================

elif page == "Market Basket Analysis":

    st.header("🧠 Association Rules")

    rules = pd.read_csv(
        "data/processed/apriori_rules.csv"
    )

    st.write("Total Rules:", len(rules))

    st.dataframe(
        rules[
            [
                "antecedents",
                "consequents",
                "support",
                "confidence",
                "lift"
            ]
        ].head(20)
    )

    fig = px.scatter(
        rules,
        x="support",
        y="confidence",
        size="lift",
        title="Support vs Confidence"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ======================================================
# RECOMMENDATION PAGE
# ======================================================

elif page == "Recommendations":

    st.header("🎯 Product Recommendation")

    products = st.text_input(
        "Enter Product Name"
    )

    if st.button("Recommend"):

        try:

            response = requests.get(
                f"http://127.0.0.1:8000/recommend?items={products}"
            )

            result = response.json()

            st.success(
                "Recommendations Generated"
            )

            for item in result["recommendations"]:

                st.write("✅", item)

        except Exception as e:

            st.error(
                "FastAPI Server Not Running"
            )

            st.code(str(e))