# 🛒 Smart Retail Analytics & Product Recommendation System

## 📌 Overview

The Smart Retail Analytics & Product Recommendation System is an end-to-end Data Science project that analyzes retail transaction data to uncover customer purchasing patterns and generate intelligent product recommendations.

The project leverages Association Rule Mining techniques such as Apriori and FP-Growth to identify frequently purchased product combinations and provide actionable business insights. It also includes a FastAPI backend and an interactive Streamlit dashboard for data visualization and recommendations.

---

## 🚀 Features

### Data Processing

* Data Cleaning & Preprocessing
* Missing Value Handling
* Duplicate Removal
* Feature Engineering

### Analytics

* Exploratory Data Analysis (EDA)
* Product Performance Analysis
* Revenue Analysis
* Country-wise Sales Analysis
* Monthly Sales Trends

### Machine Learning

* Apriori Algorithm
* FP-Growth Algorithm
* Association Rule Mining
* Market Basket Analysis
* Product Recommendation Engine

### Deployment Components

* FastAPI Backend
* Interactive Streamlit Dashboard
* Business Insights Generation
---

## 📊 Dataset

**Dataset:** Online Retail Dataset

The dataset contains transactional records of an online retail store.

### Features

| Column      | Description         |
| ----------- | ------------------- |
| InvoiceNo   | Transaction ID      |
| StockCode   | Product Code        |
| Description | Product Name        |
| Quantity    | Quantity Purchased  |
| InvoiceDate | Transaction Date    |
| UnitPrice   | Product Price       |
| CustomerID  | Customer Identifier |
| Country     | Customer Country    |

---

## ⚙️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Plotly
* Mlxtend
* Scikit-Learn

### Backend

* FastAPI
* Uvicorn

### Frontend

* Streamlit

---

## 🔍 Methodology

### 1. Data Preprocessing

* Removed missing values
* Removed duplicate records
* Removed cancelled orders
* Removed negative quantity values

### 2. Feature Engineering

Created additional business metrics:

Revenue = Quantity × UnitPrice

### 3. Market Basket Analysis

Implemented:

* Apriori Algorithm
* FP-Growth Algorithm

Generated:

* Frequent Itemsets
* Association Rules
* Support
* Confidence
* Lift

### 4. Recommendation Engine

The recommendation engine uses association rules to suggest products frequently purchased together.

Example:

Input:

```text
LUNCH BAG RED RETROSPOT
```

Output:

```text
LUNCH BAG SUKI DESIGN
```

---

## 📈 Dashboard Modules

### Dashboard

* Total Orders
* Total Products
* Total Customers
* Total Revenue

### Product Analytics

* Top Selling Products
* Top Revenue Products

### Market Basket Analysis

* Association Rules
* Support vs Confidence Analysis

### Recommendations

* Product Recommendation Engine

---

## 🌐 API Endpoints

### Home

```http
GET /
```

### Recommendation

```http
GET /recommend
```

Example:

```http
/recommend?items=LUNCH BAG RED RETROSPOT
```

### Health Check

```http
GET /health
```
## 💡 Business Impact

This project helps retailers:

* Discover frequently purchased products
* Improve cross-selling opportunities
* Optimize product placement
* Increase customer engagement
* Generate actionable business insights

---

## 🔮 Future Enhancements

* Docker Deployment
* Cloud Deployment
* Customer Segmentation
* Advanced Recommendation Engine
* Real-Time Analytics Dashboard

---

## 👨‍💻 Author

**Rudhra Roopini**

Data Science Enthusiast | Machine Learning | Analytics | AI Applications

