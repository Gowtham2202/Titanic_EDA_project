import matplotlib.pyplot as plt
import seaborn as sns

def bivariate_analysis(df):

    plt.figure(figsize=(6,4))
    sns.countplot(
        x='Sex',
        hue='Survived',
        data=df
    )
    plt.title("Gender vs Survival")
    plt.savefig("outputs/gender_survival.png")
    plt.show()

    plt.figure(figsize=(6,4))
    sns.countplot(
        x='Pclass',
        hue='Survived',
        data=df
    )
    plt.title("Class vs Survival")
    plt.savefig("outputs/class_survival.png")
    plt.show()

    plt.figure(figsize=(8,5))
    sns.boxplot(
        x='Survived',
        y='Fare',
        data=df
    )
    plt.title("Fare vs Survival")
    plt.savefig("outputs/fare_survival.png")
    plt.show()

    plt.figure(figsize=(8,5))
    sns.boxplot(
        x='Survived',
        y='Age',
        data=df
    )
    plt.title("Age vs Survival")
    plt.savefig("outputs/age_survival.png")
    plt.show()
    