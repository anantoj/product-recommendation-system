from flask import Flask, request, jsonify
import joblib
from collections import defaultdict
import pandas as pd

app = Flask(__name__)

# Load the model from the file
model_cf = joblib.load("model_cf.pkl")

df = pd.read_csv("data/product_details.csv")


def get_top_n_recommendations(customer_id, n=5):
    # First map the predictions to each user.
    predictions = [
        (
            row["product_id"],
            row["category"],
            row["price"],
            model_cf.predict(customer_id, row["product_id"]).est,
        )
        for _, row in df.iterrows()
    ]
    predictions.sort(key=lambda x: x[3], reverse=True)
    top_n = predictions[:n]

    return top_n


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    customer_id = data["customer_id"]
    n_recommendations = int(data["n_recommendations"])
    recommendations = get_top_n_recommendations(customer_id, n_recommendations)
    return jsonify(recommendations)


@app.route("/")
def home():
    return app.send_static_file("index.html")


if __name__ == "__main__":
    app.run(port=5000)
