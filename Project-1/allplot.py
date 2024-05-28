import seaborn as sns 
import matplotlib.pyplot as plt 
  
  
sns.pairplot(df.drop(['Id'], axis = 1),  
             hue='Species', height=2)