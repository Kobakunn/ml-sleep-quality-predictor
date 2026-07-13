# Sleep Insight

生活習慣データから睡眠品質を予測する機械学習Webアプリ

## プロジェクト概要

Kaggle公開データセット「Sleep Health and Lifestyle Dataset」を活用し、生活習慣データから睡眠品質（Quality of Sleep）を予測する機械学習モデルを構築。

EDA（探索的データ分析）、前処理、特徴量選定、複数モデル比較、特徴量重要度分析を実施し、学習済みモデルをFlaskアプリへ組み込むことで、ユーザーがブラウザ上から睡眠品質を予測できるヘルスケアアプリケーションを開発。

***

# 使用技術

## バックエンド

* Python
* Flask

## 機械学習

* scikit-learn
* Pandas
* NumPy
* Joblib

## 可視化

* Matplotlib
* Seaborn
* Plotly

## フロントエンド

* HTML
* CSS
* JavaScript

## その他

* Git
* GitHub
* Jupyter Notebook

***

# データセット

Sleep Health and Lifestyle Dataset

## 概要

* レコード数：374件
* カラム数：13列
* 目的変数：Quality of Sleep
* タスク：回帰問題

***

# EDA（探索的データ分析）

## 実施内容

* データ構造確認
* 欠損値確認
* 数値特徴量分布分析
* カテゴリ特徴量分析
* 相関分析
* 睡眠品質との関係分析

***

## BMI Category分析

### 発見事項

BMI Categoryには以下のカテゴリが存在していた。

```text
Normal
Normal Weight
Overweight
Obese
```

分析の結果、「Normal」と「Normal Weight」は実質的に同一カテゴリと判断。

### 平均睡眠品質

```text
Normal           7.66
Normal Weight    7.43
Overweight       6.90
Obese            6.40
```

BMIが高くなるにつれて睡眠品質が低下する傾向を確認。

***

## 年齢・性別分析

性別別平均睡眠品質

```text
Female    7.66
Male      6.97
```

### 発見事項

* 50歳以上のサンプルは女性のみ
* 53歳以上は睡眠品質がほぼ9で固定

そのため、

```text
年齢が高いほど睡眠品質が高い
```

という単純な結論は導けず、データセット固有の偏りが存在する可能性があると考察。

***

## 職業分析

職業ごとの平均睡眠品質を比較した結果、

```text
Engineer               8.41
Lawyer                 7.89
Accountant             7.89
Nurse                  7.37
Teacher                6.98
Doctor                 6.65
Salesperson            6.00
Scientist              5.00
Sales Representative   4.00
```

職業による差が確認された。

ただし、

* 一部サンプル数が極端に少ない
* ユーザーが変更できない特徴量

であることから、アプリ採用時は慎重に検討した。

***

# 特徴量選定

予測精度だけでなく、

```text
ユーザーが入力しやすいか
改善行動につながるか
```

を考慮して特徴量を選定。

## 採用特徴量

```text
Gender
Sleep Duration
Physical Activity Level
Stress Level
BMI Category
Heart Rate
Daily Steps
```

アプリでは

```text
身長
体重
```

を入力し、BMI Categoryを内部生成する方式を採用。

***

# モデル比較

比較モデル

```text
Linear Regression
Random Forest Regressor
Gradient Boosting Regressor
```

評価指標

```text
MAE
RMSE
R²
```

***

# 特徴量セット比較

## パターンA

Sleep Durationあり

```text
Gender
Sleep Duration
Physical Activity Level
Stress Level
BMI Category
Heart Rate
Daily Steps
```

### 最良モデル

GradientBoostingRegressor

```text
MAE  = 0.026
RMSE = 0.061
R²   = 0.998
```

***

## パターンB

Sleep Durationなし

```text
Gender
Physical Activity Level
Stress Level
BMI Category
Heart Rate
Daily Steps
```

### 最良モデル

GradientBoostingRegressor

```text
MAE  = 0.042
RMSE = 0.115
R²   = 0.991
```

### 考察

Sleep Durationを除外しても非常に高い性能を維持した。

一方でアプリの実用性やユーザーの納得感を考慮し、最終的にはSleep Durationを入力項目として採用した。

***

# 特徴量重要度分析

Sleep Duration除外モデルで分析。

```text
Stress Level                 0.876
Physical Activity Level      0.059
Heart Rate                   0.052
Daily Steps                  0.010
BMI Category_Obese           0.002
BMI Category_Normal          0.001
BMI Category_Overweight      0.000
```

## 考察

* Stress Levelが最も大きな影響を持つ
* 運動量と心拍数も一定の寄与を持つ
* BMI Categoryの寄与は比較的小さい

今回のデータセットではストレスレベルが睡眠品質を説明する主要因であることが確認できた。

***

# 実装済み機能

* 睡眠品質予測モデル構築
* 特徴量選定
* 学習済みモデル保存
* Flaskアプリ構築
* 入力フォーム実装
* BMI自動計算
* 推論処理実装
* 結果画面表示

***

# 開発中機能

* 診断結果画面のUI改善
* 睡眠品質ランク表示
* 睡眠改善アドバイス機能
* グラフによる可視化
* レスポンシブ対応

***

# 今後の展望

* Plotlyによるデータ可視化
* 睡眠品質履歴管理
* モデル説明機能追加
* SHAPによる予測根拠表示
* UI/UX改善

