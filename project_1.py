import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Retail Analytics Dashboard", layout="wide")

st.title("Retail Sales Intelligence & Performance Analytics")

@st.cache_data
def load_data():
    file_path = "data/retail_sales_1.csv"
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    return pd.DataFrame()

df = load_data()

if df.empty:
    st.warning("Data not found. Please ensure data/retail_sales_1.csv exists.")
    st.stop()

# Sidebar filters
st.sidebar.header("Filters")
selected_branches = st.sidebar.multiselect("Select Branch", df["Branch"].unique(), default=df["Branch"].unique())
selected_categories = st.sidebar.multiselect("Select Category", df["Category"].unique(), default=df["Category"].unique())

filtered_df = df[df["Branch"].isin(selected_branches) & df["Category"].isin(selected_categories)]

# KPIs
st.header("Executive Sales Overview")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Total Sales", f"${filtered_df['Sales'].sum():,.2f}")
kpi2.metric("Total Profit", f"${filtered_df['Profit'].sum():,.2f}")
kpi3.metric("Total Transactions", f"{len(filtered_df):,}")
margin = (filtered_df['Profit'].sum() / filtered_df['Sales'].sum()) * 100 if filtered_df['Sales'].sum() > 0 else 0
kpi4.metric("Profit Margin", f"{margin:.2f}%")

st.markdown("---")

tab1, tab2, tab3 = st.tabs(["Branch & Time Analysis", "Product & Category Performance", "Customer & Payment Insights"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        # Sales by Branch
        branch_sales = filtered_df.groupby("Branch")["Sales"].sum().reset_index()
        fig_branch = px.bar(branch_sales, x="Branch", y="Sales", title="Sales by Branch", color="Branch")
        st.plotly_chart(fig_branch, use_container_width=True)
    with col2:
        # Monthly Sales Trend
        filtered_df['Month'] = pd.to_datetime(filtered_df['Date']).dt.to_period('M').astype(str)
        monthly_trend = filtered_df.groupby("Month")["Sales"].sum().reset_index()
        fig_trend = px.line(monthly_trend, x="Month", y="Sales", markers=True, title="Monthly Sales Trend")
        st.plotly_chart(fig_trend, use_container_width=True)

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        cat_profit = filtered_df.groupby("Category")["Profit"].sum().reset_index()
        fig_cat = px.bar(cat_profit, x="Category", y="Profit", title="Profit by Category", color="Category")
        st.plotly_chart(fig_cat, use_container_width=True)
    with col2:
        top_products = filtered_df.groupby("Product")["Sales"].sum().reset_index().sort_values(by="Sales", ascending=False).head(5)
        fig_top = px.bar(top_products, x="Sales", y="Product", orientation="h", title="Top 5 Products by Sales")
        st.plotly_chart(fig_top, use_container_width=True)

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        cust_sales = filtered_df.groupby("Customer_Type")["Sales"].sum().reset_index()
        fig_cust = px.pie(cust_sales, names="Customer_Type", values="Sales", title="Sales Contribution by Customer Type")
        st.plotly_chart(fig_cust, use_container_width=True)
    with col2:
        pay_sales = filtered_df.groupby("Payment_Method")["Sales"].sum().reset_index()
        fig_pay = px.pie(pay_sales, names="Payment_Method", values="Sales", title="Sales by Payment Method", hole=0.4)
        st.plotly_chart(fig_pay, use_container_width=True)
