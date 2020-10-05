import sys
import json
import pandas as pd

with open(sys.argv[1]) as f:
  data = json.load(f)

df = pd.DataFrame(data=data.values(), index=data.keys())
df.to_csv('New_approach.csv')