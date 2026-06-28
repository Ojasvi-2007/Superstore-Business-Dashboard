def calculate_kpis(df):

    total_sales = round(df["Sales"].sum(), 2)

    total_profit = round(df["Profit"].sum(), 2)

    total_orders = df["Order ID"].nunique()

    total_customers = df["Customer ID"].nunique()

    profit_margin = round(
        (total_profit / total_sales) * 100,
        2
    )

    result = {
        "Total Sales": total_sales,
        "Total Profit": total_profit,
        "Total Orders": total_orders,
        "Total Customers": total_customers,
        "Profit Margin": profit_margin
    }

    return result