#  Energy Consumption Forecasting Using Machine Learning

> **Hourly Electricity Demand Prediction Using Weather Data, Feature Engineering, Random Forest, and XGBoost**


#  Project Overview

Accurate electricity demand forecasting plays a vital role in modern power systems by helping utility providers balance electricity generation and consumption efficiently. Predicting future energy demand enables better resource planning, reduces operational costs, and improves grid reliability.

This project focuses on forecasting hourly regional electricity consumption using historical electricity demand and weather data. The energy consumption dataset was combined with hourly weather information to create a unified dataset for machine learning.

Several data preprocessing and feature engineering techniques were applied, including data cleaning, dataset merging, lag feature generation, and time-based feature extraction. Two ensemble machine learning algorithms **Random Forest Regressor** and **XGBoost Regressor** were trained and evaluated using multiple performance metrics.

The trained model can be used to predict future hourly electricity consumption for upcoming months using forecasted weather conditions and recursive forecasting.



#  Problem Statement

Electricity demand varies continuously throughout the day due to changing weather conditions, seasonal variations, weekdays, weekends, and human activities. Accurate forecasting is essential for electricity providers to efficiently schedule power generation, minimize operational costs, and maintain a stable electricity supply.

This project addresses the problem of predicting future hourly electricity consumption using historical energy demand and weather information.


#  Objectives

The primary objectives of this project are:

- Collect and preprocess historical energy consumption and weather datasets.
- Merge both datasets using hourly timestamps.
- Perform data cleaning and feature engineering.
- Generate lag features and time-based features for improved forecasting.
- Train a Random Forest Regressor model.
- Train an XGBoost Regressor model.
- Compare model performance using MAE, RMSE, and R² Score.
- Visualize actual and predicted energy consumption of both model.
- Forecast future hourly electricity demand using the trained machine learning model.


#  Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python** | Programming language |
| **Pandas** | Data loading, preprocessing, and manipulation |
| **NumPy** | Numerical computations |
| **Matplotlib** | Data visualization |
| **Scikit-learn** | Random Forest model, preprocessing, train-test split, evaluation metrics |
| **XGBoost** | Gradient boosting regression model |
| **Jupyter Notebook** | Model development and experimentation |



#  Dataset

This project uses two separate datasets that are merged using their common hourly timestamp.

## 1. Energy Consumption Dataset

This dataset contains historical hourly electricity consumption values for the California (US) region. The target variable represents total electricity demand measured in megawatts (MW).

**Key Information**

- Hourly energy consumption records
- Target variable: **California Consumption (MW)**
- Time period: **January 2019 – April 2026**


## 2. Weather Dataset

The weather dataset contains hourly meteorological information corresponding to the same timestamps as the energy dataset.

The following weather features were used:

- Temperature
- Relative Humidity

These weather variables help the model learn how environmental conditions influence electricity demand.

## Final Dataset

After preprocessing and merging, the final dataset contains both energy consumption and weather information along with engineered features used for machine learning.

### Features Used for Training

| Feature | Description |
|---------|-------------|
| Temperature | Hourly temperature |
| RelativeHumidity | Hourly relative humidity |
| Lag_1H | Electricity consumption one hour earlier |
| Lag_1D | Electricity consumption one day earlier |
| Lag_1W | Electricity consumption one week earlier |
| Hour | Hour of the day (0–23) |
| DayOfWeek | Day of the week (0–6) |
| Month | Month of the year |
| IsWeekend | Indicates whether the day is a weekend |
| California_consumption_MW | Target variable (electricity demand) |

## Project Workflow
 ### Step 1 Import Required Libraries
 | **Library** | **Why it is Used** |
|--------------|--------------------|
| **Pandas** | Used for loading, cleaning, merging, and manipulating the dataset in tabular format. |
| **NumPy** | Used for efficient numerical computations and array operations during data preprocessing. |
| **Scikit-learn (Random Forest Regressor)** | Used to build the Random Forest machine learning model for predicting hourly energy consumption. |
| **XGBoost** | Used to train an advanced gradient boosting model and compare its performance with the Random Forest model. |
| **Scikit-learn Metrics (MAE, MSE, R² Score)** | Used to evaluate the prediction accuracy and overall performance of the trained models. |
 
 

