import pandas as pd
import json

csv_file_path = 'input.csv'

json_file_path = 'output.json'

df = pd.read_csv(csv_file_path)

json_data = df.to_json(orient='index',force_ascii=False)

print(json_data)


with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json_file.write(json_data)

print("CSVからJSONに変換が完了しました！")
