def select_features(data):

    selected_features = [
        "Age",
        "BMI",
        "Weight_kg",
        "Height_cm",
        "Daily_Calorie_Consumed",
        "Calorie_Balance"
    ]

    X = data[selected_features]
    y = data["Health_Status"]

    return X, y