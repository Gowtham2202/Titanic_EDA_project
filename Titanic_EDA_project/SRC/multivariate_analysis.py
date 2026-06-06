import matplotlib.pyplot as plt
import seaborn as sns

def multivariate_analysis(df):

    numeric_df = df.select_dtypes(
        include=['number']
    )

    plt.figure(figsize=(10,6))
    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap='coolwarm'
    )
    plt.title("Correlation Heatmap")
    plt.savefig("outputs/heatmap.png")
    plt.show()

    sns.pairplot(
        df[['Survived','Age','Fare','Pclass']]
    )
    plt.savefig("outputs/pairplot.png")
    plt.show()