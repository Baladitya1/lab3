import pandas as pd
import numpy as np
import datetime

def read_excel_data(file_path, sheet_name):
    data = pd.read_excel(file_path, sheet_name=sheet_name)
    return data

# Read data from Excel file
Data = read_excel_data("Lab_Session1_Data.xlsx", sheet_name="IRCTC Stock Price")

# Calculate the mean and variance of the Price data
Price = Data["Price"].values
mean_price = np.mean(Price)
variance_price = np.var(Price)
print(f"Mean value of Prices: {mean_price}")
print(f"Variance of Prices: {variance_price}")

# Convert the date column to datetime format
Data['Date'] = pd.to_datetime(Data['Date'])

# Filter data for Wednesdays
wednesday_data = Data[Data['Date'].dt.dayofweek == 2]  # 2 corresponds to Wednesday
mean_price_wednesday = wednesday_data["Price"].mean()
print(f"Sample mean of Prices on Wednesdays: {mean_price_wednesday}")

# Filter data for the month of April
april_data = Data[Data['Date'].dt.month == 4]  # 4 corresponds to April
mean_price_april = april_data["Price"].mean()
print(f"Sample mean of Prices in April: {mean_price_april}")

# Calculate the probability of making a loss over the stock (Chg% < 0)
loss_probability = len(Data[Data['Chg%'] < 0]) / len(Data)
print(f"Probability of making a loss over the stock: {loss_probability}")

# Calculate the probability of making a profit on Wednesday (Chg% > 0)
wednesday_profit_probability = len(wednesday_data[wednesday_data['Chg%'] > 0]) / len(wednesday_data)
print(f"Probability of making a profit on Wednesday: {wednesday_profit_probability}")

# Calculate the conditional probability of making profit given that today is Wednesday
conditional_profit_probability = len(wednesday_data[wednesday_data['Chg%'] > 0]) / len(Data)
print(f"Conditional probability of making profit given that today is Wednesday: {conditional_profit_probability}")

# Make a scatter plot of Chg% data against the day of the week
import matplotlib.pyplot as plt
plt.scatter(Data['Date'].dt.dayofweek, Data['Chg%'])
plt.xlabel('Day of the Week')
plt.ylabel('Chg%')
plt.title('Chg% data against the day of the week')
plt.show()
