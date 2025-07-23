import streamlit as st
import numpy as np
import joblib

# Page config
st.set_page_config(page_title="Income Prediction App", layout="centered")

# Load model
try:
    model = joblib.load('best_model.pkl')
except FileNotFoundError:
    st.error("❌ Model file 'best_model.pkl' not found.")
    st.stop()
except Exception as e:
    st.error(f"⚠️ Error loading model: {e}")
    st.stop()

# Custom CSS
st.markdown("""
    <style>
    .main-container {
        background-color: #f7f9fa;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 0 10px rgba(0,0,0,0.07);
        max-width: 700px;
        margin: auto;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: 600;
        padding: 0.6em 1.5em;
        border-radius: 8px;
    }
    .stRadio > div {
        flex-direction: row;
        gap: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>💡 Predict Tomorrow’s Pay Today</h1>
    <h4 style='text-align: center; color: gray;'>Predict whether a person earns more than 50K or less than 50K</h4>
    <hr style='border: 1px solid #ddd;'>
    """,
    unsafe_allow_html=True
)

# Encoding maps (same as before)
workclass_map = {'Private': 0, 'Self-emp-not-inc': 1, 'Local-gov': 2, 'Others': 3, 'State-gov': 4, 'Self-emp-inc': 5, 'Federal-gov': 6}
marital_map = {'Married-civ-spouse': 0, 'Never-married': 1, 'Divorced': 2, 'Separated': 3, 'Widowed': 4, 'Married-spouse-absent': 5}
occupation_map = {'Prof-specialty': 0, 'Craft-repair': 1, 'Exec-managerial': 2, 'Adm-clerical': 3, 'Sales': 4, 'Other-service': 5, 'Machine-op-inspct': 6, 'Others': 7, 'Transport-moving': 8, 'Handlers-cleaners': 9, 'Farming-fishing': 10, 'Tech-support': 11, 'Protective-serv': 12, 'Priv-house-serv': 13, 'Armed-Forces': 14}
relationship_map = {'Husband': 0, 'Not-in-family': 1, 'Own-child': 2, 'Unmarried': 3, 'Wife': 4, 'Other-relative': 5}
race_map = {'White': 0, 'Black': 1, 'Asian-Pac-Islander': 2, 'Amer-Indian-Eskimo': 3, 'Other': 4}
gender_map = {'Male': 0, 'Female': 1}
native_map = {'United-States': 0, 'Mexico': 1, 'Others': 2, 'Philippines': 3, 'Germany': 4, 'Puerto-Rico': 5, 'Canada': 6, 'El-Salvador': 7, 'India': 8, 'Cuba': 9, 'England': 10, 'China': 11, 'South': 12, 'Jamaica': 13, 'Italy': 14, 'Dominican-Republic': 15, 'Japan': 16, 'Guatemala': 17, 'Poland': 18, 'Vietnam': 19, 'Columbia': 20, 'Haiti': 21, 'Portugal': 22, 'Taiwan': 23, 'Iran': 24, 'Nicaragua': 25, 'Greece': 26, 'Peru': 27, 'Ecuador': 28, 'France': 29, 'Ireland': 30, 'Thailand': 31, 'Hong': 32, 'Cambodia': 33, 'Trinadad&Tobago': 34, 'Laos': 35, 'Outlying-US(Guam-USVI-etc)': 36, 'Yugoslavia': 37, 'Scotland': 38, 'Honduras': 39, 'Hungary': 40, 'Holand-Netherlands': 41}

# Input Form
st.markdown('<div class="main-container">', unsafe_allow_html=True)
with st.form("prediction_form"):
    st.subheader("📝 Enter Person Details")

    age = st.number_input("📅 Age", min_value=18, max_value=100, value=30)
    fnlwgt = st.number_input("📊 Competition Strength (fnlwgt)", value=100000)
    edu_num = st.slider("🎓 Education Level (Numeric)", 1, 16, 10)
    hours = st.slider("⏱ Hours Per Week", 1, 99, 40)
    capital_gain = st.number_input("💰 Capital Gain", value=0)
    capital_loss = st.number_input("💸 Capital Loss", value=0)
    workclass = st.selectbox("👔 Workclass", list(workclass_map.keys()))
    occupation = st.selectbox("💼 Occupation", list(occupation_map.keys()))
    marital = st.selectbox("💍 Marital Status", list(marital_map.keys()))
    relationship = st.selectbox("👨‍👩‍👧 Relationship", list(relationship_map.keys()))
    race = st.selectbox("🧑 Race", list(race_map.keys()))
    gender = st.radio("🧑‍🤝‍🧑 Gender", list(gender_map.keys()))
    native_country = st.selectbox("🌍 Native Country", list(native_map.keys()))

    submitted = st.form_submit_button("🔍 Predict Income")

    if submitted:
        try:
            input_data = np.array([[
                age,
                workclass_map[workclass],
                fnlwgt,
                edu_num,
                marital_map[marital],
                occupation_map[occupation],
                relationship_map[relationship],
                race_map[race],
                gender_map[gender],
                hours,
                native_map[native_country],
                capital_gain,
                capital_loss
            ]])

            prediction = model.predict(input_data)[0]
            label = ">50K" if prediction == 1 else "<=50K"

            st.markdown("---")
            st.subheader("📈 Prediction Result")
            if prediction == 1:
                st.success("💰 The person is likely to earn **more than 50K**.")
            else:
                st.info("💸 The person is likely to earn **50K or less**.")

        except Exception as e:
            st.error(f"⚠️ Error during prediction: {e}")
st.markdown('</div>', unsafe_allow_html=True)
