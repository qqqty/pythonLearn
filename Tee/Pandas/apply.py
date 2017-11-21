import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(3, 4))
df['sex'] = ['boy', 'boy', 'girl']

#
#
# print df
# print '---------------'
dfRes = pd.concat([df, df], ignore_index=True)
dfRes['age'] = ['15', '15', '15', '18', '16', '16']
print dfRes
print '--------------------'

print dfRes.groupby(['sex', 'age']).sum()


dfRes.to_csv('s/pandas.csv')
#dfRes.to_excel('s/pandas.xlsx', sheet_name='demo')




# mathR = pd.DataFrame({'key':['aa', 'bb'], 'math':[85,90]})
# musicR = pd.DataFrame({'key':['aa', 'bb'], 'music':[66,77]})
#
# print mathR
# print musicR
#
# print '-------------'
# print pd.merge(mathR, musicR, on='key')















