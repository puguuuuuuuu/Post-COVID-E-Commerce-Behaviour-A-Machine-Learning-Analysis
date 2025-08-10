import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from datetime import timedelta

# --- paths ---
DATA_PATH = "/content/Merged_E-Commerce___COVID_Dataset.csv"  # change if needed

# --- load ---
df = pd.read_csv(DATA_PATH)

# --- basic types ---
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
df = df.dropna(subset=['InvoiceDate'])

# compute TotalPrice if missing
if 'TotalPrice' not in df.columns:
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# keep only plausible rows
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
df = df.dropna(subset=['CustomerID'])

print(df.head())
print(df.dtypes)
print("Rows:", len(df))
