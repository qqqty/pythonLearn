import numpy as np

import pandas as pd



dates = pd.date_range('20150628', periods=10)

pf = pd.DataFrame(np.random.rand(10, 3), index=dates, columns=list('abc'))

print pf
print '-----------------------'
# print pf.mean()
# print pf.mean(1)

# s = pd.Series([1,2,3,4,5,6,7,8,9,19], index=dates).shift(-3)
# print s
#
# print pf.sub(s, axis='index')

print pf.apply(lambda x: x.max() - x.min())
print pf.apply(np.cumsum)










