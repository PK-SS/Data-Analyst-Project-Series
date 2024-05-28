import seaborn as sns 
import matplotlib.pyplot as plt 
  
  
fig, axes = plt.subplots(2, 2, figsize=(10,10)) 
  
axes[0,0].set_title("Sepal Length") 
axes[0,0].hist(df['SepalLengthCm'], bins=7) 
  
axes[0,1].set_title("Sepal Width") 
axes[0,1].hist(df['SepalWidthCm'], bins=5); 
  
axes[1,0].set_title("Petal Length") 
axes[1,0].hist(df['PetalLengthCm'], bins=6); 
  
axes[1,1].set_title("Petal Width") 
axes[1,1].hist(df['PetalWidthCm'], bins=6);