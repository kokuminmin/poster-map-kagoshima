import pandas as pd
import json

csv_file_path = 'input.csv'

json_file_path = 'output.json'

df = pd.read_csv(csv_file_path)

print(df)

result = (
    df.groupby(['area_id'])
    .apply(lambda group:{
        "area_name": group.area_id[0],
        "area_block": group.area_id[1]
    })
    .tolist()
)

print(result)

exit

#with open(json_file_path, mode='w', encoding='utf-8') as json_file:
#    json.dump(result, json_file, ensure_ascii=False, indent=4)
#
#print(f"JSON 生成: {json_file_path}")

