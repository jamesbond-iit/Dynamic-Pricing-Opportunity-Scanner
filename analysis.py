import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
df=pd.read_csv("data/pricing_sales_data.csv")
m=df[(df.listed_price>0)&(df.units_sold>0)].copy(); X=np.log(m[["listed_price"]]); y=np.log(m.units_sold); model=LinearRegression().fit(X,y)
print("Rows:",len(df)); print("Revenue:",round(df.revenue.sum(),2)); print("Estimated price elasticity:",round(model.coef_[0],3)); print("R-squared:",round(model.score(X,y),3))