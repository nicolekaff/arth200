import pandas as pd
import sys

# Run with: python3 excell_to_json.py EXCELL_FILE_NAME

df = pd.read_excel(sys.argv[1])
df= df.rename(columns=str.lower)

for i in df.index:
    name = df.iloc[i]['Image']
    prefix = name.split(".")[0]
    df.loc[i].to_json("{}.json".format(prefix))


