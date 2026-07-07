# 睡眠の質予測アプリ開発

生活習慣データから睡眠品質を予測する機械学習Webアプリ

## プロジェクト概要

Kaggle公開データセット「Sleep Health and Lifestyle Dataset」を用いて、ユーザーの生活習慣情報から睡眠品質（Quality of Sleep）を予測する機械学習モデルを構築。

EDA（探索的データ分析）、前処理、複数モデル比較、特徴量重要度分析を実施し、学習済みモデルをFlaskアプリへ組み込むことで、睡眠品質予測および改善アドバイスを提供するWebアプリケーションの開発を行った。

***

## 使用技術

### バックエンド

* Python
* Flask

### 機械学習

* scikit-learn
* Pandas
* NumPy

### 可視化

* Matplotlib
* Seaborn
* Plotly

### フロントエンド

* HTML
* CSS
* Bootstrap

### その他

* Git
* GitHub
* Jupyter Notebook

***

# データセット

Sleep Health and Lifestyle Dataset

| 項目    | 内容               |
| ----- | ---------------- |
| レコード数 | 374件             |
| カラム数  | 13列              |
| 目的変数  | Quality of Sleep |
| タスク   | 回帰問題             |

***

# EDA（探索的データ分析）

## データ確認

* 欠損値は Sleep Disorder のみ確認
* `Person ID` は識別子のため学習対象から除外
* `Blood Pressure` は `Systolic` と `Diastolic` に分割して利用

## BMIカテゴリの確認

データ確認の結果、

```text
Normal
Normal Weight
Overweight
Obese
```

が存在していた。

分析の結果、

```text
Normal
Normal Weight
```

は実質的に同じ意味であると判断し、前処理で統一を検討。

### BMIカテゴリ別睡眠品質

| BMI Category  | 平均睡眠品質 |
| ------------- | -----: |
| Normal        |   7.66 |
| Normal Weight |   7.43 |
| Overweight    |   6.90 |
| Obese         |   6.40 |

肥満傾向になるほど睡眠品質が低下する傾向が確認された。

***

## 年齢・性別分析

性別別平均睡眠品質

| Gender | 平均睡眠品質 |
| ------ | -----: |
| Female |   7.66 |
| Male   |   6.97 |

ただし分析の結果、

* 50歳以上は女性のみで構成
* 53歳以上では睡眠品質が一律9となる傾向

が確認された。

そのため、

```text
年齢が高いほど睡眠品質が高い
```

という単純な解釈はできず、データセット固有の分布やサンプリングの偏りが影響している可能性があると考察した。

***

## 職業分析

職業ごとに平均睡眠品質を比較した結果、

| Occupation  | 平均睡眠品質 |
| ----------- | -----: |
| Engineer    |   8.41 |
| Lawyer      |   7.89 |
| Accountant  |   7.89 |
| Nurse       |   7.37 |
| Teacher     |   6.98 |
| Doctor      |   6.65 |
| Salesperson |   6.00 |
| Scientist   |   5.00 |

職業による差が確認された一方で、

* 一部カテゴリのサンプル数が極端に少ない
* ユーザーが変更できない特徴量である

ことから、最終アプリでの採用については精度と実用性の観点から検討した。

***

# モデル比較

以下のモデルで比較を実施。

* Linear Regression
* Random Forest Regressor
* Gradient Boosting Regressor

評価指標

* MAE
* RMSE
* R²

***

## 特徴量比較

### パターンA

全特徴量

```text
Age
Gender
Occupation
Sleep Duration
Physical Activity Level
Stress Level
BMI Category
Heart Rate
Daily Steps
Sleep Disorder
Blood Pressure
```

***

### パターンB

Occupation除外

***

### パターンC（アプリ向け）

```text
Sleep Duration
Physical Activity Level
Stress Level
BMI Category
Heart Rate
Daily Steps
```

***

### パターンD（Sleep Duration除外）

```text
Physical Activity Level
Stress Level
BMI Category
Heart Rate
Daily Steps
```

***

## 最良モデル

### Sleep Durationあり

GradientBoostingRegressor

```text
MAE  = 0.026
RMSE = 0.061
R²   = 0.998
```

***

### Sleep Durationなし

GradientBoostingRegressor

```text
MAE  = 0.042
RMSE = 0.115
R²   = 0.991
```

睡眠時間を除外しても高い性能を維持しており、生活習慣関連特徴量のみでも睡眠品質予測が可能であることを確認した。

***

# 特徴量重要度分析

Sleep Durationを除外したモデルで特徴量重要度を分析。

| Feature                  | Importance |
| ------------------------ | ---------: |
| Stress Level             |      0.876 |
| Physical Activity Level  |      0.059 |
| Heart Rate               |      0.052 |
| Daily Steps              |      0.010 |
| BMI Category\_Obese      |      0.002 |
| BMI Category\_Normal     |      0.001 |
| BMI Category\_Overweight |      0.000 |

## 考察

* Stress Level が予測に最も大きく寄与
* 運動量および心拍数も一定の影響を持つ
* BMI Category の寄与は限定的

今回のデータセットでは、睡眠品質に対してストレスレベルが支配的な特徴量であることが確認できた。

***

# 今後の実装予定

* FlaskによるWebアプリ化
* 入力フォーム実装
* 睡眠品質スコア表示
* 改善アドバイス表示
* Plotlyによる可視化ダッシュボード
* レスポンシブデザイン対応
* モデル説明機能の追加

***
