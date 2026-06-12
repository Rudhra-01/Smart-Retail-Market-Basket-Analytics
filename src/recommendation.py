import pandas as pd

rules = pd.read_csv(
    "data/processed/apriori_rules.csv"
)

def recommend(products):

    products = [
        p.strip().lower()
        for p in products
    ]

    recommendations = []

    for _, row in rules.iterrows():

        antecedent = str(
            row['antecedents']
        ).lower()

        if all(
            product in antecedent
            for product in products
        ):

            recommendations.append({
                "product": str(row['consequents']),
                "lift": row['lift']
            })

    recommendations = sorted(
        recommendations,
        key=lambda x: x["lift"],
        reverse=True
    )

    return recommendations[:10]