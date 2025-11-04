import matplotlib.pyplot as plt
import seaborn as sns

def missing_values(df):
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    missing = missing.reset_index()
    missing.columns = ['column', 'count']

    plt.figure(figsize=(10, 4))
    sns.barplot(data=missing, x='column', y='count', hue='column', palette='tab10', legend=False)
    plt.title('Null values')
    plt.show()