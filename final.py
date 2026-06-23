import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Health Status Predictor",
    page_icon="🏥",
    layout="wide"
)

# =====================================
# CLEAN UI STYLING
# =====================================

st.markdown("""
<style>

.stApp{
    background:#f8fafc;
}

[data-testid="stSidebar"]{
    background:white;
    border-right:1px solid #e5e7eb;
}

[data-testid="metric-container"]{
    background:white;
    border:1px solid #e5e7eb;
    border-radius:12px;
    padding:15px;
}

.stButton > button{
    width:100%;
    height:50px;
    border:none;
    border-radius:10px;
    background:#2563eb;
    color:white;
    font-weight:600;
}

.stButton > button:hover{
    background:#1d4ed8;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:
    st.title("🏥 Health AI")
    st.caption("Healthcare Analytics Dashboard")
    st.success("🟢 System Online")

# =====================================
# LOAD MODEL
# =====================================

model = joblib.load("artifacts/models/health_status_model.pkl")

# =====================================
# HEADER
# =====================================

st.title("🏥 Health Status Predictor")
st.caption("AI-Powered Healthcare Assessment Dashboard")

st.divider()

# =====================================
# KPI METRICS
# =====================================

c1, c2, c3, c4 = st.columns(4)

c1.metric("Accuracy", "98%")
c2.metric("Speed", "<1 sec")
c3.metric("Records", "1200+")
c4.metric("Status", "Online")

st.write("")

# =====================================
# INPUT SECTION
# =====================================

st.subheader("🩺 Patient Information")

left, right = st.columns([2, 1])

with left:

    age = st.number_input("Age", 1, 120, 25)
    weight = st.number_input("Weight (kg)", 60.0)
    height = st.number_input("Height (cm)", 170.0)
    bmi = st.number_input("BMI", 22.0)
    daily_calories = st.number_input("Daily Calories", 2000.0)

with right:

    st.subheader("Live Summary")
    st.metric("Age", age)
    st.metric("BMI", bmi)
    st.metric("Weight", weight)
    st.metric("Calories", daily_calories)

# =====================================
# HEALTH SCORE
# =====================================

health_score = max(0, min(100, int(100 - abs(bmi - 22) * 4)))

st.metric("💚 Health Score", f"{health_score}/100")

# =====================================
# PREDICTION
# =====================================

if st.button("🔍 Predict Health Status"):

    calorie_balance = 0

    input_data = pd.DataFrame({
        "Age": [age],
        "BMI": [bmi],
        "Weight_kg": [weight],
        "Height_cm": [height],
        "Daily_Calorie_Consumed": [daily_calories],
        "Calorie_Balance": [calorie_balance]
    })

    prediction = model.predict(input_data)[0]

    # =====================================
    # RESULT
    # =====================================

    if prediction == 0:
        health_status = "HEALTHY"
        st.success("✅ HEALTHY")

    elif prediction == 1:
        health_status = "MODERATE"
        st.warning("⚠️ MODERATE")

    else:
        health_status = "UNHEALTHY"
        st.error("❌ UNHEALTHY")

    # =====================================
    # PATIENT SUMMARY
    # =====================================

    summary = pd.DataFrame({
        "Parameter": ["Age", "Weight", "Height", "BMI", "Calories"],
        "Value": [age, weight, height, bmi, daily_calories]
    })

    st.subheader("👤 Patient Summary")
    st.dataframe(summary, use_container_width=True, hide_index=True)

    # =====================================
    # BMI STATUS
    # =====================================

    if bmi < 18.5:
        bmi_status = "Underweight"

    elif bmi < 25:
        bmi_status = "Normal Weight"

    elif bmi < 30:
        bmi_status = "Overweight"

    else:
        bmi_status = "Obese"

    st.info(f"BMI Status: {bmi_status}")

    # =====================================
    # HEALTH RISK GAUGE
    # =====================================

    risk = 100 - health_score

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk,
        title={"text": "Health Risk"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#2563eb"},
            "steps": [
                {"range": [0, 30], "color": "#dcfce7"},
                {"range": [30, 70], "color": "#fef3c7"},
                {"range": [70, 100], "color": "#fee2e2"}
            ]
        }
    ))

    fig.update_layout(height=300)

    st.plotly_chart(fig, use_container_width=True)

    # =====================================
    # RECOMMENDATIONS
    # =====================================

    st.subheader("💡 Recommendations")

    recommendations = []

    if bmi > 25:
        recommendations.append("🏃 Increase physical activity and diet control.")

    if bmi < 18.5:
        recommendations.append("🍎 Improve nutrition and calorie intake.")

    if daily_calories > 2500:
        recommendations.append("🔥 Reduce daily calorie intake.")

    if len(recommendations) == 0:
        recommendations.append("✅ Maintain healthy lifestyle.")

    for rec in recommendations:
        st.info(rec)

    # =====================================
    # DOWNLOAD REPORT
    # =====================================

    report = f"""
HEALTH REPORT

Age: {age}
Weight: {weight}
Height: {height}
BMI: {bmi}
Calories: {daily_calories}

Health Score: {health_score}
Prediction: {prediction}
BMI Status: {bmi_status}
Risk: {risk}%
"""

    st.download_button(
        "📄 Download Report",
        report,
        file_name="health_report.txt"
    )

# =====================================
# FOOTER
# =====================================

st.markdown("""
---
<center style='color:gray;'>
🏥 Health Status Prediction System © 2026
</center>
""", unsafe_allow_html=True)