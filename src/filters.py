import streamlit as st


import streamlit as st
import pandas as pd


def apply_filters(df):

    st.sidebar.header("Filters")

    # Region Filter
    selected_regions = st.sidebar.multiselect(
        "Select Region",
        options=sorted(df["Region"].unique()),
        default=sorted(df["Region"].unique())
    )

    # Category Filter
    selected_categories = st.sidebar.multiselect(
        "Select Category",
        options=sorted(df["Category"].unique()),
        default=sorted(df["Category"].unique())
    )

    # Segment Filter
    selected_segments = st.sidebar.multiselect(
        "Select Segment",
        options=sorted(df["Segment"].unique()),
        default=sorted(df["Segment"].unique())
    )

    # Date Range Filter
    min_date = df["Order Date"].min().date()
    max_date = df["Order Date"].max().date()

    selected_dates = st.sidebar.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    # In case user selects only one date
    if len(selected_dates) == 2:
        start_date, end_date = selected_dates
    else:
        start_date = min_date
        end_date = max_date

    # Apply Filters
    filtered_df = df[
        (
            df["Region"].isin(selected_regions)
        )
        &
        (
            df["Category"].isin(selected_categories)
        )
        &
        (
            df["Segment"].isin(selected_segments)
        )
        &
        (
            df["Order Date"] >= pd.to_datetime(start_date)
        )
        &
        (
            df["Order Date"] <= pd.to_datetime(end_date)
        )
    ]

    return filtered_df