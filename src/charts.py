import plotly.express as px


def create_sales_trend(df):

    sales_over_time = (
        df.groupby("Order Date")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        sales_over_time,
        x="Order Date",
        y="Sales",
        title="Sales Trend Over Time"
    )

    return fig

def create_category_sales_chart(df):

    category_sales = (
        df.groupby("Category")[["Sales", "Profit"]]
        .sum()
        .reset_index()
        .sort_values(
            by="Sales",
            ascending=False
        )
    )

    fig = px.bar(
        category_sales,
        x="Category",
        y=["Sales", "Profit"],
        title="Sales and Profit by Category",
        text_auto=".2s"
    )

    return fig
def create_profit_region_chart(df):

    region_profit = (
        df.groupby("Region")[["Sales", "Profit"]]
        .sum()
        .reset_index()
        .sort_values(
            by = "Sales",
            ascending=False
        )
    )

    fig = px.bar(
        region_profit,
        x="Region",
        y=["Sales", "Profit"],
        title="Sales and Profit by Region",
        text_auto=".2s"
    )

    return fig
def create_monthly_trend_chart(df):

    monthly_data = (
        df
        .resample(
            "ME",
            on="Order Date"
        )[["Sales", "Profit"]]
        .sum()
        .reset_index()
    )

    fig = px.line(
        monthly_data,
        x="Order Date",
        y=["Sales", "Profit"],
        title="Monthly Sales and Profit Trend",
        markers=True
    )

    return fig

def create_yearly_trend_chart(df):

    yearly_data = (
        df
        .resample(
            "YE",
            on="Order Date"
        )[["Sales", "Profit"]]
        .sum()
        .reset_index()
    )

    fig = px.line(
        yearly_data,
        x="Order Date",
        y=["Sales", "Profit"],
        title="Yearly Sales and Profit Trend",
        markers=True
    )

    return fig

def create_top_products_chart(df):

    top_products = (
        df.groupby("Product Name")[["Sales", "Profit"]]
        .sum()
        .reset_index()
        .sort_values(
            by="Sales",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        top_products,
        x="Product Name",
        y=["Sales", "Profit"],
        title="Top 10 Products by Sales",
        barmode="group"
    )

    fig.update_layout(
        xaxis_title="Product",
        yaxis_title="Amount"
    )

    return fig