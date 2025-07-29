import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
from models_utils import preprocess_data, train_and_evaluate, plot_feature_importance

def plot_correlation_heatmap(df, filename="plots/correlation_heatmap.png"):
    plt.figure(figsize=(10,8))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"Correlation heatmap saved as {filename}")

def generate_report(accuracy, feature_names, importances, report_file="report.txt"):
    lines = [
        "📊 Heart Disease Prediction Report",
        "----------------------------------",
        f"Model Accuracy: {accuracy:.2%}",
        "Top Features:"
    ]
    for name, imp in sorted(zip(feature_names, importances), key=lambda x: -x[1])[:5]:
        lines.append(f"{name}: {imp:.3f}")
    summary = "\n".join(lines)
    print(summary)
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(summary)

def summarize_risk(y_pred):
    total = len(y_pred)
    at_risk = np.sum(y_pred)
    not_at_risk = total - at_risk
    risk_percent = (at_risk / total) * 100

    print(f"\n Total People Tested: {total}")
    print(f" People Predicted at Risk of Heart Disease: {at_risk}")
    print(f" People Predicted NOT at Risk: {not_at_risk}")
    print(f" Percentage at Risk: {risk_percent:.2f}%")

if __name__ == "__main__":
    os.makedirs("plots", exist_ok=True)
    df = pd.read_csv("data.csv")
    plot_correlation_heatmap(df)
    
    X, y, feature_names = preprocess_data(df)
    
    # Get accuracy, feature importances, and predictions
    accuracy, importances, y_pred = train_and_evaluate(X, y)
    
    plot_feature_importance(feature_names, importances, filename="plots/feature_importance.png")
    generate_report(accuracy, feature_names, importances)
    
    # Risk Summary Output
    summarize_risk(y_pred)