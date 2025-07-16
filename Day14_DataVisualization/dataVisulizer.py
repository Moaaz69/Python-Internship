import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("plots", exist_ok=True)

def save_plot(fig, filename):
    fig.savefig(f"plots/{filename}", bbox_inches='tight')
    plt.close(fig)
df = pd.read_csv("sales.csv", encoding="latin1")

df.dropna(inplace=True)

# Ensure proper date parsing if there’s a date column
if 'Order Date' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df.dropna(subset=['Order Date'], inplace=True)
    df['YearMonth'] = df['Order Date'].dt.to_period('M')

# Line Chart — Monthly Sales
if 'YearMonth' in df.columns and 'Sales' in df.columns:
    monthly_sales = df.groupby('YearMonth')['Sales'].sum()
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    ax1.plot(monthly_sales.index.astype(str), monthly_sales.values, marker='o', color='green')
    ax1.set_title("Monthly Sales")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Sales")
    ax1.tick_params(axis='x', rotation=45)
    ax1.grid(True)
    save_plot(fig1, "Line_Chart_Monthly_Sales.png")

# Bar Chart — Sales by Category
if 'Category' in df.columns and 'Sales' in df.columns:
    category_sales = df.groupby('Category')['Sales'].sum()
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    ax2.bar(category_sales.index, category_sales.values, color='skyblue')
    ax2.set_title("Sales by Category")
    ax2.set_xlabel("Category")
    ax2.set_ylabel("Sales")
    save_plot(fig2, "Bar_Chart_Sales_by_Category.png")

# Pie Chart — Orders by Region
if 'Region' in df.columns:
    region_counts = df['Region'].value_counts()
    fig3, ax3 = plt.subplots(figsize=(7, 7))
    ax3.pie(region_counts.values, labels=region_counts.index, autopct='%1.1f%%', startangle=140)
    ax3.set_title("Orders by Region")
    save_plot(fig3, "Pie_Chart_Orders_by_Region.png")

# Heatmap — Correlation of numeric columns
fig4, ax4 = plt.subplots(figsize=(10, 8))
corr = df.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax4)
ax4.set_title("Correlation Heatmap")
save_plot(fig4, "Heatmap_Correlation.png")

summary_text = """
Data Visualization Summary Report

✅ Line_Chart_Monthly_Sales.png   : Total Sales per Month
✅ Bar_Chart_Sales_by_Category.png: Total Sales by Product Category
✅ Pie_Chart_Orders_by_Region.png : Proportion of Orders by Region
✅ Heatmap_Correlation.png        : Correlation among numerical variables

All plots saved in the 'plots/' folder.
"""

with open("plots/Summary_Report.txt", "w", encoding="utf-8") as report_file:
    report_file.write(summary_text)

print("🎉 All plots and report generated in the 'plots/' folder.")