---
# Step 2 : Load Energy Dataset
Created a list containing the file paths of all yearly and monthly energy consumption Excel (.xlsx) files. This list was used to automate the data loading process instead of reading each file individually



 ---
 ### Step 3 : Merging Data
Iterated through the list of Excel files using a for loop, loaded each dataset, and combined them into a single DataFrame. The final merged dataset was then exported and saved as **Energy_Consumption_2019_April2026.xlsx** for further preprocessing and model development.

---

### Step 4 : Inspect and Prepare Datasets
Inspected the merged energy consumption dataset using **df.head()** and **df.info()** to verify its structure, data types, and overall data quality. Loaded the weather dataset into a separate DataFrame (weather_df) and performed the same inspection to ensure it was ready for integration. Since the energy dataset stored the date and hour in separate columns (Date and HR), the Date column was updated by adding the corresponding hour values using **merged_df["Date"] = merged_df["Date"] + pd.to_timedelta(merged_df["HR"] - 1, unit="h")**. This created a complete datetime format, making it compatible for merging with the weather datas


---
### Step 5:Merge Energy and Weather Datasets
Merged the energy consumption dataset (merged_df) with the weather dataset (weather_df) using the common datetime columns (Date from the energy dataset and Time from the weather dataset). An inner join (how='inner') was applied to retain only the records with matching timestamps in both datasets, resulting in a unified dataset containing both energy consumption and corresponding weather information and stored in **final_df** dataframe.

---

### Step 6 : Select Relevant Features and Save the Final Dataset - DATA CLEANING
- Removed all unnecessary columns, keeping only **Date**, **SCE**, **Temperature**, and **Relative Humidity**.
- Renamed SCE to **California_Consumption_MW** for better readability.
- Saved the cleaned dataset as final_data.xlsx for further analysis and model training.


---

### Step 7 Feature Engineering
- Created historical lag features **(Lag_1H, Lag_1D, and Lag_1W)** to capture previous energy consumption patterns.
- Removed rows containing null values generated after creating lag features.
- Extracted time-based features **(Hour, DayOfWeek, Month, and IsWeekend)** from the Date column to help the model learn temporal patterns in  electricity consumption.

---

 ## Model Selection
Based on the dataset structure two model **Random Forest Regresser** and **XGBoost** are selected.
**REASON**
Since electricity consumption depends on complex relationships between weather conditions, historical demand, and time-based patterns, ensemble learning models were chosen for their ability to capture nonlinear relationships and improve prediction accuracy.
**Why Ensemble Learning?**

Ensemble learning combines the predictions of multiple decision trees to produce a more accurate and stable model than a single decision tree. It helps reduce overfitting and improves overall prediction performance.

This project uses two ensemble learning algorithms:

* Random Forest Regressor
* XGBoost Regressor


**Random Forest Regressor**

Random Forest is based on the **Bagging (Bootstrap Aggregating)** technique, where multiple decision trees are trained on different subsets of the training data. The final prediction is obtained by averaging the predictions of all trees.

**Why Random Forest?**

* Handles nonlinear relationships effectively.
* Reduces overfitting compared to a single decision tree.
* Performs well on structured tabular data.
* Works well with weather and time-based features.
* Requires minimal preprocessing.

---

**XGBoost Regressor**

XGBoost is based on the **Gradient Boosting** technique, where trees are built sequentially. Each new tree learns from the errors of the previous one, gradually improving the model's predictions.

**Why XGBoost?**

* Delivers high prediction accuracy.
* Captures complex feature relationships.
* Includes regularization to reduce overfitting.
* Optimized for speed and efficiency.
* Widely used for real-world forecasting tasks.

---

### Step 8 : Input Featur, Target Selection and Train Test Split
- **Input Feature** Selected all input features by excluding Date and the target column (California_Consumption_MW).
- **Target Selection** Assigned California_Consumption_MW as the target variable for prediction.

**Train Test Split**
- Split the dataset into 80% training and 20% testing sets using train_test_split().
- Set shuffle=False to preserve the chronological order of the time-series data and random_state=42 for reproducibility.
