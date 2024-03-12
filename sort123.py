import pandas as pd
import numpy as np

def read_excel_data(file_path, sheet_name):
    data = pd.read_excel(file_path, sheet_name=sheet_name)
    return data

def calculate_matrix_rank(matrix):
    rank = np.linalg.matrix_rank(matrix)
    return rank

def calculate_matrix_pseudoinverse(matrix):
    pseudoinverse = np.linalg.pinv(matrix)
    return pseudoinverse

# Read data from Excel file
data = read_excel_data("Lab_Session1_Data.xlsx", sheet_name="Sheet1")

# Extract relevant columns as numpy arrays
features = data[["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)"]].values
payments = data[["Payment (Rs)"]].values

# Dimensionality of the feature matrix
print(f"Dimensionality of feature matrix: {features.shape}")

# Number of vectors in the feature matrix
print(f"Number of vectors in feature matrix: {len(features)}")

# Calculate rank of the feature matrix
print(f"Rank of the feature matrix: {calculate_matrix_rank(features)}")

# Calculate the pseudoinverse of the feature matrix
pseudoinverse = calculate_matrix_pseudoinverse(features)

# Calculate the model vector X
model_vector = np.dot(pseudoinverse, payments)

# Calculate the prices of the products
prices = np.dot(features, model_vector)

# Categorize customers as RICH or POOR based on payment amount
customer_classes = []
for price in prices:
    if price > 200:
        customer_classes.append("RICH")
    else:
        customer_classes.append("POOR")

# Insert the 'Class' column into the data DataFrame
data.insert(11, "Class", customer_classes, True)

# Print the 'Class' column
print(data[["Class"]])
