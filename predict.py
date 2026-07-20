import joblib
import numpy as np

# Load trained model
model = joblib.load("diabetes_model.pkl")

# Load scaler
scaler = joblib.load("scaler.pkl")


def predict_diabetes(input_data):
    """
    Predict diabetes risk.

    Parameters:
        input_data (list): [
            Pregnancies,
            Glucose,
            BloodPressure,
            SkinThickness,
            Insulin,
            BMI,
            DiabetesPedigreeFunction,
            Age
        ]

    Returns:
        prediction (int): 0 or 1
        probability (float): confidence score
    """

    # Convert list to numpy array
    input_array = np.array(input_data).reshape(1, -1)

    # Scale input
    input_scaled = scaler.transform(input_array)

    # Prediction
    prediction = model.predict(input_scaled)[0]

    # Probability
    probability = model.predict_proba(input_scaled)[0][1]

    return int(prediction), float(probability)


# Test the model directly
if __name__ == "__main__":

    sample = [
        2,      # Pregnancies
        120,    # Glucose
        70,     # BloodPressure
        20,     # SkinThickness
        85,     # Insulin
        28.5,   # BMI
        0.35,   # DiabetesPedigreeFunction
        35      # Age
    ]

    prediction, probability = predict_diabetes(sample)

    print("Prediction :", prediction)

    if prediction == 1:
        print("Result : High Risk of Diabetes")
    else:
        print("Result : Low Risk of Diabetes")

    print("Probability :", round(probability * 100, 2), "%")
