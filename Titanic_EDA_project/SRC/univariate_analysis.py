import matplotlib.pyplot as plt
import seaborn as sns

def univariate_analysis(df):

    plt.figure(figsize=(6,4))
    sns.countplot(x='Survived', data=df)
    plt.title("Survival Distribution")
    plt.savefig("outputs/survival_distribution.png")
    plt.show()

    plt.figure(figsize=(8,5))
    sns.histplot(df['Age'], bins=30, kde=True)
    plt.title("Age Distribution")
    plt.savefig("outputs/age_distribution.png")
    plt.show()

    plt.figure(figsize=(8,5))
    sns.histplot(df['Fare'], bins=40, kde=True)
    plt.title("Fare Distribution")
    plt.savefig("outputs/fare_distribution.png")
    plt.show()

    plt.figure(figsize=(6,4))
    sns.boxplot(y=df['Age'])
    plt.title("Age Boxplot")
    plt.show()