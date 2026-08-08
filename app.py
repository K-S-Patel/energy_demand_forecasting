import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(
    page_title="Future Energy Consumption Forecast", layout="wide"
)

st.title("⚡ California Electricity Load - Future Forecast")


# Sirf saved future_df load kar rahe hain
@st.cache_data
def load_future_data():
    df = pd.read_csv("future_predictions.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df


future_df = load_future_data()

# 1. Plotly Graph (Sirf future_df ka)
st.subheader("📈 Future Forecast Graph")

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=future_df["Date"],
        y=future_df["California_consumption_MW"],
        mode="lines+markers",
        name="Predicted Load (MW)",
        line=dict(color="#FF4B4B", width=2),
        marker=dict(size=6),
        hovertemplate="<b>Date:</b> %{x|%Y-%m-%d %H:%M}<br><b>Predicted Load:</b> %{y:.2f} MW<extra></extra>",
    )
)

fig.update_layout(
    xaxis_title="Future Date & Time",
    yaxis_title="Predicted Consumption (MW)",
    hovermode="x unified",
    template="plotly_white",
    height=500,
)

st.plotly_chart(fig, use_container_width=True)

# 2. Table (Sirf future_df ka)
st.subheader("📋 Future Predictions Table")

cols_to_show = [
    col
    for col in [
        "Date",
        "Predicted_Consumption_MW",
        "Temperature",
        "RelativeHumidity",
    ]
    if col in future_df.columns
]

st.dataframe(
    future_df[cols_to_show].style.format(
        {
            "Predicted_Consumption_MW": "{:.2f}",
            "Temperature": "{:.1f}",
            "RelativeHumidity": "{:.1f}",
        },
        na_rep="-",
    ),
    use_container_width=True,
    height=400,
)