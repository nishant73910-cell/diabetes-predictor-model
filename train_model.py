import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# -----------------------------
# Load Dataset
# -----------------------------
data = pd.read_csv("dataset/diabetes.csv")

# -----------------------------
# Replace invalid zero values
# -----------------------------
columns = [
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI"
]

for col in columns:
    data[col] = data[col].replace(0, data[col].median())

# -----------------------------
# Split Features and Target
# -----------------------------
X = data.drop("Outcome", axis=1)
y = data["Outcome"]

# -----------------------------
# Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Feature Scaling
# -----------------------------
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# -----------------------------
# Train Model
# -----------------------------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------
# Prediction
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# Accuracy
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)

print("="*40)
print("Model Accuracy :", round(accuracy*100,2),"%")
print("="*40)

print("\nConfusion Matrix\n")
print(confusion_matrix(y_test,y_pred))

print("\nClassification Report\n")
print(classification_report(y_test,y_pred))

# -----------------------------
# Save Model
# -----------------------------
joblib.dump(model,"model/diabetes_model.pkl")
joblib.dump(scaler,"model/scaler.pkl")

print("\nModel Saved Successfully.")