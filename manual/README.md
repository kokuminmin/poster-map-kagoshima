# poster-mapの使い方
## 概要
* このシステムは安野たかひろさんチームが公開したオープンソースを元にカスタマイズしたものです
* Googleスプレッドシートに入れたデータをnetlifyで作ったサイトに自動デプロイするまでの手順を記します

## 準備するもの（環境）
* Google Spreadsheet
* Linuxサーバ
* Github アカウント
* netlify アカウント(githubアカウントでログインできます)

## 準備するもの（データ）
* arealist.csv
    * area_id,area_name,area_block の形に編集したもの。
* public/data/arealist.json
    * arealist.csvをjsonにしたもの（フォーマットの変換方法はまだわかっていないので、わかったら後述）
* 掲示板データのcsv
    * area,name,lat,long,status,noteの形に編集したもの。Google Spreadsheetに取り込みピンのデータになる。areaはarealistのarea_nameから選択する。
* vote_venue.json
    * 投票所のデータのようですがこれはいらないかも。

## Linuxサーバセットアップ
windows wsl2 on ubuntuでの場合です
```sh
# pipインストール
sudo apt update
sudo apt upgrade
sudo apt install python3-pip
# pandasインストール
sudo apt install python3-pandas
```
