import numpy as np
import pandas as pd

# s = pd.Series([1,3,5,np.nan,6,8])
# print s, type(s)





dates = pd.date_range('20150226', periods=6)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print df
print '-------------------------------'
# print df.head(1)
# print df.tail(1)
#
# print df.describe()
#
# print df['A']
# print df[['A','C']]
# print df[0:3]

# print df.loc[dates[0:3]]

# print df.loc[:, ['A', 'B']]

# print df.loc[dates[0], 'A']
# print df.at[dates[0], 'A']
#
# print df.iloc[0:3, 0:2]
# print df.iloc[[0,3], [0, 2]]

# print df[df > 0]
df.at[dates[0], 'B'] = np.nan
df.iat[3, 3] = np.nan
dfTmp = df.copy()
# dfTmp['E'] = ['one', 'ff', 'add'] * 2
# print dfTmp
# print dfTmp[dfTmp['E'].isin(['ff', 'add'])]

print df
print df.isnull()
print df.dropna(how='any')

print '---------------------------'
print dfTmp
print df.fillna(value=3.33)













