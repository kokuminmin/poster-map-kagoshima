# エリアリストをjsonに変換

import pandas as pd
import json

csv_file_path = 'arealist.csv'

json_file_path = 'arealist.json'

df = pd.read_csv(csv_file_path)

df = df.set_index('area_id')

json_data = df.to_json(orient='index',force_ascii=False)

with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json_file.write(json_data)

print("CSVからJSONに変換が完了しました！")
