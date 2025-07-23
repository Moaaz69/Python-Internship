import pandas as pd
import matplotlib.pyplot as plt
import os

def read_data(filename):
    ext = os.path.splitext(filename)[1].lower()
    if ext == ".csv":
        return pd.read_csv(filename)
    elif ext in [".xlsx", ".xls"]:
        return pd.read_excel(filename)
    else:
        raise ValueError("Unsupported file type.")

def generate_report(df, report_file="report.txt"):
    df["Revenue"] = df["Units Sold"] * df["Unit Price"]
    summary_lines = ["📊 Sales Summary"]
    for _, row in df.groupby("Product").sum(numeric_only=True).reset_index().iterrows():
        summary_lines.append(f"Product: {row['Product']} – Revenue: {int(row['Revenue'])}")
    total_revenue = int(df["Revenue"].sum())
    top_product = df.groupby("Product")["Revenue"].sum().idxmax()
    summary_lines.append(f"🔸 Total Revenue: {total_revenue}")
    summary_lines.append(f"🔸 Top Product: {top_product}")
    summary = "\n".join(summary_lines)
    print(summary)
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(summary)

def plot_bar_chart(df, filename="sales_bar_chart.png"):
    revenue_by_product = df.groupby("Product")["Revenue"].sum()
    plt.figure(figsize=(8,5))
    revenue_by_product.plot(kind="bar", color="skyblue")
    plt.title("Revenue by Product")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"Bar chart saved as {filename}")

if __name__ == "__main__":
    filename = input("Enter CSV or Excel filename (default: sales_data.csv): ").strip()
    if not filename:
        filename = "sales_data.csv"
    try:
        df = read_data(filename)
        generate_report(df)
        plot_bar_chart(df)
    except Exception as e:
        print(f"Error: {e}")