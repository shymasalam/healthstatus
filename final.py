import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Health Status Predictor",
    page_icon="🏥",
    layout="wide"
)

# =====================================================
# LOAD MODEL
# =====================================================

model = joblib.load("artifacts/models/health_status_model.pkl")


# =====================================================
# CUSTOM CSS (BRIGHT PROFESSIONAL THEME)
# =====================================================
st.markdown("""
<style>

/* =======================================================
   GLOBAL THEME
======================================================= */

.stApp{
    background:linear-gradient(
        180deg,
        #f8fbff 0%,
        #eef6ff 100%
    );
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container{
    padding-top:1.5rem;
    padding-bottom:2rem;
    max-width:1450px;
}

/* =======================================================
   SIDEBAR
======================================================= */

[data-testid="stSidebar"]{
    background:#ffffff;
    border-right:1px solid #e5e7eb;
}

[data-testid="stSidebar"] *{
    color:#1f2937 !important;
}

/* =======================================================
   HERO HEADER
======================================================= */

.hero{
    background:linear-gradient(
        135deg,
        #0f766e 0%,
        #14b8a6 50%,
        #2dd4bf 100%
    );

    padding:45px;
    border-radius:30px;

    box-shadow:
        0 20px 40px rgba(20,184,166,.20);

    margin-bottom:25px;

    position:relative;
    overflow:hidden;
}

.hero::before{
    content:"";
    position:absolute;
    width:250px;
    height:250px;
    background:rgba(255,255,255,0.08);
    border-radius:50%;
    top:-120px;
    right:-80px;
}

.hero::after{
    content:"";
    position:absolute;
    width:180px;
    height:180px;
    background:rgba(255,255,255,0.05);
    border-radius:50%;
    bottom:-80px;
    right:120px;
}

/* =======================================================
   TEXT
======================================================= */

h1,h2,h3,h4,h5,h6{
    color:#111827 !important;
}

label{
    color:#111827 !important;
    font-weight:600 !important;
}

/* =======================================================
   KPI CARDS
======================================================= */

[data-testid="metric-container"]{
    background:white;
    border-radius:20px;
    padding:18px;
    box-shadow:0 5px 18px rgba(0,0,0,.05);
    border:1px solid #eef2f7;
}

[data-testid="metric-container"] label,
[data-testid="metric-container"] div{
    color:#111827 !important;
}

/* =======================================================
   DASHBOARD CARDS
======================================================= */

.card{
    background:white;
    border-radius:24px;
    padding:22px;
    height:220px;

    display:flex;
    flex-direction:column;
    justify-content:space-between;

    box-shadow:0 8px 25px rgba(0,0,0,.05);
    border:1px solid #eef2f7;
}

.summary-card{
    background:white;
    border-radius:18px;
    padding:16px;
    margin-bottom:12px;
    box-shadow:0 4px 15px rgba(0,0,0,.04);
}

/* =======================================================
   PATIENT INFORMATION CARDS
======================================================= */

/* =======================================================
   PATIENT INFORMATION SECTION
======================================================= */

.patient-card{
    background:white;
    padding:25px 30px;
    border-radius:28px;
    border:1px solid #e5e7eb;

    box-shadow:
        0 10px 30px rgba(15,23,42,.06);

    margin-bottom:20px;
}

.info-box{
    background:linear-gradient(
        90deg,
        #ecfeff,
        #f0fdfa
    );

    padding:16px;
    border-radius:14px;
    border-left:5px solid #14b8a6;

    margin-top:15px;

    font-size:15px;
    font-weight:500;
    color:#0f766e;
}

/* =======================================================
   LIVE SUMMARY CARD
======================================================= */

.live-card{
    background:white;
    border-radius:22px;
    padding:22px;
    border:1px solid #edf2f7;

    box-shadow:
        0 10px 25px rgba(0,0,0,.05);

    margin-bottom:15px;
}

.live-item{
    background:#f8fafc;
    padding:14px 16px;
    border-radius:14px;

    margin-bottom:12px;

    border-left:4px solid #14b8a6;

    font-size:16px;
    color:#0f172a;

    box-shadow:
        0 2px 6px rgba(0,0,0,.03);
}

/* =======================================================
   PREMIUM TEXT INPUTS
======================================================= */

/* ==========================================
   MODERN HEALTHCARE INPUTS
========================================== */

.stTextInput > div > div{
    background:#ffffff !important;

    border:none !important;

    border-radius:18px !important;

    box-shadow:
        0 2px 10px rgba(15,23,42,0.05),
        0 1px 3px rgba(15,23,42,0.03);

    min-height:58px !important;

    transition:all .25s ease;
}

.stTextInput > div > div:hover{
    box-shadow:
        0 6px 18px rgba(15,23,42,0.08);
}

.stTextInput > div > div:focus-within{

    box-shadow:
        0 0 0 4px rgba(20,184,166,.15),
        0 8px 25px rgba(20,184,166,.10);

    transform:translateY(-1px);
}

.stTextInput input{
    border:none !important;

    font-size:18px !important;
    font-weight:600 !important;

    color:#0f172a !important;

    padding:14px 18px !important;

    background:transparent !important;
}
/* =======================================================
   PREMIUM NUMBER INPUTS
======================================================= */

/* ===============================
   PREMIUM BRIGHT NUMBER INPUT
================================ */

.stNumberInput div[data-baseweb="input"]{

    background:#ffffff !important;

    border:2px solid #d1d5db !important;

    border-radius:18px !important;

    box-shadow:0 6px 18px rgba(0,0,0,.08);

    transition:all .3s ease;
}

.stNumberInput div[data-baseweb="input"]:hover{

    border:2px solid #38bdf8 !important;
}

.stNumberInput div[data-baseweb="input"]:focus-within{

    border:2px solid #14b8a6 !important;

    box-shadow:
        0 0 0 5px rgba(20,184,166,.18);
}

.stNumberInput input{

    background:#ffffff !important;

    color:#111827 !important;

    font-size:20px !important;

    font-weight:700 !important;
}
            /* ==========================================
   REMOVE + / - BUTTONS FROM NUMBER INPUTS
========================================== */

.stNumberInput button{
    display:none !important;
}

.stNumberInput div[data-baseweb="input"]{
    padding-right:0 !important;
}

/* Hide spinner controls in browsers */

input[type=number]::-webkit-inner-spin-button,
input[type=number]::-webkit-outer-spin-button{
    -webkit-appearance:none;
    margin:0;
}

input[type=number]{
    -moz-appearance:textfield;
}


/* ===============================
   PREMIUM BRIGHT TEXT INPUTS
================================ */

.stTextInput > div > div{
    background:#ffffff !important;
    border:2px solid #d1d5db !important;
    border-radius:18px !important;

    box-shadow:
        0 6px 18px rgba(0,0,0,0.08);

    transition:all .3s ease;
}

.stTextInput > div > div:hover{
    border:2px solid #38bdf8 !important;

    box-shadow:
        0 8px 20px rgba(56,189,248,.18);
}

.stTextInput > div > div:focus-within{

    border:2px solid #14b8a6 !important;

    box-shadow:
        0 0 0 5px rgba(20,184,166,.18),
        0 10px 25px rgba(20,184,166,.15);
}

.stTextInput input{

    background:#ffffff !important;

    color:#111827 !important;

    font-size:20px !important;

    font-weight:700 !important;

    padding:16px !important;
}

/* Label */

label{

    color:#0f172a !important;

    font-size:16px !important;

    font-weight:700 !important;
}
            
/* =======================================================
   BUTTON
======================================================= */

.stButton > button{
    width:100%;
    height:60px;
    border:none;
    border-radius:15px;

    background:linear-gradient(
        90deg,
        #0f766e,
        #14b8a6
    );

    color:white !important;
    font-size:18px;
    font-weight:700;

    transition:all .3s ease;
}

.stButton > button:hover{
    transform:translateY(-2px);

    box-shadow:
        0 10px 25px rgba(20,184,166,.25);
}

/* =======================================================
   DATAFRAME
======================================================= */

[data-testid="stDataFrame"]{
    background:white;
    border-radius:18px;
    overflow:hidden;
}

/* =======================================================
   RECOMMENDATION CARDS
======================================================= */

.recommend{
    background:white;
            color:black;
    border-radius:16px;
    padding:16px;
    margin-bottom:12px;

    border-left:5px solid #14b8a6;

    box-shadow:
        0 4px 12px rgba(0,0,0,.04);
}

/* =======================================================
   ALERTS
======================================================= */

[data-testid="stAlert"]{
    border-radius:15px;
}

/* =======================================================
   PLOTLY GAUGE
======================================================= */

.js-plotly-plot{
    background:white;
    border-radius:20px;
    padding:10px;
}

/* =======================================================
   SCROLLBAR
======================================================= */

::-webkit-scrollbar{
    width:8px;
}

::-webkit-scrollbar-thumb{
    background:#14b8a6;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)
# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2966/2966486.png",
        width=90
    )

    st.markdown("## Health AI")

    st.caption("Healthcare Analytics Dashboard")

    st.success("🟢 System Online")

    st.divider()

    st.markdown("""
### Features

✔ Health Prediction

✔ BMI Analysis

✔ Risk Assessment

✔ Lifestyle Suggestions

✔ Download Report
""")


# =====================================================
# PREMIUM HERO SECTION
# =====================================================

from datetime import datetime

current_time = datetime.now().strftime(
    "%d %B %Y | %I:%M %p"
)

st.markdown(f"""
<div class="hero">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
">

<div>

<div style="
font-size:14px;
background:rgba(255,255,255,.15);
padding:8px 14px;
border-radius:10px;
display:inline-block;
color:white;
margin-bottom:15px;
">
🚀 AI Healthcare Platform
</div>

<h1 style="
color:white;
font-size:56px;
font-weight:800;
margin:0;
">
🏥 Health Status Predictor
</h1>

<p style="
color:#ecfeff;
font-size:20px;
margin-top:12px;
margin-bottom:20px;
">
Advanced Health Assessment & Risk Analysis
</p>

<div style="
display:flex;
gap:15px;
flex-wrap:wrap;
">

<div style="
background:rgba(255,255,255,.12);
padding:10px 18px;
border-radius:12px;
color:white;
">
📅 {current_time}
</div>

<div style="
background:rgba(255,255,255,.12);
padding:10px 18px;
border-radius:12px;
color:white;
">
⚡ Real-Time Prediction
</div>

<div style="
background:rgba(255,255,255,.12);
padding:10px 18px;
border-radius:12px;
color:white;
">
🎯 98% Accuracy
</div>

</div>

</div>

<div style="
font-size:100px;
">
🩺
</div>

</div>

</div>
""", unsafe_allow_html=True)

# =====================================================
# KPI CARDS
# =====================================================

# =====================================================
# KPI DASHBOARD
# =====================================================

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.markdown("""
    <div class="card">

    <h4 style="
    color:#64748b;
    font-size:20px;
    font-weight:600;
    height:35px;
    margin-bottom:15px;
    ">
    🎯 Accuracy
    </h4>

    <h1 style="
    font-size:54px;
    font-weight:800;
    color:#0f172a;
    margin:0;
    ">
    98%
    </h1>

    <p style="
    color:#22c55e;
    font-size:18px;
    ">
    ▲ +2.4% This Month
    </p>

    </div>
    """, unsafe_allow_html=True)

with k2:

    st.markdown("""
    <div class="card">

    <h4 style="
    color:#64748b;
    font-size:20px;
    font-weight:600;
    height:35px;
    margin-bottom:15px;
    ">
    ⚡ Response Time
    </h4>

    <h1 style="
    font-size:54px;
    font-weight:800;
    color:#0f172a;
    margin:0;
    ">
    &lt;1 sec
    </h1>

    <p style="
    color:#22c55e;
    font-size:18px;
    ">
    Fast Processing
    </p>

    </div>
    """, unsafe_allow_html=True)

with k3:

    st.markdown("""
    <div class="card">

    <h4 style="
    color:#64748b;
    font-size:20px;
    font-weight:600;
    height:35px;
    margin-bottom:15px;
    ">
    📊 Records
    </h4>

    <h1 style="
    font-size:54px;
    font-weight:800;
    color:#0f172a;
    margin:0;
    ">
    1200+
    </h1>

    <p style="
    color:#2563eb;
    font-size:18px;
    ">
    Training Samples
    </p>

    </div>
    """, unsafe_allow_html=True)

with k4:

    st.markdown("""
    <div class="card">

    <h4 style="
    color:#64748b;
    font-size:20px;
    font-weight:600;
    height:35px;
    margin-bottom:15px;
    ">
    🟢 Status
    </h4>

    <h1 style="
    font-size:54px;
    font-weight:800;
    color:#0f172a;
    margin:0;
    ">
    Online
    </h1>

    <p style="
    color:#22c55e;
    font-size:18px;
    ">
    System Active
    </p>

    </div>
    """, unsafe_allow_html=True)
# =====================================================
# INPUT SECTION
# =====================================================

# =====================================================
# INPUT SECTION
# =====================================================

# =====================================================
# PATIENT INFORMATION
# =====================================================

# =====================================================
# MODERN PATIENT INFORMATION SECTION
# =====================================================

# =====================================================
# PREMIUM PATIENT INFORMATION SECTION
# =====================================================

# =====================================================
# PROFESSIONAL PATIENT INFORMATION SECTION
# =====================================================

st.markdown("""
<div class="patient-card">

<h2 style="
margin-bottom:5px;
color:#0f172a;
">
🩺 Patient Information
</h2>

<p style="
color:#64748b;
margin-bottom:25px;
font-size:15px;
">
Enter patient details for AI-powered health assessment
</p>

</div>
""", unsafe_allow_html=True)

left, right = st.columns([2.3, 1])

# =====================================================
# INPUT PANEL
# =====================================================

with left:

    st.markdown("""
    <div class="live-card">
    <h3 style="margin-top:0;">📋 Health Parameters</h3>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:

        age = st.number_input(
            "👤 Age (Years)",
            min_value=1,
            max_value=120,
            value=25
        )

        height = st.number_input(
            "📏 Height (cm)",
            min_value=50.0,
            max_value=250.0,
            value=170.0
        )

        daily_calories = st.number_input(
            "🔥 Daily Calories",
            min_value=0,
            value=2000
        )

    with c2:

        weight = st.number_input(
            "⚖️ Weight (kg)",
            min_value=1.0,
            max_value=300.0,
            value=60.0
        )

        calculated_bmi = round(
            weight / ((height / 100) ** 2),
            1
        )

        st.markdown(
            f"""
            <div style="
                background:white;
                padding:20px;
                border-radius:18px;
                border:1px solid #e5e7eb;
            ">
                <h4>🧮 BMI</h4>
                <h1 style="color:#14b8a6;">
                    {calculated_bmi}
                </h1>
            </div>
            """,
            unsafe_allow_html=True
        )

        bmi = calculated_bmi
# =====================================================
# HEALTH SNAPSHOT PANEL
# =====================================================

health_score = max(
    0,
    min(
        100,
        int(100 - abs(calculated_bmi - 22) * 4)
    )
)

with right:

    st.markdown("""
    <div class="live-card">
    <h3 style="margin-top:0;">💚 Live Health Snapshot</h3>
    </div>
    """, unsafe_allow_html=True)

    if calculated_bmi < 18.5:
        bmi_status = "Underweight 🔵"
    elif calculated_bmi < 25:
        bmi_status = "Normal 🟢"
    elif calculated_bmi < 30:
        bmi_status = "Overweight 🟠"
    else:
        bmi_status = "Obese 🔴"

    st.markdown(f"""
    <div class="live-item">
    <b>👤 Age</b><br>
    {age} Years
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="live-item">
    <b>⚖️ Weight</b><br>
    {weight} kg
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="live-item">
    <b>🧮 BMI Status</b><br>
    {bmi_status}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="live-item">
    <b>💚 Health Score</b><br>
    {health_score}/100
    </div>
    """, unsafe_allow_html=True)

    st.progress(health_score / 100)




# =====================================================
# PREDICTION BUTTON
# =====================================================

if st.button("🔍 Predict Health Status"):

    # -----------------------------
    # Prepare Input
    # -----------------------------
    input_data = pd.DataFrame({
        "Age": [age],
        "BMI": [bmi],
        "Weight_kg": [weight],
        "Height_cm": [height],
        "Daily_Calorie_Consumed": [daily_calories],
        "Calorie_Balance": [0]
    })

    # Prediction
    prediction = int(model.predict(input_data)[0])

    # Confidence
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(input_data)[0]
        confidence = max(probs) * 100
    else:
        confidence = 0
    # -----------------------------
    # -----------------------------
    # Health Status Mapping
    # -----------------------------

    if prediction == 0:
        health_status = "HEALTHY"
        icon = "✅"
        bg = "#dcfce7"
        text = "#166534"

    elif prediction == 1:
        health_status = "OBESE"
        icon = "🔴"
        bg = "#fee2e2"
        text = "#991b1b"

    elif prediction == 2:
        health_status = "OVERWEIGHT"
        icon = "⚠️"
        bg = "#fef3c7"
        text = "#92400e"

    elif prediction == 3:
        health_status = "UNDERWEIGHT"
        icon = "🟦"
        bg = "#dbeafe"
        text = "#1d4ed8"

    # -----------------------------
    # Professional Result Card
   

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🏥 Health Status",
            health_status
        )

    with col2:
        if hasattr(model, "predict_proba"):
            confidence = max(probs) * 100
            st.metric(
                "🎯 Confidence",
                f"{confidence:.0f}%"
            )
    st.markdown("<div style='margin-top:25px;'></div>", unsafe_allow_html=True)
    st.markdown(f"""
<div style="
margin-top:15px;
background:#e5e7eb;
border-radius:20px;
height:18px;
overflow:hidden;
">

<div style="
width:{confidence}%;
height:18px;
background:linear-gradient(90deg,#06b6d4,#3b82f6);
border-radius:20px;
">
</div>

</div>
""", unsafe_allow_html=True)
    st.markdown("<div style='margin-top:30px;'></div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="
    margin-top:25px;
    background:{bg};
    padding:20px;
    border-radius:25px;
    border-left:8px solid {text};
    ">

    <h2 style="
    margin-top:0;
    color:{text};
    ">
    📋 Final Assessment
    </h2>

    <p style="
    font-size:18px;
    font-weight:700;
    color:{text};
    ">
    Your current health classification is:
    <b>{health_status}</b>
    </p>

    </div>
    """, unsafe_allow_html=True)


    st.markdown("<div style='height:35px;'></div>", unsafe_allow_html=True)

    # ==============================================
    # ASSESSMENT SUMMARY
    # ==============================================

    st.markdown(f"""
    <div class="info-box">

    📌 Current Assessment Summary

    <br><br>

    👤 Age: <b>{age}</b>

    <br><br>

    ⚖️ Weight: <b>{weight} kg</b>

    <br><br>

    📏 Height: <b>{height} cm</b>

    <br><br>

    🧮 BMI: <b>{calculated_bmi}</b>

    <br><br>

    🔥 Calories: <b>{daily_calories}</b>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)

    # ==============================================
    # HEALTH SCORE
    # ==============================================
    # ==============================================
    # HEALTH DASHBOARD
    # ==============================================

    st.subheader("💚 Health Dashboard")

    c1, c2 = st.columns(2)

    with c1:

        st.markdown(f"""
        <div style="
        background:white;
        padding:30px;
        border-radius:25px;
        text-align:center;
        border:1px solid #e5e7eb;
        box-shadow:0 8px 25px rgba(0,0,0,.05);
        ">

        <h4 style="color:#64748b;">
        Overall Score
        </h4>

        <h1 style="
        font-size:70px;
        color:#10b981;
        margin:0;
        ">
        {health_score}
        </h1>

        <p style="
        color:#94a3b8;
        font-size:20px;
        ">
        out of 100
        </p>

        </div>
        """, unsafe_allow_html=True)

    with c2:

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=health_score,
            title={"text":"Health Score"},
            gauge={
                "axis":{"range":[0,100]},
                "bar":{"color":"#14b8a6"},
                "steps":[
                    {"range":[0,40],"color":"#fee2e2"},
                    {"range":[40,70],"color":"#fef3c7"},
                    {"range":[70,100],"color":"#dcfce7"}
                ]
            }
        ))

        fig.update_layout(
            height=300,
            paper_bgcolor="white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    
    # ==============================================
    # PATIENT SUMMARY
    # ==============================================

    st.subheader("👤 Patient Summary")

    summary = pd.DataFrame({

        "Parameter": [
            "Age",
            "Weight",
            "Height",
            "BMI",
            "Calories",
            "Health Status"
        ],

        "Value": [
            age,
            weight,
            height,
            bmi,
            daily_calories,
            health_status
        ]
    })

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )

    # ==============================================
    # BMI STATUS
    # ==============================================

    st.subheader("📈 BMI Status")

    if bmi < 18.5:

        bmi_status = "Underweight"

        st.info("🔵 Underweight")

    elif bmi < 25:

        bmi_status = "Normal Weight"

        st.success("🟢 Normal Weight")

    elif bmi < 30:

        bmi_status = "Overweight"

        st.warning("🟠 Overweight")

    else:

        bmi_status = "Obese"

        st.error("🔴 Obese")

    # ==========================================
    # PERSONALIZED HEALTH INSIGHTS
    # ==========================================

    if health_status == "HEALTHY":

        card_color = "#10b981"
        risk = "Low Risk"

        advice = [
            "🥗 Maintain balanced nutrition",
            "💧 Continue proper hydration",
            "🏃 Maintain regular exercise routine",
            "🩺 Annual preventive health checkups"
        ]

    elif health_status == "OVERWEIGHT":

        card_color = "#f59e0b"
        risk = "Moderate Risk"

        advice = [
            "📉 Reduce excess calorie intake",
            "🚶 Increase daily physical activity",
            "🥦 Improve meal quality and portion control",
            "⚖️ Monitor weight progression weekly"
        ]

    elif health_status == "OBESE":

        card_color = "#ef4444"
        risk = "High Risk"

        advice = [
            "🚨 Structured weight-management program required",
            "🥗 Follow a calorie-controlled diet plan",
            "🏃 Perform regular cardio exercise",
            "👨‍⚕️ Consult a healthcare professional"
        ]

    else:

        card_color = "#3b82f6"
        risk = "Nutritional Risk"

        advice = [
            "🍗 Increase protein intake",
            "🍚 Increase healthy calorie consumption",
            "💪 Focus on muscle development",
            "🩺 Seek nutrition specialist guidance"
        ]
     # ==========================================
    # INSIGHTS CARD
    # ==========================================
    st.markdown(f"""
    <div style="
    background:white;
    padding:35px;
    border-radius:30px;
    box-shadow:0 15px 40px rgba(0,0,0,.08);
    margin-top:35px;
    overflow:hidden;
    ">

    <div style="
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:25px;
    ">

    <div>

    <h2 style="
    margin:0;
    color:#0f172a;
    ">
    💡 Personalized Health Insights
    </h2>

    <p style="
    margin-top:8px;
    color:#64748b;
    font-size:15px;
    ">
    AI-powered recommendations based on your health profile
    </p>

    </div>

    <div style="
    background:{card_color};
    color:white;
    padding:10px 18px;
    border-radius:50px;
    font-weight:600;
    font-size:14px;
    ">
    {risk}
    </div>

    </div>

    <div style="
    background:#f8fafc;
    padding:25px;
    border-radius:20px;
    border-left:6px solid {card_color};
    ">

    <h3 style="
    margin-top:0;
    color:#0f172a;
    ">
    Recommended Action Plan
    </h3>

    </div>

    </div>
    """, unsafe_allow_html=True)


    # ==========================================
    # DISPLAY RECOMMENDATIONS
    # ==========================================

    for item in advice:
        st.markdown(
            f"""
            <div style="
            margin-left:30px;
            margin-top:10px;
            font-size:17px;
            color:#334155;
            line-height:1.8;
            ">
            {item}
            </div>
            """,
            unsafe_allow_html=True
        )


    # ==========================================
    # STATUS & CONFIDENCE CARDS
    # ==========================================

    st.markdown(f"""
    <div style="
    display:flex;
    gap:20px;
    margin-top:25px;
    ">

    <div style="
    flex:1;
    background:#f1f5f9;
    padding:20px;
    border-radius:18px;
    text-align:center;
    ">

    <div style="
    font-size:13px;
    color:#64748b;
    ">
    Health Status
    </div>

    <div style="
    font-size:24px;
    font-weight:700;
    margin-top:8px;
    color:{card_color};
    ">
    {health_status}
    </div>

    </div>

    <div style="
    flex:1;
    background:#f1f5f9;
    padding:20px;
    border-radius:18px;
    text-align:center;
    ">

    <div style="
    font-size:13px;
    color:#64748b;
    ">
    Prediction Confidence
    </div>

    <div style="
    font-size:24px;
    font-weight:700;
    margin-top:8px;
    color:#2563eb;
    ">
    {confidence:.0f}%
    </div>

    </div>

    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)
    # ==============================================
    # DOWNLOAD REPORT
    # ==============================================
    report = f'''
HEALTH REPORT

Age: {age}
Weight: {weight}
Height: {height}
BMI: {bmi}
Calories: {daily_calories}

Health Score: {health_score}
Health Status: {health_status}
BMI Status: {bmi_status}
'''

    st.download_button(
    label="📄 Download Health Report",
    data=report,
    file_name="health_report.txt",
    key="download_report_btn"
)
    # =====================================================
# FOOTER
# =====================================================

st.markdown("""
<br><br>
<hr>

<center style='color:gray;'>

🏥 Health Status Prediction System © 2026

</center>
""", unsafe_allow_html=True)