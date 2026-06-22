import numpy as np
import joblib
import os
from sklearn.preprocessing import LabelEncoder

os.makedirs("artifacts/models", exist_ok=True)

def transform_data(data):

    le = LabelEncoder()

    data["Health_Status"] = le.fit_transform(
        data["Health_Status"]
    )

    joblib.dump(
        le,
        "artifacts/models/label_encoder.pkl"
    )

    data["Protein_Intake_g"] = np.log1p(
        data["Protein_Intake_g"]
    )

    return data