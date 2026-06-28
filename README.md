# 📊 Superstore Business Dashboard

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge\&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge\&logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Visualization-3F4F75?style=for-the-badge\&logo=plotly)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-EF4B4B?style=for-the-badge\&logo=streamlit)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-Excel%20Support-green?style=for-the-badge)

---

## 🚀 Project Overview

The **Superstore Business Dashboard** is an interactive business intelligence dashboard built using **Pandas, Plotly, and Streamlit**.

The dashboard allows users to explore sales performance, profitability, customer segments, product categories, and regional trends through interactive filters and visualizations.

This project demonstrates the complete analytics workflow from **data loading and preprocessing** to **business KPI generation and interactive dashboard creation**.

---

## 🎯 Objectives

* Analyze sales and profitability performance.
* Identify high-performing and low-performing regions.
* Compare category-wise business performance.
* Explore monthly business trends.
* Provide an interactive decision-support dashboard.

---

## 📂 Dataset

The project uses the classic **Superstore Dataset**, containing:

* Orders
* Customers
* Products
* Sales
* Profit
* Regions
* Categories
* Shipping Information

Dataset size:

* **9,994 Rows**
* **21 Columns**

---

## 📈 Dashboard Features

### 📌 Key Performance Indicators (KPIs)

* Total Sales
* Total Profit
* Total Orders
* Total Customers
* Profit Margin

---

### 🔍 Interactive Filters

Users can dynamically filter the dashboard using:

* Region
* Category
* Segment
* Date Range

---

### 📊 Visualizations

#### Monthly & Yearly Sales and Profit Trend

Track business growth and seasonal patterns over time.

#### Sales and Profit by Category

Compare category performance using grouped bar charts.

#### Sales and Profit by Region

Identify profitable and underperforming regions.

#### Top Products Analysis

Discover the products contributing most to revenue and profit.

---

## 🛠 Technologies Used

| Technology | Purpose                    |
| ---------- | -------------------------- |
| Python     | Programming Language       |
| Pandas     | Data Manipulation          |
| Plotly     | Interactive Visualizations |
| Streamlit  | Dashboard Development      |
| OpenPyXL   | Excel File Handling        |

---

## 📁 Project Structure

```text
Superstore_Dashboard/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └──Sample - Superstore.xlsx
│
|── src/
    ├── loader.py
    ├── filters.py
    ├── charts.py
    └── kpi_calculator.py
```

---

## 🧠 Skills Demonstrated

### Data Analysis

* Data Loading
* Data Cleaning
* Aggregation
* Filtering
* Time Series Analysis

### Data Visualization

* Interactive Charts
* KPI Design
* Dashboard Layout
* Business Reporting

### Business Analytics

* Sales Analysis
* Profitability Analysis
* Regional Analysis
* Product Performance Analysis

### Software Development

* Modular Code Structure
* Git and GitHub Workflow
* Virtual Environments
* Project Documentation

---

## 📷 Dashboard Preview

Add screenshots of your dashboard here after deployment.

Example:

```markdown
![Dashboard Screenshot](images/dashboard.png)
```

---

## ⚡ Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_LINK
```

Move into the project directory:

```bash
cd Superstore_Dashboard
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / MacOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🎓 Learning Outcomes

This project helped develop practical experience in:

* Building interactive dashboards
* Handling business datasets
* Creating professional visualizations
* Performing business analytics
* Structuring production-style data projects

---

## 📌 Future Improvements

* Customer segmentation analysis
* Forecasting future sales trends
* Deployment on Streamlit Cloud
* Advanced business KPIs
* Predictive analytics integration

---

## 👨‍💻 Author

**Ojasvi Kumar**

BS in Data Science and Applications
Indian Institute of Technology Madras

Passionate about Data Analytics, Data Science, Machine Learning, and building impactful AI solutions.

---
