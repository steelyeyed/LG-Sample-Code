import pandas as pd 
#print ('Larry')
#drinks = pd.read_csv('https://bit.ly/drinksbycountry', index_col='country')
#drinks.head()
#drinks.count()
drinks = pd.read_csv('http://bit.ly/drinksbycountry', index_col='country')
print (drinks.head())