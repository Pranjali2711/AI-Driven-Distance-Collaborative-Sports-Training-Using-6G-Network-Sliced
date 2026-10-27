import streamlit as st
import joblib

# Load model
model = joblib.load("training_efficiency_model.pkl")

st.title("AI-Driven Sports Training Efficiency System")

st.write("Enter system and network parameters to predict training efficiency.")

# User Inputs
heart_rate = st.slider("Heart Rate (BPM)", 80, 200, 150)
acceleration = st.slider("Acceleration (m/s²)", 0.0, 5.0, 2.5)
latency = st.slider("Network Latency (ms)", 0, 200, 40)
bandwidth = st.slider("Bandwidth Usage (Mbps)", 0, 200, 100)
cpu_util = st.slider("CPU Utilization (%)", 0, 100, 60)
gpu_util = st.slider("GPU Utilization (%)", 0, 100, 60)
ai_alloc = st.slider("AI Optimized Allocation (%)", 0, 100, 70)
packet_loss = st.slider("Packet Loss (%)", 0, 10, 1)
training_duration = st.slider("Training Duration (minutes)", 10, 120, 60)

# Predict Button
if st.button("Predict Training Efficiency"):

    input_data = [[
        heart_rate,
        acceleration,
        latency,
        bandwidth,
        cpu_util,
        gpu_util,
        ai_alloc,
        packet_loss,
        training_duration
    ]]

    prediction = model.predict(input_data)

    st.subheader("Prediction Result")

    if prediction[0] == 0:
        st.subheader("System Recommendations")

    recommendations = []

    if latency > 80:
        recommendations.append("Reduce network latency or allocate low-latency slice")

    if packet_loss > 3:
        recommendations.append("Improve network reliability to reduce packet loss")

    if bandwidth < 50:
        recommendations.append("Increase bandwidth allocation")

    if cpu_util > 85:
        recommendations.append("Offload AI processing to edge/cloud server")

    if gpu_util > 85:
        recommendations.append("Allocate additional GPU resources")

    if ai_alloc < 60:
        recommendations.append("Increase AI resource allocation")

    if len(recommendations) == 0:
        st.info("System conditions are optimal.")
    else:
        for rec in recommendations:
            st.write("•", rec)