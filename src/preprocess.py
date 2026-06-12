import pandas as pd

df = pd.read_csv(
    "data/raw/OnlineRetail.csv",
    encoding="ISO-8859-1"
)

print("Original Shape:", df.shape)

# Remove null values
df.dropna(inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Remove cancelled orders
df = df[
    ~df['InvoiceNo'].astype(str).str.startswith('C')
]

# Remove negative quantity
df = df[df['Quantity'] > 0]

# Revenue column
df['Revenue'] = (
    df['Quantity'] *
    df['UnitPrice']
)

df.to_csv(
    "data/processed/cleaned_data.csv",
    index=False
)

print("Cleaned Shape:", df.shape)
print("Data Saved Successfully")