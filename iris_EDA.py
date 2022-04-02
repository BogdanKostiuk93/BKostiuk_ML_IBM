from sklearn.datasets import load_iris
iris = load_iris()
# print(iris)

import pandas as pd

ir=pd.DataFrame(iris.data)
ir.columns=iris.feature_names
ir['CLASS']=iris.target
print(ir.head(100))


