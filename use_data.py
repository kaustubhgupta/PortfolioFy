import os
import sys
import json
import pandas as pd

path = sys.argv[1]
with open(os.path.join(path, 'data.json')) as f:
  data = json.load(f)

df = pd.DataFrame(data=data.values(), index=data.keys())
df.to_csv('New_approach.csv')