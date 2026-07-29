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
    sleep_duration = float(request.form["sleep_duration"])
    stress_level = int(request.form["stress_level"])
    heart_rate = int(request.form["heart_rate"])
    daily_steps = int(request.form["daily_steps"])
    
    # 受け取ったパラメータから、結果を返す
    bmi_category = calculate_bmi_category(height=height, weight=weight)

    input_df = create_input_df(
        age,
        sleep_duration,
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


    # フィードバックメッセージ（SHAP値が高い特徴量を優先的に、コメント文を追加）
    advice = []

    if sleep_duration < 6:
        advice.append(
            "睡眠時間が短めです。普段よりも早めの就寝や、6～8時間の睡眠を心掛けましょう。"
        )

    if stress_level >= 7:
        advice.append(
            "ストレスレベルが高めです。リラックスする時間を作りましょう。"
        )

    if daily_steps <= 4000:
        advice.append(
            "歩数が少なめです。軽い散歩から始めてみましょう。そうすることで、熟睡しやすくなります。"
        )

    if heart_rate >= 80:
        advice.append(
            "安静時心拍数が高めです。十分な休息を取りましょう。"
        )

    if bmi_category == "Obese":
        advice.append(
            "BMIが高めです。適度な運動習慣を検討してみましょう。"
        )

    elif bmi_category == "Overweight":
        advice.append(
            "体重管理や意識しましょう。食生活の改善や運動習慣などを心掛けるとよいです。"
        )

    if len(advice) == 0:
        if result >= 8:
            advice.append(
                "健康状態を意識出来ていますね。この調子で今後も現在の生活習慣を維持しましょう！"
            )
        elif result >= 6:
            advice.append(
                "平均的な睡眠の質です。少しの意識でさらに改善できます。"
            )
        else:
            advice.append(
                "睡眠の質が低下している可能性があります。生活習慣を見直してみましょう。"
            )

    return render_template(
            "result.html",
            result=result,
            status=status,
            advice=advice
        )


if __name__ == "__main__":
    app.run(debug=True)