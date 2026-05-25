import streamlit as st
import random
import pandas as pd
from datetime import datetime

# -----------------------------------
# SESSION STORAGE
# -----------------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------------
# TITLE
# -----------------------------------
st.title("AI Smart Bridge Monitoring System")

st.write("Live Traffic & Structural Analysis Dashboard")

# -----------------------------------
# GENERATE DATA BUTTON
# -----------------------------------
if st.button("Generate New Vehicle Data"):

    vehicle_types = ["Car", "Bus", "Truck", "Bike", "Mini Truck"]

    vehicle = random.choice(vehicle_types)

    vehicle_weight = round(random.uniform(0.5, 8.0), 2)

    speed = random.randint(20, 90)

    load = round(random.uniform(0.5, 4.0), 2)

    vibration = round(random.uniform(0.1, 1.5), 2)

    crack_level = round(random.uniform(0.0, 0.8), 2)

    # -----------------------------------
    # AI HISTORY ANALYSIS
    # -----------------------------------

    history = st.session_state.history

    recent_danger = 0

    for item in history[-5:]:

        if item["Condition"] == "DANGER":
            recent_danger += 1

    # -----------------------------------
    # SMART PREDICTION LOGIC
    # -----------------------------------

    score = 0

    if load > 3:
        score += 1

    if vibration > 1:
        score += 1

    if crack_level > 0.5:
        score += 1

    if vehicle_weight > 6:
        score += 1

    # History affects prediction
    score += recent_danger

    # Balanced outputs
    if score <= 1:

        condition = "SAFE"
        risk = "20%"
        suggestion = "Bridge operating normally."

    elif score <= 3:

        condition = "WARNING"
        risk = "55%"
        suggestion = "Bridge should be inspected."

    else:

        condition = "DANGER"
        risk = "85%"
        suggestion = "Immediate maintenance required."

    # -----------------------------------
    # CONTRACTOR NOTIFICATION
    # -----------------------------------

    if condition == "DANGER":

        contractor_msg = """
🚨 ALERT SENT TO CONTRACTOR

Possible structural weakness detected.
Emergency inspection recommended.
Heavy vehicle movement should be restricted.
"""

    elif condition == "WARNING":

        contractor_msg = """
⚠ Notification Sent To Maintenance Team

Bridge stress levels increasing.
Routine inspection recommended.
"""

    else:

        contractor_msg = """
✔ No contractor notification required.
Bridge functioning safely.
"""

    # -----------------------------------
    # STORE HISTORY
    # -----------------------------------

    st.session_state.history.append({
        "Time": datetime.now().strftime("%H:%M:%S"),
        "Vehicle": vehicle,
        "Weight": vehicle_weight,
        "Speed": speed,
        "Load": load,
        "Vibration": vibration,
        "Crack Level": crack_level,
        "Condition": condition,
        "Risk": risk
    })

# -----------------------------------
# DISPLAY DATA
# -----------------------------------

if len(st.session_state.history) > 0:

    latest = st.session_state.history[-1]

    st.header("Current Vehicle Data")

    st.write(f"Vehicle Type: {latest['Vehicle']}")
    st.write(f"Vehicle Weight: {latest['Weight']} Tons")
    st.write(f"Vehicle Speed: {latest['Speed']} km/h")

    st.header("Bridge Structural Data")

    st.write(f"Bridge Load: {latest['Load']} Tons")
    st.write(f"Vibration Level: {latest['Vibration']}")
    st.write(f"Crack Detection Level: {latest['Crack Level']}")

    # -----------------------------------
    # AI ANALYSIS
    # -----------------------------------

    st.header("AI Prediction Result")

    st.write(f"Bridge Condition: {latest['Condition']}")
    st.write(f"Risk Percentage: {latest['Risk']}")

    if latest["Condition"] == "SAFE":

        st.success("Bridge structure stable.")

    elif latest["Condition"] == "WARNING":

        st.warning("Bridge stress increasing.")

    else:

        st.error("Critical structural risk detected!")

    # -----------------------------------
    # CONTRACTOR NOTIFICATION
    # -----------------------------------

    st.header("Contractor Notification")

    st.write(contractor_msg)

    # -----------------------------------
    # HISTORY TABLE
    # -----------------------------------

    st.header("Vehicle & Bridge History")

    history_df = pd.DataFrame(st.session_state.history)

    st.dataframe(history_df)

    # -----------------------------------
    # AI HISTORY ANALYSIS
    # -----------------------------------

    st.header("AI Historical Analysis")

    safe_count = len(history_df[history_df["Condition"] == "SAFE"])

    warning_count = len(history_df[history_df["Condition"] == "WARNING"])

    danger_count = len(history_df[history_df["Condition"] == "DANGER"])

    st.write(f"Safe Records: {safe_count}")
    st.write(f"Warning Records: {warning_count}")
    st.write(f"Danger Records: {danger_count}")

    if danger_count >= 3:

        st.error("AI predicts increasing structural risk based on history.")

    elif warning_count >= 3:

        st.warning("AI predicts future maintenance may be required.")

    else:

        st.success("AI predicts bridge stability is good.")

else:

    st.info("Click 'Generate New Vehicle Data' to begin monitoring.")