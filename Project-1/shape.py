df.shape()

df.info()

df.describe()

df.isnull().sum()

data = df.drop_duplicates(subset ="Species",) 
data

df.value_counts("Species")


