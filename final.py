import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px

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
    background:
    radial-gradient(circle at top left,#0ea5e9 0%,transparent 25%),
    radial-gradient(circle at bottom right,#8b5cf6 0%,transparent 25%),
    #020617;
}

.stApp::before{
    content:'';
    position:fixed;
    width:500px;
    height:500px;
    border-radius:50%;
    background:#06b6d4;
    filter:blur(200px);
    opacity:0.15;
    top:-150px;
    left:-100px;
    z-index:-1;
}

.stApp::after{
    content:'';
    position:fixed;
    width:500px;
    height:500px;
    border-radius:50%;
    background:#8b5cf6;
    filter:blur(220px);
    opacity:0.15;
    bottom:-150px;
    right:-100px;
    z-index:-1;
}

</style>
""", unsafe_allow_html=True)
# =====================================
# LOAD MODEL
# =====================================

model = joblib.load(
    "artifacts/models/health_status_model.pkl"
)

# Load Label Encoder
encoder = joblib.load(
    "artifacts/models/label_encoder.pkl"
)

# =====================================
# PREMIUM HEADER
# =====================================

st.markdown("""
<div style="
background:linear-gradient(135deg,#07122b,#111f46,#2d1064);
padding:50px;
border-radius:30px;
text-align:center;
border:1px solid rgba(255,255,255,0.12);
box-shadow:0px 15px 40px rgba(0,0,0,0.45);
margin-bottom:25px;
position:relative;
overflow:hidden;
">

<!-- Hospital Icon -->
<div style="
width:120px;
height:120px;
margin:auto;
margin-bottom:25px;
border-radius:50%;
background:rgba(255,255,255,0.08);
backdrop-filter:blur(15px);
border:2px solid rgba(255,255,255,0.15);
display:flex;
align-items:center;
justify-content:center;
font-size:55px;
box-shadow:
0 0 20px rgba(56,189,248,0.4),
0 0 40px rgba(139,92,246,0.3);
">

🏥

</div>

<h1 style="
font-size:80px;
font-weight:900;
margin-bottom:15px;
background:linear-gradient(
90deg,
#38bdf8,
#22c55e,
#a855f7);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
letter-spacing:-2px;
">
Health Status Predictor
</h1>

<h3 style="
color:#cbd5e1;
letter-spacing:2px;
margin-bottom:30px;">
Next Generation AI Healthcare Analytics
</h3>

<div style="
display:flex;
justify-content:center;
gap:18px;
flex-wrap:wrap;">

<span style="
background:rgba(16,185,129,0.15);
border:1px solid rgba(16,185,129,0.4);
padding:12px 24px;
border-radius:40px;
color:#4ade80;
font-weight:700;
font-size:18px;">
🟢 Online
</span>

<span style="
background:rgba(14,165,233,0.15);
border:1px solid rgba(14,165,233,0.4);
padding:12px 24px;
border-radius:40px;
color:#38bdf8;
font-weight:700;
font-size:18px;">
⚡ Real-Time
</span>

<span style="
background:rgba(139,92,246,0.15);
border:1px solid rgba(139,92,246,0.4);
padding:12px 24px;
border-radius:40px;
color:#a78bfa;
font-weight:700;
font-size:18px;">
🤖 AI Powered
</span>

</div>

</div>
""", unsafe_allow_html=True)

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style="
    background:rgba(255,255,255,0.05);
    backdrop-filter:blur(20px);
    padding:20px;
    border-radius:20px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.1);
    ">
    <h3>🎯 Accuracy</h3>
    <h1 style="color:#22c55e;">98%</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
    background:rgba(255,255,255,0.05);
    backdrop-filter:blur(20px);
    padding:20px;
    border-radius:20px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.1);
    ">
    <h3>⚡ Speed</h3>
    <h1 style="color:#38bdf8;"><1 sec</h1>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="
    background:rgba(255,255,255,0.05);
    backdrop-filter:blur(20px);
    padding:20px;
    border-radius:20px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.1);
    ">
    <h3>📊 Records</h3>
    <h1 style="color:#a855f7;">1200+</h1>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style="
    background:rgba(255,255,255,0.05);
    backdrop-filter:blur(20px);
    padding:20px;
    border-radius:20px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.1);
    ">
    <h3>🏥 Status</h3>
    <h1 style="color:#f59e0b;">Active</h1>
    </div>
    """, unsafe_allow_html=True)









# =====================================
# INPUT SECTION
# =====================================

# =====================================
# INPUT SECTION
# =====================================

st.markdown("""
<div class="glass-card">

<h2 style="color:white;">
🩺 Enter Health Information
</h2>

<p style="color:#94a3b8;">
Provide your health details below.
</p>

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
# HEALTH DASHBOARD
# =====================================

st.subheader("📊 Health Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👤 Age", age)

with col2:
    st.metric("⚖ BMI", round(bmi, 1))

with col3:
    st.metric("🏋 Weight", f"{weight} kg")

with col4:
    st.metric("🔥 Calories", int(daily_calories))

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

    if prediction == 0:
        health_status = "✅ HEALTHY"
        status_color = "#22c55e"

    elif prediction == 1:
        health_status = "⚠️ MODERATE"
        status_color = "#f59e0b"

    else:
        health_status = "❌ UNHEALTHY"
        status_color = "#ef4444"

    st.markdown(f"""
    <div style="
    background:{status_color};
    padding:25px;
    border-radius:20px;
    text-align:center;">

    <h1 style="color:white;">
    {health_status}
    </h1>

    </div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
<div style="
background:linear-gradient(135deg,#1e293b,#0f172a);
padding:25px;
border-radius:25px;
margin-top:20px;
margin-bottom:20px;
color:white;">

<h2>👤 Patient Summary</h2>

<table style="width:100%;font-size:18px;">

<tr>
<td><b>Age</b></td>
<td>{age}</td>
</tr>

<tr>
<td><b>Weight</b></td>
<td>{weight} kg</td>
</tr>

<tr>
<td><b>Height</b></td>
<td>{height} cm</td>
</tr>

<tr>
<td><b>BMI</b></td>
<td>{bmi:.1f}</td>
</tr>

<tr>
<td><b>Calories</b></td>
<td>{daily_calories}</td>
</tr>

</table>

</div>
""", unsafe_allow_html=True)






    
    
   # =====================================
# BMI ANALYSIS CARD
# =====================================

    if bmi < 18.5:
        bmi_status = "Underweight"
        bmi_color = "#3b82f6"

    elif bmi < 25:
        bmi_status = "Normal Weight"
        bmi_color = "#22c55e"

    elif bmi < 30:
        bmi_status = "Overweight"
        bmi_color = "#f59e0b"

    else:
        bmi_status = "Obese"
        bmi_color = "#ef4444"

    bmi_position = min(max((bmi / 40) * 100, 0), 100)

    st.markdown(f"""
    <div style="
    background:rgba(255,255,255,0.05);
    backdrop-filter:blur(20px);
    padding:25px;
    border-radius:25px;
    margin-top:20px;
    border:1px solid rgba(255,255,255,0.1);
    color:white;">

    <h2>🩺 Health Insights</h2>

    <div style="
    display:flex;
    justify-content:space-around;
    text-align:center;
    margin-top:20px;">

    <div>
    <h3>⚖ BMI</h3>
    <h1 style="color:{bmi_color};">{bmi:.1f}</h1>
    </div>

    <div>
    <h3>📊 Status</h3>
    <h1 style="color:{bmi_color};">{bmi_status}</h1>
    </div>

    <div>
    <h3>🔥 Score</h3>
    <h1 style="color:#22c55e;">{health_score}</h1>
    </div>

    </div>

    </div>
    """, unsafe_allow_html=True)













    # HEALTH SCORE DONUT CHART
    # =====================================

    score_fig = go.Figure(
        go.Pie(
            values=[health_score, 100-health_score],
            hole=0.8,
            marker_colors=["#22c55e", "#1e293b"],
            textinfo="none"
        )
    )

    score_fig.update_layout(
        title="💚 Health Score",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"),
        height=350
    )

    st.plotly_chart(score_fig, use_container_width=True)
















 # =====================================
# PERSONALIZED HEALTH TIPS
# =====================================

    tips = []

    if bmi < 18.5:
        tips.append("🍎 Increase protein-rich foods")
        tips.append("🥛 Add healthy calories to meals")

    elif bmi > 25:
        tips.append("🏃 Increase daily physical activity")
        tips.append("🥗 Reduce processed foods")

    else:
        tips.append("✅ Maintain your current lifestyle")
        tips.append("💧 Stay hydrated")

    st.markdown("### 💡 Personalized Health Tips")

    for tip in tips:
        st.info(tip)
    
    # =====================================
# AI RECOMMENDATIONS
# =====================================

    st.subheader("🤖 AI Recommendations")

    recommendations = []

    if bmi > 25:
        recommendations.append(
            "🏃 Increase physical activity and follow a balanced diet."
    )

    if bmi < 18.5:
        recommendations.append(
            "🍎 Increase healthy calorie intake and protein consumption."
    )

    if daily_calories > 2500:
        recommendations.append(
            "🔥 Consider reducing daily calorie consumption."
    )

    if prediction == 2:
        recommendations.append(
            "🩺 Consult a healthcare professional."
    )

    if len(recommendations) == 0:
        recommendations.append(
            "✅ Maintain your current healthy lifestyle."
    )

    for rec in recommendations:
        st.success(rec)

        # Download Report

    report = f"""
HEALTH REPORT

Age: {age}
Weight: {weight}
Height: {height}
BMI: {bmi}

Health Score: {health_score}
Prediction: {health_status}
"""

    st.download_button(
        "📄 Download Report",
        report,
        file_name="health_report.txt"
)





st.markdown("""
<hr>

<center>

<p style="color:#94a3b8;">
Health Status Prediction System © 2026
</p>

</center>
""", unsafe_allow_html=True)