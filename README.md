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
 Pandas and NumPy were used for data preprocessing, Matplotlib for visualization, Scikit-learn for machine learning utilities, and XGBoost for gradient boosting    regression.
 
 <img width="780" height="195" alt="Screenshot 2026-08-06 150058" src="https://github.com/user-attachments/assets/15b951d7-04de-4dd7-b248-0abfd22b4397" />

---
# Step 2 : Load Energy Dataset
Historical hourly electricity consumption data was loaded from multiple Excel files. These files were combined into a single DataFrame to create a continuous dataset for preprocessing and analysis.

<img width="664" height="203" alt="Screenshot 2026-08-06 153507" src="https://github.com/user-attachments/assets/357b812c-6d28-4493-acef-d59c8e521632" />

 ---
 ### Step 3 : Merging Data
 Energy consumption data from 2019 to april 2026 merged into single excel file using pandas and saved in Energy_consumption_2019_April2026.xlsx

 <img width="720" height="331" alt="Screenshot 2026-08-06 154029" src="https://github.com/user-attachments/assets/ea32ce44-618f-4c01-8242-c7bf30d24963" />

---

### Step 4 : Load and Inspect merged energy data and Weather data
The hourly weather dataset and merged dataset was loaded into a Pandas DataFrame and inspected to verify its structure, data types, and completeness before merging it with the energy consumption datase
<img width="725" height="329" alt="Screenshot 2026-08-06 160156" src="https://github.com/user-attachments/assets/07e2314e-febb-4942-90d7-e38290733885" />
<img width="689" height="154" alt="Screenshot 2026-08-06 161034" src="https://github.com/user-attachments/assets/d5407d04-8be3-43f6-8c3a-06791b1e9f8f" />


Weather Data 

<img width="508" height="113" alt="Screenshot 2026-08-06 160841" src="https://github.com/user-attachments/assets/0f5b710e-b1bb-45c8-9cde-9503df349491" />
<img width="553" height="159" alt="Screenshot 2026-08-06 160851" src="https://github.com/user-attachments/assets/2e46de02-20da-4694-a056-fd8256e655e8" />

---
### Step 5: Restore Date-Time Format and Merge 
The original energy consumption dataset contained only the date, while the hourly time information was missing after processing. To ensure compatibility with the weather dataset, the complete date-time format (including hours) was restored. This enables accurate merging of both dataset.

<img width="695" height="335" alt="Screenshot 2026-08-06 161824" src="https://github.com/user-attachments/assets/2f939437-9e81-4e67-8285-b2080cf5a5f4" />

---

### Step 6 : Data Cleaning
Before training the machine learning models, the merged dataset was cleaned to improve data quality and retain only the features relevant to California Region for energy consumption forecasting. Unnecessary columns were removed, and selected column names were renamed to make the dataset more consistent, readable, and easier to work with during feature engineering and model development.
 <img width="703" height="227" alt="Screenshot 2026-08-06 162517" src="https://github.com/user-attachments/assets/d27afb3e-af1a-4ab7-a53b-ad9b5620b4bf" />
<img width="769" height="199" alt="Screenshot 2026-08-06 162706" src="https://github.com/user-attachments/assets/5dabad2f-494c-4eb0-8c16-1ed9c9e87949" />

---