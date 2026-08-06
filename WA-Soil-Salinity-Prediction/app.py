import streamlit as st
import joblib
import pandas as pd

model = joblib.load("models/xgboost_model.joblib")
label_encoder = joblib.load("models/label_encoder.joblib")
# ------------------------------
# Page configuration
# ------------------------------
st.set_page_config(
    page_title="WA Soil Salinity Prediction",
    page_icon="🌱",
    layout="wide"
)



page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🗺️ Prediction",
        "📊 Model Performance",
        "ℹ️ About"
    ]
)

if page == "🏠 Home":

# ------------------------------
# Title
# ------------------------------



# ------------------------------
# Title
# ------------------------------
    st.title("🌱 Western Australia Soil Salinity Prediction")

    st.markdown("""
    This project applies **Machine Learning** to predict soil salinity risk
    in the Western Australian Wheatbelt using environmental variables.
    """)

    st.divider()

# ------------------------------
# Project Overview
# ------------------------------
    st.header("📖 Project Overview")

    st.write("""
    Soil salinity is one of the major environmental challenges affecting
    agricultural productivity in Western Australia.

    This project develops machine learning models to predict soil salinity
    risk using environmental variables including:

    - Elevation
    - Slope
    - Annual Rainfall
    - Land Cover
    """)

# ------------------------------
# Data Source
# ------------------------------
    st.header("🛰 Data Sources")

    st.write("""
    - Department of Primary Industries and Regional Development (DPIRD)
    - AW3D30 Digital Elevation Model
    - ERA5 Annual Rainfall
    - ESA WorldCover 2021
    """)

# ------------------------------
# Machine Learning Models
# ------------------------------
    st.header("🤖 Machine Learning Models")

    st.write("""
    Models explored:

    - Random Forest
    - XGBoost
    """)

# ------------------------------
# Current Results
# ------------------------------
    st.header("📈 Current Performance")

    st.success("Current best accuracy: approximately 57% (XGBoost)")




elif page == "🗺️ Prediction":

    st.title("🗺️ Soil Salinity Prediction")

    elevation = st.number_input(
        "Elevation (m)",
        min_value=0.0,
        value=100.0
    )

    slope = st.number_input(
        "Slope (degree)",
        min_value=0.0,
        value=5.0
    )

    rain = st.number_input(
        "Annual Rainfall (mm)",
        min_value=0.0,
        value=400.0
    )


    st.write("Before dictionary")
    landcover_dict = {
        "Tree Cover": 10,
        "Shrubland": 20,
        "Grassland": 30,
        "Cropland": 40,
        "Built-up": 50,
        "Bare / Sparse Vegetation": 60,
        "Permanent Water Bodies": 80,
        "Herbaceous Wetland": 90
    }
    st.write(landcover_dict)
    selected_landcover = st.selectbox(
        "Land Cover",
        list(landcover_dict.keys())
    )

    landcover = landcover_dict[selected_landcover]

    if st.button("Predict"):

        X_new = pd.DataFrame(
            [[elevation, slope, rain, landcover]],
            columns=["Elevation", "Slope", "Rain", "LandCover"]
        )

        prediction = model.predict(X_new)

        result = label_encoder.inverse_transform(prediction)

        st.success(f"Predicted Soil Salinity Class: {result[0]}")





elif page == "📊 Model Performance":
    st.title("📊 Model Performance")
    st.write("Random Forest Accuracy")
    st.progress(54)

    st.write("XGBoost Accuracy")
    st.progress(57)

elif page == "ℹ️ About":
    st.title("ℹ️ About")

    st.write("""
Author: Jingxuan Wang

Monash University

Master of Data Science
""")