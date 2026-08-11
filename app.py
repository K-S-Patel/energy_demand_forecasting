

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

st.set_page_config(
    page_title="Future Energy Consumption Forecast",
    layout="wide"
)

st.title("⚡ California Electricity Load - Future Forecast")

@st.cache_data
def load_future_data():
    df = pd.read_csv("future_predictions.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    
    # Target column alignment
    if "California_consumption_MW" in df.columns and "Predicted_Consumption_MW" not in df.columns:
        df["Predicted_Consumption_MW"] = df["California_consumption_MW"]
        
    # Filter: Today to 21 August 2026
    today = pd.Timestamp.now().normalize()
    end_date = pd.Timestamp("2026-08-21 23:59:59")
    
    filtered_df = df[(df["Date"] >= today) & (df["Date"] <= end_date)].copy()
    return filtered_df

future_df = load_future_data()

if future_df.empty:
    st.warning("No data found from today onwards up to 21 August.")
else:
    # 1. Dual-Axis Plotly Graph (Consumption + Temperature)
    st.subheader("📈 Future Forecast Graph (Today to 21 August)")

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Predicted Load Trace
    fig.add_trace(
        go.Scatter(
            x=future_df["Date"],
            y=future_df["Predicted_Consumption_MW"],
            mode="lines+markers",
            name="Predicted Load (MW)",
            line=dict(color="#FF4B4B", width=2),
            marker=dict(size=4),
            hovertemplate="<b>Date:</b> %{x|%Y-%m-%d %H:%M}<br><b>Predicted Load:</b> %{y:.2f} MW<extra></extra>",
        ),
        secondary_y=False
    )

    # Temperature Trace (if column exists)
    if "Temperature" in future_df.columns:
        fig.add_trace(
            go.Scatter(
                x=future_df["Date"],
                y=future_df["Temperature"],
                mode="lines",
                name="Temperature (°C)",
                line=dict(color="#1f77b4", width=1.5, dash="dot"),
                hovertemplate="<b>Date:</b> %{x|%Y-%m-%d %H:%M}<br><b>Temperature:</b> %{y:.1f} °C<extra></extra>",
            ),
            secondary_y=True
        )

    fig.update_layout(
        xaxis_title="Date & Time",
        hovermode="x unified",
        template="plotly_white",
        height=520,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    fig.update_yaxes(title_text="Predicted Consumption (MW)", secondary_y=False)
    fig.update_yaxes(title_text="Temperature (°C)", secondary_y=True, showgrid=False)

    st.plotly_chart(fig, use_container_width=True)

    # 2. Filtered Table View
    st.subheader("📋 Future Predictions Table (Today to 21 August)")

    cols_to_show = [
        col for col in [
            "Date",
            "Predicted_Consumption_MW",
            "Temperature",
            "RelativeHumidity"
        ] if col in future_df.columns
    ]

    formatted_df = future_df[cols_to_show].copy()
    formatted_df["Date"] = formatted_df["Date"].dt.strftime("%Y-%m-%d %H:%M")

    st.dataframe(
        formatted_df.style.format(
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