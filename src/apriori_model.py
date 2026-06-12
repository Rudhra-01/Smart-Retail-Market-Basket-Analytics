import pandas as pd

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

df = pd.read_csv(
    "data/processed/cleaned_data.csv"
)

basket = (
    df.groupby(
        ['InvoiceNo', 'Description']
    )['Quantity']
      .sum()
      .unstack()
      .fillna(0)
)

basket = (basket > 0).astype(int)

frequent_itemsets = apriori(
    basket,
    min_support=0.02,
    use_colnames=True
)

rules = association_rules(
    frequent_itemsets,
    metric="lift",
    min_threshold=1
)

rules.to_csv(
    "data/processed/apriori_rules.csv",
    index=False
)

print("Apriori Rules Generated Successfully")
print("Total Rules:", len(rules))