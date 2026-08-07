#  Energy Consumption Forecasting Using Machine Learning

> **Hourly Electricity Demand Prediction Using Weather Data, Feature Engineering, Random Forest, and XGBoost**


# Project Overview

This project forecasts hourly electricity consumption using historical energy demand and weather data. After preprocessing and feature engineering, **Random Forest** and **XGBoost** models were trained and compared using **MAE, RMSE, and R² Score**. The best-performing model was then used to generate future electricity demand forecasts through recursive prediction.



# Problem Statement

Electricity demand changes with weather conditions, seasonal patterns, and human activities. Accurate forecasting helps utilities optimize power generation, reduce operational costs, and improve grid reliability. This project predicts hourly electricity consumption using historical demand and weather data.


# Objectives

* Preprocess and merge energy and weather datasets.
* Perform feature engineering using lag and time-based features.
* Train **Random Forest** and **XGBoost** regression models.
* Evaluate model performance using **MAE, RMSE, and R² Score**.
* Compare both models and select the best-performing model.
* Forecast future hourly electricity consumption.



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

# Installation guide and Requirement

```bash
git clone https://github.com/your-username/Energy-Consumption-Forecasting.git

cd Energy-Consumption-Forecasting

pip install -r requirements.txt

jupyter notebook


# Dataset

The project uses two datasets merged on hourly timestamps to create the final training dataset.

## 1. Energy Consumption Dataset

* **Region:** California (US)
* **Time Period:** January 2019 – April 2026
* **Target Variable:** California Consumption (MW)
* **Frequency:** Hourly

## 2. Weather Dataset

The weather dataset provides hourly environmental data corresponding to the energy consumption records.

**Features Used**

* Temperature
* Relative Humidity

## Final Dataset

The merged dataset combines energy consumption, weather data, and engineered features for model training and forecasting.


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
### Step 2 : Load Energy Dataset
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

---

### Step 9 : Training the model
- Trained Random Forest Regressor and XGBoost Regressor using the training dataset.
- Configured each model with appropriate hyperparameters for energy consumption forecasting.

---

### Step 10 : Generate prediction
- Used the trained models to predict energy consumption on the testing dataset.
- Stored the predictions for later performance evaluation and model comparison.

---

### Step 11 Model Evaluation
Calculated **MAE** (Mean Absolute Error), **RMSE** (Root Mean Squared Error), and **R² Score** to measure prediction accuracy and compare the performance of both models.

---

### Step 12 Model Performance Comparison
-Created a comparison table containing MAE, RMSE, and R² Score for both Random Forest and XGBoost models.
-**XGBoost** achieved the best overall performance, with slightly better MAE and R² Score, and a significantly lower RMSE than the Random Forest model.

---


### Step 13 Prediction Comparison on Individual Values

-Created a comparison table showing the actual values, Random Forest predictions, and XGBoost predictions.
-Calculated the prediction error and absolute error for both models to compare their prediction accuracy on individual test samples.

---

### Step 14  Visulaiztion of Energy Consumption (2019 to April 2026)
 **Daily trend**


 **Weekly Average trend**


 **Monthly Average trend**


 ---


 ### Step 15 Actual vs Predicted Consumption
 -Plotted the actual energy consumption alongside the predictions from Random Forest and XGBoost on the testing dataset.
 -Used the graph to identify which model more closely followed the real energy consumption pattern.

 ---


## FUTURE ENERGY FORECASTING

***Note: Historical energy consumption data was available only until April 2026. Therefore, future forecasting was performed for the period May–August 2026 using the available weather data and the trained model.**

---


### Step 16 Prepare Future Input Data
- Loaded the future weather dataset (new_weather_info.xlsx) containing weather information for the forecasting period (May–August 2026).
- Inspected the dataset to verify its structure and data types.
- Generated time-based features (Hour, DayOfWeek, Month, and IsWeekend) from the Date column to prepare the input data for future energy consumption prediction.

---

### Step 17 Future Energy Consumption Prediction
-Generated lag features using historical and previously predicted values.
-Predicted future energy consumption using the trained XGBoost model.
-Stored the predicted values in the dataset for the complete forecasting period (May–August 2026).

### Step 18 Visualize Future Forecast
- Visualized the predicted energy consumption for the May–August 2026 forecasting period.
- The forecast follows a realistic trend during the initial period (May–June). However, a noticeable drop appears from early July as the model increasingly relies on previously predicted values for lag features instead of historical observations, causing prediction errors to accumulate over time

---
---

# 📈 Results & Key FindingsModel Performance: 
XGBoost outperformed the Random Forest Regressor across metrics, demonstrating superior $R^2$ accuracy and a lower RMSE value when learning complex non-linear relationships.Trend Alignment: Visual evaluation confirmed that predictions closely matched real daily peaks, weekly cycles, and monthly seasonality shifts.Future Demand Forecasting: Successfully generated hourly future electricity demand projections for May–August 2026.
## 💡 Observation on Future Forecasts: While short-term recursive forecasts (May–June 2026) yielded accurate baseline trends, long-range predictions (July–August 2026) showed error compounding due to relying heavily on previously predicted lag values rather than ground-truth historical inputs.


# 🚀 Future Improvements
- Evaluate deep learning models such as **LSTM** and **Transformer** for long-term forecasting.
- Develop a web-based dashboard for real-time energy demand prediction and visualization.

# Conclusion

This project demonstrates that machine learning can effectively forecast hourly electricity consumption using historical demand, weather conditions, and engineered time-series features. Among the evaluated models, **XGBoost** delivered the best overall performance and was selected as the final forecasting model. The proposed approach provides reliable short-term forecasts that can support energy planning and decision-making.