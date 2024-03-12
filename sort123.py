import pandas as pd
import numpy as np

def read(x, sheet_name):
    data = pd.read_excel(x, sheet_name=sheet_name)
    return data
def rank(A):
    rank=np.linalg.matrix_rank(A)
    return rank

def inverse(A):
    inv=np.linalg.pinv(A)
    return inv

data=read("Lab_Session1_Data.xlsx")
A=data[["Candies (#)","Mangoes (Kg)", "Milk Packets (#)"]].values
C=data[["Payment (Rs)"]].values
#Dimensionality of matrix
print(F"Dimensionality of A is {A.shape}")
#Number of vectors
print(F"No of vectors of A is {len(A)}")
# Rank of matrix
print(f"rank of matrix A is {rank(A)}")
#inverse of matrix
# Finding X
X=np.dot(inverse(A),C)




# Use the Pseudo-inverse to calculate the model vector X for
#predicting the cost of the products available with the vendor
prices=np.dot(A,X)

# Mark all customers(in the “Purchase Data” table)with payments above Rs. 200 as RICH and
#others as POOR. Develop a classifier model to categorize customers \
#into RICH or POOR class based on purchase behavior.
bias=[]
for i in range(len(prices)):
    if prices[i]>200:
        bias.append("RICH")
    else:
        bias.append("POOR")
data.insert(11, "Class", bias,True)
print(data[["Class"]])
