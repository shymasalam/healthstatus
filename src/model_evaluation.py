import os
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

os.makedirs("artifacts/plots", exist_ok=True)

def evaluate_model(
    model,
    X_test,
    y_test
):

    y_pred = model.predict(X_test)

    print(
        "Accuracy:",
        accuracy_score(y_test, y_pred)
    )

    print(
        classification_report(
            y_test,
            y_pred
        )
    )

    cm = confusion_matrix(
        y_test,
        y_pred
    )

    plt.figure(figsize=(6,5))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues"
    )

    plt.title("Confusion Matrix")

    plt.savefig(
        "artifacts/plots/confusion_matrix.png"
    )

    plt.close()