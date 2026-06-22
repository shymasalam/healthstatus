import pandas as pd

def feature_engineering(data):

    data['Calorie_Balance'] = (
        data['Daily_Calorie_Consumed']
        - data['Daily_Calorie_Requirement']
    )

    data['Protein_Per_Weight'] = (
        data['Protein_Intake_g']
        / data['Weight_kg']
    )

    data['Age_Group'] = pd.cut(
        data['Age'],
        bins=[0,18,35,50,100],
        labels=[
            'Teen',
            'Young Adult',
            'Adult',
            'Senior'
        ]
    )

    data['Weight_Category'] = pd.cut(
        data['Weight_kg'],
        bins=[0,50,70,90,200],
        labels=[
            'Low',
            'Normal',
            'High',
            'Very High'
        ]
    )

    data.to_csv(
        "feature_engineered.csv",
        index=False
    )

    return data