import pandas as pd

import quandl
from Tools.scripts.dutree import display

df =pd.DataFrame (quandl.get('HKEX/01255'))
authtoken ="DEWrRf6VzQuNdn1jH29e"
print(df.head(n=20))

