import seaborn as sns
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
df.info()

# ----------------------------------------------------------

# Regressão Linear Simples
# x = total_bill
# y = tip

X = df["total_bill"]
Y = df["tip"]

# Adiciona o intercepto

x = sm.add_constant(X)
modelo = sm.OLS(Y, x).fit()
print(modelo.summary())


# plot

sns.lmplot(data=df, x="total_bill", y="tip")