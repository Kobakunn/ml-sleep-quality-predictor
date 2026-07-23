from flask import Flask, render_template, request
from sleep_model import calculate_bmi_category, create_input_df, predict_sleep_quality

app: Flask = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # リクエストパラメータの定義
    age = int(request.form["age"])
    weight = float(request.form["weight"])
    height = float(request.form["height"])
    # gender = request.form["gender"]
    sleep_duration = float(request.form["sleep_duration"])
    physical_activity = int(request.form["physical_activity"])
    stress_level = int(request.form["stress_level"])
    heart_rate = int(request.form["heart_rate"])
    daily_steps = int(request.form["daily_steps"])
    # sleep_disorder = request.form["sleep_disorder"]

    # 受け取ったパラメータから、結果を返す
    bmi_category = calculate_bmi_category(height=height, weight=weight)

    input_df = create_input_df(
        age,
        sleep_duration,
        physical_activity,
        stress_level,
        heart_rate,
        daily_steps,
        bmi_category
    )

    result = predict_sleep_quality(input_df=input_df)

    if result >= 8:
        status = "良好"

    elif result >= 6:
        status = "普通"

    else:
        status = "要改善"

    massage = "サンプル"

    return render_template(
        "result.html",
        result=result,
        status=status,
        message=massage
    )


if __name__ == "__main__":
    app.run(debug=True)