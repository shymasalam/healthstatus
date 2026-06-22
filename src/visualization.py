import os
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("artifacts/plots", exist_ok=True)

def visualize_data(data):

    # Box Plot
    plt.figure(figsize=(6,5))
    sns.boxplot(
        x='Activity_Level',
        y='Daily_Calorie_Consumed',
        data=data
    )
    plt.savefig("artifacts/plots/boxplot.png")
    plt.close()

    # Pie Chart
    data['Diet_Type'].value_counts().plot(
        kind='pie',
        autopct='%1.1f%%'
    )
    plt.savefig("artifacts/plots/diet_type_pie.png")
    plt.close()

    # BMI Histogram
    plt.figure(figsize=(6,5))
    plt.hist(data['BMI'], bins=10)
    plt.savefig("artifacts/plots/bmi_distribution.png")
    plt.close()

    # Scatter Plot
    plt.figure(figsize=(6,5))
    sns.scatterplot(
        x='Weight_kg',
        y='BMI',
        data=data
    )
    plt.savefig("artifacts/plots/weight_vs_bmi.png")
    plt.close()

    # Line Plot
    plt.figure(figsize=(6,5))
    sns.lineplot(
        x='Age',
        y='Daily_Calorie_Consumed',
        data=data
    )
    plt.savefig("artifacts/plots/age_vs_calorie.png")
    plt.close()

    # Heatmap
    plt.figure(figsize=(10,8))
    sns.heatmap(
        data.corr(numeric_only=True),
        annot=True
    )
    plt.savefig("artifacts/plots/heatmap.png")
    plt.close()