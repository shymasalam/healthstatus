from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.visualization import visualize_data
from src.feature_engineering import feature_engineering
from src.transformation import transform_data
from src.feature_selection import select_features
from src.model_training import train_model
from src.model_evaluation import evaluate_model


def main():

    data = load_data()

    data = clean_data(data)

    visualize_data(data)

    data = feature_engineering(data)

    data = transform_data(data)

    X, y = select_features(data)

    model, X_test, y_test = train_model(
        X,
        y
    )

    evaluate_model(
        model,
        X_test,
        y_test
    )

    print("\nProject Completed Successfully")


if __name__ == "__main__":
    main()

import streamlit as st
import pandas as pd
import joblib

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Health Status Predictor",
    page_icon="🏥",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.stApp{
    background-color:#000000;
    color:white;
}

/* Metric Cards */
[data-testid="stMetric"]{
    background-color:#111111;
    border:1px solid #333333;
    border-radius:15px;
    padding:15px;
}

/* Input Boxes */
.stNumberInput input{
    background-color:#1a1a1a;
    color:white;
}

/* Button */
.stButton > button{
    background:linear-gradient(90deg,#16a34a,#06b6d4);
    color:white;
    border:none;
    border-radius:10px;
    font-size:18px;
    font-weight:bold;
    padding:10px 20px;
}

.stButton > button:hover{
    background:linear-gradient(90deg,#22c55e,#0891b2);
}

</style>
""", unsafe_allow_html=True)

# =====================================
# LOAD MODEL
# =====================================

model = joblib.load("health_status_model.pkl")

# =====================================
# HEADER
# =====================================

st.markdown("""
<div style="
background: linear-gradient(135deg,#10b981,#06b6d4);
padding:30px;
border-radius:20px;
text-align:center;
color:white;
box-shadow:0px 0px 20px rgba(16,185,129,0.5);">

<h1>🏥 Health Status Prediction System</h1>

<h4>
AI-Powered Healthcare Analytics Dashboard
</h4>

</div>
""", unsafe_allow_html=True)

st.write("")

# =====================================
# INPUT SECTION
# =====================================

st.markdown("""
<div style="
background:#111111;
padding:15px;
border-radius:15px;
border:1px solid #333333;">

<h3>🩺 Enter Health Information</h3>

</div>
""", unsafe_allow_html=True)

st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "👤 Age",
        min_value=1,
        max_value=120,
        value=25
    )

    bmi = st.number_input(
        "⚖️ BMI",
        value=22.0
    )

with col2:
    weight = st.number_input(
        "🏋️ Weight (kg)",
        value=60.0
    )

    height = st.number_input(
        "📏 Height (cm)",
        value=170.0
    )

with col3:
    daily_calories = st.number_input(
        "🍽 Daily Calories Consumed",
        value=2000.0
    )

# =====================================
# LIVE DASHBOARD
# =====================================

m1, m2, m3 = st.columns(3)

m1.metric("Age", age)
m2.metric("BMI", bmi)
m3.metric("Calories", daily_calories)

# =====================================
# HEALTH SCORE
# =====================================

health_score = max(
    0,
    min(
        100,
        int(100 - abs(bmi - 22) * 4)
    )
)

st.metric(
    "💚 Health Score",
    f"{health_score}/100"
)

# =====================================
# BMI STATUS
# =====================================

st.subheader("BMI Status")

if bmi < 18.5:
    st.info("🔵 Underweight")

elif bmi < 25:
    st.success("🟢 Normal Weight")

elif bmi < 30:
    st.warning("🟠 Overweight")

else:
    st.error("🔴 Obese")

# =====================================
# PREDICT BUTTON
# =====================================

if st.button("🔍 Predict Health Status"):

    calorie_balance = 0

    input_data = pd.DataFrame({
        "Age":[age],
        "BMI":[bmi],
        "Weight_kg":[weight],
        "Height_cm":[height],
        "Daily_Calorie_Consumed":[daily_calories],
        "Calorie_Balance":[calorie_balance]
    })

    prediction = model.predict(input_data)[0]

    st.write("")

    # =================================
    # HEALTHY
    # =================================

    if prediction == 0:

        st.markdown("""
        <div style="
        background:linear-gradient(90deg,#16a34a,#22c55e);
        padding:25px;
        border-radius:15px;
        text-align:center;
        color:white;">

        <h1>✅ HEALTHY</h1>

        <h4>
        Keep maintaining your healthy lifestyle.
        </h4>

        </div>
        """, unsafe_allow_html=True)

    # =================================
    # MODERATE
    # =================================

    elif prediction == 1:

        st.markdown("""
        <div style="
        background:linear-gradient(90deg,#f59e0b,#fbbf24);
        padding:25px;
        border-radius:15px;
        text-align:center;
        color:white;">

        <h1>⚠️ MODERATE</h1>

        <h4>
        Your health needs some attention.
        </h4>

        </div>
        """, unsafe_allow_html=True)

    # =================================
    # UNHEALTHY
    # =================================

    else:

        st.markdown("""
        <div style="
        background:linear-gradient(90deg,#dc2626,#ef4444);
        padding:25px;
        border-radius:15px;
        text-align:center;
        color:white;">

        <h1>❌ UNHEALTHY</h1>

        <h4>
        Please improve nutrition and lifestyle habits.
        </h4>

        </div>
        """, unsafe_allow_html=True)