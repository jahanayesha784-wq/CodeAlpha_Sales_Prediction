
import streamlit as st
import pandas as pd
import joblib
import os


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Sales Prediction",
    page_icon="📈",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #fff0f6,
        #f3e8ff,
        #ede9fe
    );
}

/* Main Title */

.main-title {
    text-align: center;
    font-size: 45px;
    font-weight: 800;
    color: #7e22ce;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #6b21a8;
    margin-bottom: 30px;
}


/* Input Card */

.card {
    background: rgba(255, 255, 255, 0.92);
    padding: 28px;
    border-radius: 22px;
    box-shadow: 0px 8px 25px rgba(126, 34, 206, 0.12);
    margin-bottom: 20px;
}


/* Prediction Box */

.prediction-box {
    background: linear-gradient(
        135deg,
        #ec4899,
        #8b5cf6
    );

    padding: 35px;
    border-radius: 22px;
    text-align: center;
    color: white;
    margin-top: 30px;

    box-shadow:
        0px 10px 30px rgba(139, 92, 246, 0.25);
}


/* Only the prediction number */

.prediction-number {
    font-size: 44px;
    font-weight: 800;
}


/* Predict Button */

div.stButton > button {
    width: 100%;

    background: linear-gradient(
        90deg,
        #ec4899,
        #8b5cf6
    );

    color: white;
    border: none;
    border-radius: 14px;

    padding: 13px;

    font-size: 18px;
    font-weight: 700;

    transition: 0.3s;
}


div.stButton > button:hover {
    background: linear-gradient(
        90deg,
        #db2777,
        #7c3aed
    );

    color: white;
    transform: scale(1.01);
}


/* Input Labels */

label {
    color: #581c87 !important;
    font-weight: 600 !important;
}


/* Footer */

.footer {
    text-align: center;
    margin-top: 40px;
    color: #7e22ce;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.markdown(
    '<div class="main-title">📈 Sales Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine Learning Based Advertising Sales Prediction'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

MODEL_PATH = os.path.join(
    "models",
    "sales_prediction_model.pkl"
)

if not os.path.exists(MODEL_PATH):

    st.error(
        "Model file not found. Please make sure "
        "'sales_prediction_model.pkl' is inside the models folder."
    )

    st.stop()


model = joblib.load(MODEL_PATH)


# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

st.subheader("Enter Advertising Budget")

col1, col2, col3 = st.columns(3)


with col1:

    tv = st.number_input(
        "TV Advertising",
        min_value=0.0,
        max_value=500.0,
        value=100.0,
        step=1.0
    )


with col2:

    radio = st.number_input(
        "Radio Advertising",
        min_value=0.0,
        max_value=100.0,
        value=25.0,
        step=1.0
    )


with col3:

    newspaper = st.number_input(
        "Newspaper Advertising",
        min_value=0.0,
        max_value=150.0,
        value=25.0,
        step=1.0
    )


st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# PREDICTION BUTTON
# --------------------------------------------------

if st.button("Predict Sales"):

    input_data = pd.DataFrame({
        "TV": [tv],
        "Radio": [radio],
        "Newspaper": [newspaper]
    })

    try:

        prediction = model.predict(input_data)[0]

        prediction = max(0, prediction)

        # Clean prediction display
        st.markdown(
            f"""
            <div class="prediction-box">
                <div class="prediction-number">
                    {prediction:.2f}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    except Exception as e:

        st.error("Prediction failed.")
        st.code(str(e))


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    '<div class="footer">'
    'CodeAlpha Data Science Internship — Task 4'
    '</div>',
    unsafe_allow_html=True
)

