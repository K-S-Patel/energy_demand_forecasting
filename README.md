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
 ### Step 1
 