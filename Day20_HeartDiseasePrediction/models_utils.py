import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import os

def preprocess_data(df):
    # Drop rows with missing values
    df = df.dropna()

    # Convert categorical columns to numeric (one-hot encoding or label encoding)
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype('category').cat.codes

    # Features and target
    X = df.drop("HeartDisease", axis=1)
    y = df["HeartDisease"]

    return X, y, X.columns.tolist()


def train_and_evaluate(X, y):
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    importances = model.feature_importances_

    return accuracy, importances, y_pred

def plot_feature_importance(feature_names, importances, filename="plots/feature_importance.png"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Plotting
    plt.figure(figsize=(10,6))
    sorted_indices = importances.argsort()[::-1]
    sorted_features = [feature_names[i] for i in sorted_indices]
    sorted_importances = importances[sorted_indices]

    plt.barh(sorted_features, sorted_importances, color="skyblue")
    plt.xlabel("Importance")
    plt.title("Feature Importance")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    print(f"Feature importance plot saved as {filename}")
