import pandas as pd
data = pd.read_csv("./files/articles.csv", encoding = 'latin1')
print(data.head())


data["Number of Words"] = data["Article"].apply(lambda n: len(n.split()))
print(data.head())