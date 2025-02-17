import csv
import json

csv_file_path = 'input.csv'

json_file_path = 'output.json'

# csvをjsonに変換する

with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    # csvデータを辞書形式で読み込む
    csv_reader = csv.DictReader(csv_file)

    # csvデータをリスト形式に変換
    data = [row for row in csv_reader]

# jsonファイルに書き込む
with open(csv_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
