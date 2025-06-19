import pandas as pd
from pandas.core.computation.ops import BinOp

data={"Name":["Alice","Bob", "Charlie"],
      "Age": [25,30.32],
      "City":["New York", "San Francisco", "Los Angeles"]
      }

df=pd.DataFrame(data)
print(df)