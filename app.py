
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Health Monitoring System", layout="wide")

st.title("🩺 AI-Powered Health Monitoring Dashboard")

st.markdown("""
This is a sample **AI-powered health monitoring system** that visualizes and detects anomalies in health data.
Feel free to customize this with your own model or live data.
""")

# Simulate data
np.random.seed(42)
df = pd.DataFrame({
    "Time": pd.date_range("2025-01-01", periods=100, freq="H"),
    "Heart Rate (bpm)": np.random.normal(72, 10, 100).astype(int),
    "SpO2 (%)": np.clip(np.random.normal(96, 2, 100), 90, 100),
    "Temperature (°C)": np.random.normal(36.5, 0.5, 100)
})

# Show data
st.subheader("📊 Patient Health Data")
st.dataframe(df.tail(10))

# Plot
st.subheader("📈 Trends")
fig, ax = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
ax[0].plot(df["Time"], df["Heart Rate (bpm)"], color="red")
ax[0].set_title("Heart Rate")
ax[1].plot(df["Time"], df["SpO2 (%)"], color="green")
ax[1].set_title("SpO2")
ax[2].plot(df["Time"], df["Temperature (°C)"], color="blue")
ax[2].set_title("Temperature")
st.pyplot(fig)

# Anomaly detection example
st.subheader("🚨 Anomaly Detection")
anomalies = df[df["Heart Rate (bpm)"] > 100]
st.warning(f"⚠️ Detected {len(anomalies)} anomaly/anomalies where heart rate exceeded 100 bpm.")
st.dataframe(anomalies)
