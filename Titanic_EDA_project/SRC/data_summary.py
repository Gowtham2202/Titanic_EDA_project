def dataset_summary(df):

    print("\nFIRST 5 RECORDS")
    print(df.head())

    print("\nDATASET INFO")
    print(df.info())

    print("\nSTATISTICAL SUMMARY")
    print(df.describe())

    print("\nMISSING VALUES")
    print(df.isnull().sum())