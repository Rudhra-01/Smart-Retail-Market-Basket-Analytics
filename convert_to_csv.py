import pandas as pd

df = pd.read_excel(
    "data/raw/Online Retail.xlsx"
)

df.to_csv(
    "data/raw/OnlineRetail.csv",
    index=False
)

print("CSV File Created Successfully")