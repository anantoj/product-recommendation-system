# Product Recommendation System

This is a product recommendation system built with Python and Flask. It uses a collaborative filtering model to predict product ratings and recommend products to customers.

## Features

- Predict product ratings for a given customer
- Recommend top N products for a given customer
- Display product details including ID, category, and price
- User-friendly web interface with Bootstrap

## Installation

1. Clone this repository:

    ```
    git clone https://github.com/anantoj/product-recommendation-system.git
    cd product-recommendation-system
    ```

2. Install the required packages:

    ```
    pip install -r requirements.txt
    ```

3. Run the application:

    ```
    flask run
    ```

4. Open your web browser and navigate to `http://localhost:5000`.

## Usage

1. Enter a customer ID and the number of recommendations in the form on the home page.
2. Click the "Get Recommendations" button to get the top N recommended products for the given customer.
3. The recommended products will be displayed below the form, along with their categories, prices, and predicted ratings.

## Data Generation (Seeding)

The data used in this project is generated using the `Faker` library and Python's built-in `random` module. The data generation process is documented in the `seed.py` script. Here's a brief overview of what's covered in the script:

- Initialize Faker
- Generate `customer_interactions` data, which includes `customer_id`, `page_views`, and `time_spent_on_website`
- Generate `purchase_history` data, which includes `customer_id`, `product_id`, and `purchase_date`
- Generate `product_details` data, which includes `product_id`, `category`, `price`, and `ratings`
- Introduce some outliers in the price
- Save dataframes to CSV files

The generated data is saved in the `data` directory, with the following files:

- `customer_interactions.csv`: Contains data about customer interactions
- `purchase_history.csv`: Contains data about purchase history
- `product_details.csv`: Contains data about product details

You can run the `seed.py` script to generate the data. Be sure to install the required packages with `pip install -r requirements.txt` before running the script.

## Data Analysis and Model Training

The data analysis and model training process is documented in the `data_exploration.ipynb` Jupyter notebook. Here's a brief overview of what's covered in the notebook:

### Data Analysis

The first part of the notebook is dedicated to exploring and understanding the data. This includes:

- Loading the data from CSV files
- Checking for missing values
- Visualizing the distribution of product ratings
- Analyzing the number of products in each category
- Visualizing the relationship between price and ratings
- Analyzing the correlations between page views, time spent on website, price, and ratings

### Model Training

The second part of the notebook focuses on training two models: a collaborative filtering model using the SVD algorithm, and a content-based model using a decision tree regressor. This involves:

- Loading the data into a format that the SVD algorithm can use
- Splitting the data into a training set and a test set
- Training the SVD model on the training set
- Converting the 'category' column to numerical values
- Training the decision tree model on the customer id, product id, page views, time spent on website, price, and category

### Model Usage

The final part of the notebook demonstrates how to use the trained models to predict the next product a customer is likely to buy. This includes:

- Getting a list of products that the customer hasn't bought yet
- Using the models to predict the rating the customer would give to each product they haven't bought yet
- Sorting the predictions by estimated rating in descending order
- Returning the product id with the highest estimated rating

You can run the notebook in Jupyter to follow along with the data analysis and model training process. Be sure to install the required packages with `pip install -r requirements.txt` before running the notebook.
