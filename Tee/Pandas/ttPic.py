import numpy as np
import pandas as pd
import matplotlib


ts = pd.DataFrame(np.random.randn(1000, 4), index=pd.date_range('20050101', periods=1000), columns=list('ABCD'))
ts = ts.cumsum()

ts.plot()
matplotlib.pyplot.show()











