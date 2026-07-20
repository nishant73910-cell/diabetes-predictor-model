import streamlit as st

from predict import predict_diabetes



# ---------------- Page Configuration ----------------

st.set_page_config(

    page_title="Health Risk Analyzer",

    page_icon="💙",

    layout="wide"

)



# ---------------- Custom CSS ----------------

st.markdown("""

<style>



/* Background */

.stApp{

    background: linear-gradient(135deg,#e0f7fa,#f8fbff,#e8f5e9);

}



.block-container{

    padding-top:2rem;

}



/* Input Labels */

label,

div[data-testid="stWidgetLabel"] label,

[data-testid="stWidgetLabel"]{

    color:#000000 !important;

    font-size:16px !important;

    font-weight:600 !important;

}



/* Caption */

[data-testid="stCaptionContainer"]{

    color:#37474F !important;

    font-size:16px !important;

}



/* Result Card */

.card{

    background:white;

    padding:20px;

    border-radius:16px;

    box-shadow:0 4px 15px rgba(0,0,0,.12);

}



/* Number Input */

.stNumberInput input{

    background:#23252f !important;

    color:white !important;

    border-radius:8px;

}



/* Button */

div.stButton>button{

    width:100%;

    background:#00897b;

    color:white;

    border:none;

    border-radius:10px;

    height:3em;

    font-weight:bold;

    font-size:16px;

}



div.stButton>button:hover{

    background:#00695c;

    color:white;

}



</style>

""", unsafe_allow_html=True)



# ---------------- Title ----------------

st.markdown(

    "<h1 style='text-align:center;color:#00695c;'>💙 Diabetes Risk Assessment Dashboard</h1>",

    unsafe_allow_html=True

)



st.markdown(

    "<p style='text-align:center;color:#37474F;font-size:18px;'>Fill in the patient's clinical information.</p>",

    unsafe_allow_html=True

)



# ---------------- Input Fields ----------------

c1, c2 = st.columns(2)



with c1:

    preg = st.number_input("Pregnancies", min_value=0, step=1)

    glucose = st.number_input("Glucose Level", min_value=0)

    bp = st.number_input("Blood Pressure", min_value=0)

    skin = st.number_input("Skin Thickness", min_value=0)



with c2:

    insulin = st.number_input("Insulin", min_value=0)

    bmi = st.number_input("BMI", min_value=0.0, format="%.1f")

    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")

    age = st.number_input("Age", min_value=1)



# ---------------- Sidebar ----------------

st.sidebar.header("About")

st.sidebar.info("AI-powered diabetes screening tool.")



# ---------------- Prediction ----------------

if st.button("🔍 Analyze Health Risk"):



    prediction, probability = predict_diabetes([

        preg,

        glucose,

        bp,

        skin,

        insulin,

        bmi,

        dpf,

        age

    ])



    st.markdown("## 📊 Analysis Result")



    st.progress(float(probability))



    if prediction == 1:

        st.markdown(

            f"""

            <div class="card">

                <h3 style="color:#c62828;">⚠ High Diabetes Risk</h3>

                <p><b>Confidence:</b> {probability*100:.2f}%</p>

            </div>

            """,

            unsafe_allow_html=True

        )

    else:

        st.markdown(

            f"""

            <div class="card">

                <h3 style="color:#2e7d32;">✅ Low Diabetes Risk</h3>

                <p><b>Confidence:</b> {probability*100:.2f}%</p>

            </div>

            """,

            unsafe_allow_html=True

        )
