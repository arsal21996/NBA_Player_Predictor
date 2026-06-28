## app.py


import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="NBA Player Points Predictor",
    page_icon="🏀",
    layout="centered"
)

st.title("🏀 NBA Player Points Predictor")
st.write("Enter a player's information to predict their Points Per Game (PTS).")

# -----------------------------
# User Inputs
# -----------------------------
age = st.number_input("Age", min_value=18, max_value=45, value=25)

player_height = st.number_input(
    "Height (cm)",
    min_value=160.0,
    max_value=230.0,
    value=200.0
)

player_weight = st.number_input(
    "Weight (kg)",
    min_value=60.0,
    max_value=180.0,
    value=100.0
)

gp = st.number_input(
    "Games Played",
    min_value=0,
    max_value=82,
    value=70
)

reb = st.number_input(
    "Rebounds Per Game",
    min_value=0.0,
    max_value=20.0,
    value=5.0
)

ast = st.number_input(
    "Assists Per Game",
    min_value=0.0,
    max_value=15.0,
    value=3.0
)

net_rating = st.number_input(
    "Net Rating",
    value=0.0
)

oreb_pct = st.number_input(
    "Offensive Rebound %",
    value=5.0
)

dreb_pct = st.number_input(
    "Defensive Rebound %",
    value=15.0
)

usg_pct = st.number_input(
    "Usage %",
    value=20.0
)

ts_pct = st.number_input(
    "True Shooting %",
    value=55.0
)

ast_pct = st.number_input(
    "Assist %",
    value=15.0
)

experience = st.number_input(
    "Years of Experience",
    min_value=0,
    max_value=25,
    value=3
)

is_drafted = st.selectbox(
    "Drafted?",
    ["Yes", "No"]
)

height_category = st.selectbox(
    "Height Category",
    ["Guard", "Wing", "Big"]
)

weight_category = st.selectbox(
    "Weight Category",
    ["Light", "Medium", "Heavy"]
)

# -----------------------------
# Prediction Button
# -----------------------------
if st.button("Predict Points"):

    height_m = player_height / 100
    bmi = player_weight / (height_m ** 2)

    input_data = {
        "age": age,
        "player_height": player_height,
        "player_weight": player_weight,
        "gp": gp,
        "reb": reb,
        "ast": ast,
        "net_rating": net_rating,
        "oreb_pct": oreb_pct,
        "dreb_pct": dreb_pct,
        "usg_pct": usg_pct,
        "ts_pct": ts_pct,
        "ast_pct": ast_pct,
        "experience": experience,
        "is_drafted": 1 if is_drafted == "Yes" else 0,
        "height_m": height_m,
        "BMI": bmi,
        "height_category": height_category,
        "weight_category": weight_category
    }

    input_df = pd.DataFrame([input_data])

    # One-hot encode categorical variables
    input_df = pd.get_dummies(input_df)

    # Match training columns
    input_df = input_df.reindex(columns=feature_columns, fill_value=0)

    prediction = model.predict(input_df)[0]

    st.success(f"🏀 Predicted Points Per Game: **{prediction:.2f}**")
