import pandas as pd
from faker import Faker
import random
from random import randint
import numpy as np

# Initialize Faker
fake = Faker()

num_samples = 1000

# Generate customer_interactions data
customer_interactions = pd.DataFrame(
    {
        "customer_id": [
            fake.unique.random_number(digits=5) if random.random() > 0.05 else np.nan
            for _ in range(num_samples)
        ],
        "page_views": [
            randint(1, 100) if random.random() > 0.05 else np.nan
            for _ in range(num_samples)
        ],
        "time_spent_on_website": [
            randint(1, 60) if random.random() > 0.05 else np.nan
            for _ in range(num_samples)
        ],  # in minutes
    }
)

# Generate purchase_history data
purchase_history = pd.DataFrame(
    {
        "customer_id": customer_interactions["customer_id"],
        "product_id": [
            fake.unique.random_number(digits=5) if random.random() > 0.05 else np.nan
            for _ in range(num_samples)
        ],
        "purchase_date": [
            fake.date_between(start_date="-1y", end_date="today")
            if random.random() > 0.05
            else np.nan
            for _ in range(num_samples)
        ],
    }
)

# Generate product_details data
product_details = pd.DataFrame(
    {
        "product_id": purchase_history["product_id"],
        "category": [
            fake.word(
                ext_word_list=["electronics", "clothing", "home", "books", "sports"]
            )
            if random.random() > 0.05
            else np.nan
            for _ in range(num_samples)
        ],
        "price": [
            round(random.uniform(10.5, 200.5), 2) if random.random() > 0.05 else np.nan
            for _ in range(num_samples)
        ],
        "ratings": [
            round(random.uniform(1.0, 5.0), 1) if random.random() > 0.05 else np.nan
            for _ in range(num_samples)
        ],
    }
)

# Introduce some outliers in the price
for _ in range(50):  # add 50 outliers
    product_details.loc[randint(0, num_samples - 1), "price"] = round(
        random.uniform(1000, 2000), 2
    )

# Save dataframes to CSV files
customer_interactions.to_csv("data/customer_interactions.csv", index=False)
purchase_history.to_csv("data/purchase_history.csv", index=False)
product_details.to_csv("data/product_details.csv", index=False)
