Project Overview
This project involves predicting the prices of products based on various features. The dataset includes information about different product attributes such as brand, material, size, compartments, laptop compartment, waterproof, style, color, weight capacity, and price.

Data Description
The dataset consists of the following columns:

Brand: The brand of the product.
Material: The material of the product.
Size: The size of the product.
Compartments: The number of compartments in the product.
Laptop Compartment: Whether the product has a laptop compartment.
Waterproof: Whether the product is waterproof.
Style: The style of the product.
Color: The color of the product.
Weight Capacity (kg): The weight capacity of the product in kilograms.
Price: The price of the product (target variable).
Achievements
Data Exploration and Visualization:

Loaded and inspected the data.
Visualized categorical and numerical features using count plots and histograms.
Checked for missing values and data types.
Data Preprocessing:

Handled missing values using SimpleImputer.
Encoded categorical features using OneHotEncoder.
Scaled numerical features using StandardScaler.
Combined preprocessing steps into a pipeline using ColumnTransformer.
Model Training and Evaluation:

Split the data into training and testing sets.
Trained multiple models including Linear Regression and Gradient Boosting Regressor.
Evaluated models using Mean Squared Error (MSE) and R-squared score.
Selected the best model based on performance metrics.
Model Deployment:

Trained the best model on the full dataset.
Saved the trained model using joblib.
Created a Streamlit web application for user interaction and predictions.
Prepared the project for deployment on Heroku.
Conclusion
This project demonstrates a complete machine learning workflow, from data exploration and preprocessing to model training, evaluation, and deployment. The final model can predict product prices based on various features, and the Streamlit app provides an interactive interface for users to input parameters and get predictions.
