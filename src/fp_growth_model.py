import pandas as pd

from mlxtend.frequent_patterns import fpgrowth
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

basket = basket.map(
    lambda x: 1 if x > 0 else 0
)

itemsets = fpgrowth(
    basket,
    min_support=0.02,
    use_colnames=True
)

rules = association_rules(
    itemsets,
    metric="lift",
    min_threshold=1
)

rules.to_csv(
    "data/processed/fp_growth_rules.csv",
    index=False
)

print("FP Growth Rules Generated")