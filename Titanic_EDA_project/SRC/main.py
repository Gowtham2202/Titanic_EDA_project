from load_data import load_dataset
from data_summary import dataset_summary
from univariate_analysis import univariate_analysis
from bivariate_analysis import bivariate_analysis
from multivariate_analysis import multivariate_analysis

def main():

    df = load_dataset()

    dataset_summary(df)

    univariate_analysis(df)

    bivariate_analysis(df)

    multivariate_analysis(df)

    print("\nEDA COMPLETED SUCCESSFULLY")

if __name__ == "__main__":
    main()