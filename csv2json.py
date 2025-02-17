import pandas as pd
import json

csv_file_path = 'input.csv'

json_file_path = 'output.json'

df = pd.read_csv(csv_file_path)

print(df)

json_data = df.to_json(orient='index')

with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=4)

print("CSVからJSONに変換が完了しました！")
