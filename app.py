import streamlit as st
from src.loader import load_data
from src.kpi_calculator import calculate_kpis
from src.filters import apply_filters
from src.charts import (
    create_sales_trend,
    create_category_sales_chart,
    create_profit_region_chart,
    create_monthly_trend_chart,
    create_yearly_trend_chart,
    create_top_products_chart
)

df = load_data("data\Sample - Superstore.xlsx")

st.set_page_config(
    page_title="Superstore Business Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Superstore Business Dashboard")

st.markdown(
    """
    Interactive business dashboard for sales and profitability analysis.
    Use the filters in the sidebar to explore the data.
    """
)

st.divider()
st.dataframe(df.head())

st.divider()
st.subheader("Key Performance Indicator")
filtered_df = apply_filters(df)
kpis = calculate_kpis(filtered_df)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Sales", f"${kpis['Total Sales']/1_000_000:,.2f}M")

with col2:
    st.metric("Total Profit", f"${kpis['Total Profit']/1_000_000:,.2f}M")

with col3:
    st.metric("Orders", kpis["Total Orders"])

with col4:
    st.metric("Customers", kpis["Total Customers"])

with col5:
    st.metric("Profit Margin", f"{kpis['Profit Margin']}%")


st.divider()
st.subheader("Analysis Charts")

sales_chart = create_sales_trend(filtered_df)
category_chart = create_category_sales_chart(filtered_df)
profit_region_chart = create_profit_region_chart(filtered_df)
monthly_chart = create_monthly_trend_chart(filtered_df)
yearly_chart = create_yearly_trend_chart(filtered_df)
top_product_chart = create_top_products_chart(filtered_df)

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.plotly_chart(
        sales_chart,
        use_container_width=True
    )

with chart_col2:
    st.plotly_chart(
        category_chart,
        use_container_width=True
    )
st.plotly_chart(profit_region_chart, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(monthly_chart, use_container_width=True)
with col2:
    st.plotly_chart(yearly_chart, use_container_width=True)

st.plotly_chart(top_product_chart, use_container_width= True)

with st.expander("View Filtered Dataset"):
    st.dataframe(filtered_df)

st.divider()
csv_data = filtered_df.to_csv(index=False)
st.download_button(
    label="Download Filtered Data",
    data=csv_data,
    file_name="filtered_superstore_data.csv",
    mime="text/csv"
)
