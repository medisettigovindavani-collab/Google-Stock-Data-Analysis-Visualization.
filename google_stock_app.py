import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import numpy as np

# Page Configuration
st.set_page_config(page_title="Google Stock Analysis", layout="wide")

# Title and Header
st.title("Google Stock Data Analysis and Prediction")
st.subheader("A visualization and prediction tool for Google's stock prices (2004–2024)")

# Sidebar
st.sidebar.header("Navigation")
nav_options = ["Data Overview", "Yearly Average Analysis", "Prediction"]
choice = st.sidebar.radio("Select Page:", nav_options)



@st.cache_data
def load_data():
    df = pd.read_csv("C:\\Users\\chakr\\OneDrive\\stockdata.csv")
    df['Date'] = pd.to_datetime(df['Date'])  # Convert 'Date' column to datetime
    return df

# Load the Data
df = load_data()

# Extract 'Year' from 'Date' column
df['Year'] = df['Date'].dt.year

if choice == "Data Overview":
    st.header("Google Stock Data Overview")
    st.write("Below is a preview of the dataset used for analysis.")
    st.write(df.head())

    st.write("Basic Statistics of the Dataset:")
    st.write(df.describe())

elif choice == "Yearly Average Analysis":
    st.header("Yearly Average Opening Prices of Google Stock")

    # Create a Year column
    df['Year'] = df['Date'].dt.year

    # Calculate yearly averages
    yearly_avg_open = df.groupby('Year')['Open'].mean()

    # Plotting the bar chart
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.bar(yearly_avg_open.index, yearly_avg_open.values, color='cornflowerblue', edgecolor='black')
    ax.set_xlabel("Year", fontsize=12, labelpad=10)
    ax.set_ylabel("Average Opening Price (USD)", fontsize=12, labelpad=10)
    ax.set_title("Yearly Average Opening Prices of Google Stock", fontsize=14, pad=15)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    for year, value in zip(yearly_avg_open.index, yearly_avg_open.values):
        ax.text(year, value + 1, f"{value:.2f}", ha='center', va='bottom', fontsize=10)
    plt.xticks(yearly_avg_open.index, rotation=45, fontsize=10)
    plt.tight_layout()

    # Display plot in Streamlit
    st.pyplot(fig)

    # Insights
    st.write("**Insights:**")
    st.markdown("""
    - 2024 saw a significant increase in Google's average opening stock price compared to previous years.
    - The average opening price in 2024 was 1.67 USD, marking a sharp rise from the previous year's average of 0.57 USD.
    - This represents a substantial growth trajectory for Google's stock in 2024.
    """)

elif choice == "Prediction":
    st.header("Google Stock Price Prediction")
    st.write(
        """
        Enter the required stock details below to predict the closing price.
        This is a demonstration page, so predictions are simulated.
        """
    )

    # Input Fields
    st.subheader("Enter Stock Details:")
    open_price = st.number_input("Opening Price (e.g., 1500.00)", min_value=0.0, step=0.01)
    high_price = st.number_input("High Price (e.g., 1550.00)", min_value=0.0, step=0.01)
    low_price = st.number_input("Low Price (e.g., 1480.00)", min_value=0.0, step=0.01)
    volume = st.number_input("Volume (e.g., 2000000)", min_value=0, step=1000)

    # Button to trigger prediction
    if st.button("Predict Closing Price"):
        try:
            # Simulated Prediction Logic
            avg_price = (open_price + high_price + low_price) / 3
            simulated_closing_price = avg_price + (volume * 0.000001)  # Add a small adjustment based on volume
            
            # Display the simulated result
            st.success(f"Predicted Closing Price: ${simulated_closing_price:,.2f}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
