import joblib
import pandas as pd

model = joblib.load("../models/sleep_quality_model.pkl")

# bmiの計算
def calculate_bmi_category(height, weight):

    bmi = weight / ((height / 100) ** 2)

    if bmi < 25:
        return "Normal"

    elif bmi < 35:
        return "Obese"

    return "Overweight"

# DataFrameの定義
def create_input_df(
    age,
    sleep_duration,
    stress_level,
    heart_rate,
    daily_steps,
    bmi_category
):

    return pd.DataFrame([{
        "Age": age,
        "Sleep Duration": sleep_duration,
        "Stress Level": stress_level,
        "BMI Category": bmi_category,
        "Heart Rate": heart_rate,
        "Daily Steps": daily_steps
    }])

# 予測の処理
def predict_sleep_quality(input_df):
    prediction = model.predict(input_df)[0]
    return int(round(prediction, 1))
