import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


def main():
    st.subheader("Data Visualization Charts for E-Commerce Dataset [Kaggle]")

    df = pd.read_csv("E-commerce Dataset.csv")

    option = st.selectbox("Choose the Chart type",
                          ("Bar Gender", "Bar Grouped", "Bar Sales", "Bubble", "Line", "Pie", "Scatter"))

    if option == "Bar Gender":
        # get the value counts of the "gender" column
        gender_counts = df["Gender"].value_counts()

        # create a bar plot
        gender_counts.plot.bar()

        # add value labels to the chart
        for i in range(len(gender_counts)):
            plt.text(i, gender_counts[i], gender_counts[i], ha="center", va="bottom")

        # set the title and axis labels
        plt.title("Gender Counts")
        plt.xlabel("Gender")
        plt.ylabel("Count")

        st.pyplot(plt, use_container_width=True)

    elif option == "Bar Grouped":
        # group dataframe by product and sum the profit and sales columns
        grouped_df = df.groupby("Product").sum()[["Profit", "Sales"]]

        # create bar chart using matplotlib
        fig, ax = plt.subplots()
        grouped_df.plot(kind="bar", ax=ax, fontsize=8)

        # set labels and title
        ax.set_xlabel("Product Category")
        ax.set_ylabel("Profit")
        ax.set_title("Revenue by Product")

        st.pyplot(fig, use_container_width=True)

    elif option == "Bar Sales":
        # Group the product column by the sum of the profit column and sort it in descending order
        data = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)

        # Create a bar chart using Matplotlib
        fig, ax = plt.subplots()
        ax.bar(data.index, data.values)
        ax.set_xticks(data.index)
        ax.set_xticklabels(data.index, rotation=90, fontsize=8)
        ax.set_xlabel("Products")
        ax.set_ylabel("Sales")
        ax.set_title("Sales by Product")

        # Use Streamlit to display the chart
        st.pyplot(fig, use_container_width=True)

    elif option == "Bubble":
        # Group the data by product and calculate the total sales
        grouped_data = df.groupby("Product")["Profit"].sum().reset_index()

        # Create the bubble chart
        fig = px.scatter(grouped_data, x="Product", y="Profit", size="Profit", hover_data=["Profit"])

        # Display the chart using Streamlit
        st.plotly_chart(fig)

    elif option == "Line":
        # Convert date column from string to datetime data type
        df["date"] = pd.to_datetime(df["Order_Date"])

        # Group sales data by month and find total sales for each month
        monthly_sales = df.groupby(pd.Grouper(key="date", freq="M")).sum()

        # Display line chart with month-wise sales data
        st.line_chart(monthly_sales["Sales"], y="Sales", use_container_width=True)

    elif option == "Pie":
        fig = px.pie(df, values="Sales", names="Product")
        fig.update_layout(
            autosize=False,
            width=1600,
            height=800
        )
        st.plotly_chart(fig, use_container_width=True)

    elif option == "Scatter":
        # Scatter plot with grid
        fig = px.scatter(df, x="Product", y="Sales", title="Sales by Product Category",
                         marginal_x="histogram", color="Product_Category")

        # Display plot
        st.plotly_chart(fig, use_container_width=True)

    else:
        pass

    st.dataframe(df, use_container_width=True)


if __name__ == "__main__":
    main()
