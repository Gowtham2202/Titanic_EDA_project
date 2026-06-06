 Titanic Exploratory Data Analysis (EDA)

 Project Overview

This project was completed as part of the Data Analyst Internship Task 5: Exploratory Data Analysis (EDA).

The objective of this project is to analyze the Titanic dataset using Python and identify patterns, trends, and relationships that influenced passenger survival. Various statistical methods and visualizations were used to gain insights from the data.

---

 Objective

* Understand the structure of the Titanic dataset.
* Perform exploratory data analysis (EDA).
* Identify missing values and data distributions.
* Analyze relationships between features and survival.
* Generate visualizations to support findings.
* Summarize key insights and observations.

---

 Tools & Libraries Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

 Dataset Information

The Titanic dataset contains information about passengers aboard the RMS Titanic.

 Features

| Column      | Description                       |
| ----------- | --------------------------------- |
| PassengerId | Unique passenger identifier       |
| Survived    | Survival status (0 = No, 1 = Yes) |
| Pclass      | Passenger class                   |
| Name        | Passenger name                    |
| Sex         | Gender                            |
| Age         | Age of passenger                  |
| SibSp       | Number of siblings/spouses aboard |
| Parch       | Number of parents/children aboard |
| Ticket      | Ticket number                     |
| Fare        | Ticket fare                       |
| Cabin       | Cabin number                      |
| Embarked    | Port of embarkation               |

---

 Project Structure

```text
TASK 5/
│
├── data/
│   └── train.csv
│
├── outputs/
│   ├── survival_distribution.png
│   ├── age_distribution.png
│   ├── fare_distribution.png
│   ├── gender_survival.png
│   ├── class_survival.png
│   ├── fare_survival.png
│   ├── age_survival.png
│   ├── heatmap.png
│   └── pairplot.png
│
├── src/
│   ├── load_data.py
│   ├── data_summary.py
│   ├── univariate_analysis.py
│   ├── bivariate_analysis.py
│   ├── multivariate_analysis.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

 Analysis Performed

 1. Dataset Overview

* Displayed dataset information using `.info()`
* Generated statistical summary using `.describe()`
* Identified missing values using `.isnull().sum()`

 2. Univariate Analysis

* Survival Distribution
* Age Distribution
* Fare Distribution
* Age Boxplot

 3. Bivariate Analysis

* Gender vs Survival
* Passenger Class vs Survival
* Fare vs Survival
* Age vs Survival

 4. Multivariate Analysis

* Correlation Heatmap
* Pairplot Analysis

---
Visualizations Used

* Count Plot
* Histogram
* Box Plot
* Bar Chart
* Heatmap
* Pairplot

Key Findings

1. Majority of passengers did not survive.
2. Female passengers had significantly higher survival rates.
3. First-class passengers were more likely to survive.
4. Higher ticket fares were associated with better survival chances.
5. Most passengers were between 20 and 40 years old.
6. Fare distribution was positively skewed.
7. Passenger class strongly influenced survival probability.
8. Missing values were primarily found in Cabin and Age columns.

Learning Outcomes

* Data Cleaning and Inspection
* Exploratory Data Analysis (EDA)
* Statistical Data Interpretation
* Data Visualization
* Correlation Analysis
* Pattern and Trend Identification
* Business Insight Generation
