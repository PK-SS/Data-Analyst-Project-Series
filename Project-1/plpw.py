import seaborn as sns 
import matplotlib.pyplot as plt 
  
  
sns.scatterplot(x='PetalLengthCm', y='PetalWidthCm', 
                hue='Species', data=df, ) 
  
# Placing Legend outside the Figure 
plt.legend(bbox_to_anchor=(1, 1), loc=2) 
  
plt.show()