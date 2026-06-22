def clean_data(data):

    print("Dataset Info")
    print(data.info())

    print("\nDescription")
    print(data.describe())

    print("\nDuplicates:")
    print(data.duplicated().sum())

    print("\nNull Values:")
    print(data.isna().sum())

    data.to_csv(
        "cleaned_data.csv",
        index=False
    )

    return data