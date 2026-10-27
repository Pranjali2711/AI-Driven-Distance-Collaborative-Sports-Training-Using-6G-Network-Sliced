import joblib

# Load trained model
model = joblib.load("training_efficiency_model.pkl")

print("AI-Driven Sports Training Efficiency Prediction System")
print("Enter the following parameters:\n")

# User Inputs
heart_rate = float(input("Heart Rate (BPM): "))
acceleration = float(input("Acceleration (m/s^2): "))
latency = float(input("Network Latency (ms): "))
bandwidth = float(input("Bandwidth Usage (Mbps): "))
cpu_util = float(input("CPU Utilization (%): "))
gpu_util = float(input("GPU Utilization (%): "))
ai_alloc = float(input("AI Optimized Allocation (%): "))
packet_loss = float(input("Packet Loss (%): "))
training_duration = float(input("Training Duration (minutes): "))

# Prepare input for model
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

# ML Prediction
prediction = model.predict(input_data)

print("\n===== AI Prediction Result =====")

if prediction[0] == 1:
    print("Training Efficiency: HIGH")
    print("System Status: Training session is running efficiently.")
else:
    print("Training Efficiency: MODERATE")
    print("Warning: Training conditions may reduce session quality.")

# ----------------------------
# Rule-Based Recommendation Engine
# ----------------------------

print("\n===== System Recommendations =====")

recommendations = []

# Network conditions
if latency > 80:
    recommendations.append("Reduce network latency or allocate a low-latency network slice.")

if packet_loss > 3:
    recommendations.append("Improve network reliability to reduce packet loss.")

if bandwidth < 50:
    recommendations.append("Increase bandwidth allocation for smoother data transmission.")

# System resources
if cpu_util > 85:
    recommendations.append("Consider offloading AI computation to edge/cloud resources.")

if gpu_util > 85:
    recommendations.append("Allocate additional GPU resources for faster processing.")

# AI allocation
if ai_alloc < 60:
    recommendations.append("Increase AI resource allocation for better training analytics.")

# If no issues detected
if len(recommendations) == 0:
    print("No optimization required. System conditions are optimal.")
else:
    for rec in recommendations:
        print("•", rec)