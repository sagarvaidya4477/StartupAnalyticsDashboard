import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import millify

st.set_page_config(layout="wide", page_title="Startup Dashboard")

df = pd.read_csv("Cleaned_Startup.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.drop_duplicates(subset=["Startup", "Industry", "Investors"]).reset_index(drop=True)
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month_name().str[:3]


def overall_analysis():
    st.title("Overall Analysis")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Total Startups", millify.millify(df["Startup"].nunique()))
    with col2:
        st.metric("Total Funding", millify.millify(df["Turnover"].sum()) + " Cr")
    with col3:
        st.metric("Max Funded Startup", df.groupby("Startup")["Turnover"].sum().sort_values(ascending = False).head(1).index[0])
    with col4:
        st.metric("Max Funding", millify.millify(df.groupby("Startup")["Turnover"].sum().sort_values(ascending = False).head(1).values[0]) + " Cr")
    with col5:
        st.metric("Average Funding", str(round(df.groupby("Startup")["Turnover"].sum().mean())) + " Cr")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Location Analysis")
        location_series = df["Locations"].value_counts().head(7)
        location_fig, location_ax = plt.subplots()
        location_ax.pie(location_series.values, labels=location_series.index, autopct="%0.0f%%")
        st.pyplot(location_fig)

    with col2:
        st.subheader("Type Analysis")
        type_series = df["Type"].value_counts().head()
        type_fig, type_ax = plt.subplots()
        type_ax.bar(type_series.index, type_series.values)
        st.pyplot(type_fig)

    st.subheader("Month-Year Analysis")
    choice = st.selectbox("Select an option", ["Total Startups", "Total Funding"])

    if choice == "Total Startups":
        temp_df = df.groupby(["Year", "Month"])["Startup"].count().reset_index()
        temp_df["mon_yr"] = temp_df["Month"] + " - " + temp_df["Year"].astype(str)

        temp_fig, temp_ax = plt.subplots()
        temp_ax.plot(temp_df["mon_yr"], temp_df["Startup"])
        plt.xticks(rotation = 90)
        st.pyplot(temp_fig)
    else:
        temp_df = df.groupby(["Year", "Month"])["Turnover"].sum().reset_index()
        temp_df["mon_yr"] = temp_df["Month"] + " - " + temp_df["Year"].astype(str)

        temp_fig, temp_ax = plt.subplots()
        temp_ax.plot(temp_df["mon_yr"], temp_df["Turnover"])
        plt.xticks(rotation=90)
        st.pyplot(temp_fig)


def investor_analysis(investor):
    st.header(investor)
    st.subheader("Recent Investments")
    inv_df = df[df["Investors"].str.contains(investor)].drop(columns='Investors').sort_values("Date",
                                                                                              ascending=False).head()
    st.dataframe(inv_df)

    st.subheader("Biggest Investments")
    big_df = df[df["Investors"].str.contains(investor)].groupby("Startup")["Turnover"].sum().sort_values(
        ascending=False).head().reset_index().set_index("Startup").T
    st.dataframe(big_df)

    col1, col2 = st.columns(2)

    with col1:
        st.write("Biggest Investment Analysis")
        big_fig, big_ax = plt.subplots()
        big_ax.bar(big_df.columns, big_df.iloc[0].values)
        st.pyplot(big_fig)

    with col2:
        st.write("Industry Analysis")
        industry_series = df["Industry"][df["Investors"].str.contains(investor)].value_counts().head()
        industry_fig, industry_ax = plt.subplots()
        industry_ax.pie(industry_series.values, labels=industry_series.index, autopct="%0.0f%%")
        st.pyplot(industry_fig)

    st.subheader("Year on Year Analysis")
    year_series = df[df["Investors"].str.contains(investor)].groupby("Year")["Turnover"].sum()
    year_fig, year_ax = plt.subplots()
    year_ax.plot(year_series.index, year_series.values)
    st.pyplot(year_fig)


st.sidebar.title('Startup Analysis')
option = st.sidebar.selectbox("Select an option", ["Overall Analysis", "Startup Analysis", "Investor Analysis"])

if option == "Overall Analysis":
    overall_analysis()
elif option == "Startup Analysis":
    st.sidebar.selectbox("Select a Startup", df["Startup"].unique())
    st.sidebar.button("Show Startup Analysis")
else:
    selected_investor = st.sidebar.selectbox("Select a Investor", sorted(set(df["Investors"].str.split(", ").sum())))
    investor_btn = st.sidebar.button("Show Investor Analysis")

    if investor_btn:
        investor_analysis(selected_investor)
