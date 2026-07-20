import streamlit as st
from predict import predict_diabetes
import time

# ---------------- PAGE ---------------- #

st.set_page_config(
    page_title="AI Diabetes Risk Analyzer",
    page_icon="🩺",
    layout="wide"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#d8f3ff,#eefcff,#ffffff);
}

/* Fade Animation */

@keyframes fadeIn{
0%{opacity:0;transform:translateY(20px);}
100%{opacity:1;transform:translateY(0);}
}

.block-container{
padding-top:2rem;
animation:fadeIn .8s;
}

/* Title */

.title{
text-align:center;
font-size:45px;
font-weight:800;
color:#0066cc;
}

.subtitle{
text-align:center;
font-size:18px;
color:#455A64;
margin-bottom:30px;
}

/* Labels */

label,
[data-testid="stWidgetLabel"]{
font-size:17px !important;
font-weight:bold !important;
color:#0D47A1 !important;
}

/* Inputs */

.stNumberInput input{

background:#1f2937 !important;

color:white !important;

border-radius:15px !important;

border:2px solid #4FC3F7 !important;

padding:12px;

transition:.3s;

}

.stNumberInput input:focus{

border:2px solid cyan !important;

box-shadow:0px 0px 15px cyan !important;

}

/* Button */

div.stButton>button{

width:100%;

height:60px;

border-radius:18px;

font-size:20px;

font-weight:bold;

border:none;

background:linear-gradient(90deg,#0288d1,#00bcd4);

color:white;

transition:.3s;

}

div.stButton>button:hover{

transform:scale(1.03);

box-shadow:0px 0px 20px #00BCD4;

}

/* Result Card */

.card{

background:white;

padding:25px;

border-radius:20px;

box-shadow:0px 10px 25px rgba(0,0,0,.15);

animation:fadeIn .5s;

}

/* Sidebar */

section[data-testid="stSidebar"]{

background:#E3F2FD;

}

</style>
""",unsafe_allow_html=True)

# ---------------- TITLE ---------------- #

st.markdown("<div class='title'>🩺 AI Diabetes Risk Analyzer</div>",unsafe_allow_html=True)

st.markdown("<div class='subtitle'>🏥 Machine Learning Powered Medical Screening System</div>",unsafe_allow_html=True)

# ---------------- INPUT ---------------- #

c1,c2=st.columns(2)

with c1:

    preg=st.number_input("🤰 Pregnancies",0,step=1)

    glucose=st.number_input("🩸 Glucose Level",0)

    bp=st.number_input("❤️ Blood Pressure",0)

    skin=st.number_input("🧬 Skin Thickness",0)

with c2:

    insulin=st.number_input("💉 Insulin",0)

    bmi=st.number_input("⚖ BMI",0.0,format="%.1f")

    dpf=st.number_input("🧪 Diabetes Pedigree Function",0.0,format="%.3f")

    age=st.number_input("🎂 Age",1)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🏥 About")

st.sidebar.success("✔ AI Powered")

st.sidebar.info("""

This dashboard predicts diabetes risk using

Machine Learning.

Enter patient information

Click Analyze

View AI Report

""")

# ---------------- BUTTON ---------------- #

if st.button("🩺 Analyze Health Risk"):

    status=st.empty()

    progress=st.progress(0)

    status.info("🔍 Collecting Patient Information...")

    progress.progress(15)

    time.sleep(.6)

    status.info("🩸 Checking Blood Glucose...")

    progress.progress(35)

    time.sleep(.6)

    status.info("💉 Analyzing Insulin...")

    progress.progress(55)

    time.sleep(.6)

    status.info("🤖 Running AI Prediction Model...")

    progress.progress(80)

    time.sleep(.8)

    status.success("✅ Report Generated Successfully")

    progress.progress(100)

    prediction,probability=predict_diabetes([
        preg,
        glucose,
        bp,
        skin,
        insulin,
        bmi,
        dpf,
        age
    ])

    st.markdown("## 📋 AI Medical Report")

    st.progress(float(probability))

    if prediction==1:

        st.markdown(f"""
        <div class="card">

        <h2 style="color:#d32f2f;">⚠ HIGH DIABETES RISK</h2>

        <h3>Confidence : {probability*100:.2f}%</h3>

        <hr>

        <h4>Recommendations</h4>

        ✔ Consult a Doctor

        <br>

        ✔ Maintain Healthy Diet

        <br>

        ✔ Monitor Blood Sugar

        <br>

        ✔ Regular Exercise

        </div>
        """,unsafe_allow_html=True)

    else:

        st.markdown(f"""
        <div class="card">

        <h2 style="color:#2e7d32;">✅ LOW DIABETES RISK</h2>

        <h3>Confidence : {probability*100:.2f}%</h3>

        <hr>

        <h4>Recommendations</h4>

        ✔ Continue Healthy Lifestyle

        <br>

        ✔ Balanced Diet

        <br>

        ✔ Regular Exercise

        <br>

        ✔ Annual Health Check-up

        </div>
        """,unsafe_allow_html=True)
