import streamlit as st
import pandas as pd
import plotly.express as px
from odata_client import fetch_odata_entity

st.set_page_config(page_title="D365FO KPI Dashboard", layout="wide")

st.title("📊 D365FO Multi-Entity KPI Dashboard")

# Tabs for multiple entities
tabs = st.tabs(["🏢 Vendors", "👥 Customers", "📦 Sales Orders"])

# ---------- TAB 1: Vendors ----------
with tabs[0]:
    st.subheader("Vendor KPIs (VendorsV2)")
    try:
        vendors = fetch_odata_entity("VendorsV2")
        st.dataframe(vendors.head(20))

        if "CreatedBy" in vendors.columns:
            counts = vendors["CreatedBy"].value_counts().reset_index()
            counts.columns = ["CreatedBy", "Count"]
            fig = px.bar(counts, x="CreatedBy", y="Count", title="Vendors Created by User")
            st.plotly_chart(fig, use_container_width=True)

        if "CreatedDateTime" in vendors.columns:
            vendors["CreatedDateTime"] = pd.to_datetime(vendors["CreatedDateTime"], errors="coerce")
            over_time = vendors.groupby(vendors["CreatedDateTime"].dt.date).size().reset_index(name="Count")
            fig2 = px.line(over_time, x="CreatedDateTime", y="Count", title="Vendors Created Over Time")
            st.plotly_chart(fig2, use_container_width=True)

    except Exception as e:
        st.error(f"Error fetching Vendors: {e}")

# ---------- TAB 2: Customers ----------
with tabs[1]:
    st.subheader("Customer KPIs (CustomersV3)")
    try:
        customers = fetch_odata_entity("CustomersV3")
        st.dataframe(customers.head(20))

        if "CustomerGroupId" in customers.columns:
            group_counts = customers["CustomerGroupId"].value_counts().reset_index()
            group_counts.columns = ["CustomerGroupId", "Count"]
            fig3 = px.pie(group_counts, names="CustomerGroupId", values="Count", title="Customers by Group")
            st.plotly_chart(fig3, use_container_width=True)

        if "CreatedDateTime" in customers.columns:
            customers["CreatedDateTime"] = pd.to_datetime(customers["CreatedDateTime"], errors="coerce")
            cust_time = customers.groupby(customers["CreatedDateTime"].dt.date).size().reset_index(name="Count")
            fig4 = px.line(cust_time, x="CreatedDateTime", y="Count", title="Customers Created Over Time")
            st.plotly_chart(fig4, use_container_width=True)

    except Exception as e:
        st.error(f"Error fetching Customers: {e}")

# ---------- TAB 3: Sales Orders ----------
with tabs[2]:
    st.subheader("Sales Order KPIs (SalesOrderHeadersV2)")
    try:
        sales_orders = fetch_odata_entity("SalesOrderHeadersV2")
        st.dataframe(sales_orders.head(20))

        if "SalesOrderStatus" in sales_orders.columns:
            status_counts = sales_orders["SalesOrderStatus"].value_counts().reset_index()
            status_counts.columns = ["Status", "Count"]
            fig5 = px.bar(status_counts, x="Status", y="Count", title="Sales Orders by Status")
            st.plotly_chart(fig5, use_container_width=True)

        if "OrderTotalAmount" in sales_orders.columns:
            fig6 = px.histogram(sales_orders, x="OrderTotalAmount", nbins=20, title="Sales Order Total Amount Distribution")
            st.plotly_chart(fig6, use_container_width=True)

    except Exception as e:
        st.error(f"Error fetching Sales Orders: {e}")
