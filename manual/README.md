# poster-mapのセットアップマニュアル
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

## githubとnetlifyのセットアップ
* githubのリポジトリを用意し必要なファイルをコミットする
    * 必要なファイルとディレクトリ
        - public以下すべて
    * index.htmlは必要に応じて編集すること
* netlifyで「Add new site」を行い、↑のリポジトリからの自動デプロイを設定する
    * index.htmlなどのデザインや表記を変更し、コミットしたものがサイトに反映されたかを確認するのが簡単

## 設定ファイル化するまでの暫定
* public/scripts/summary.js
    * 88行目の東京都を対象の都道府県に書き換える（外部設定ファイル化したい）
* csv2json_small.py
    * 17行目 area_blocks 内をarealist.csvで定義したブロック名で書き換える（json化したい）

## google spreadsheetの設定
* 掲示板データのcsvをインポートしシート名を定義する（英数字で）
* 拡張機能→AppsScriptを開き、新しくスクリプトを作成して保存する
    * スクリプトはtools/spreadsheet/getcsv.gsをメモ帳で開き貼り付ければよい
* デプロイ→新しいデプロイでウェブアプリを選択し、アクセスできるユーザーを「全員」にして「デプロイ」する
    * 表示されるウェブアプリのURLをメモする
* コマンドでcsvがダウンロードできるかどうかテストする
```sh
# コマンドを実行する
curl -sL "{ウェブアプリのURL}?sheetName={シート名}" > test.csv
```
* test.csvの中身を確認し、public/data/all.csvのフォーマット、文字コードと同じかどうかを確認する

## 動作確認
* main.shの必要なコマンドを１つずつ実行していく
```sh
cd {カレントディレクトリ}
# グーグルスプレッドシートからcsvをダウンロード
curl -sL "{ウェブアプリのURL}?sheetName={シート名}" > public/data/all.csv

# 掲示板データをJSON出力＆エリアごとに分割
python3 csv2json_small.py public/data/all.csv public/data/

# 完了率のJSON出力
python3 summarize_progress.py ./public/data/summary.json

# 未完了数をJSON出力
python3 summarize_progress_absolute.py ./public/data/summary_absolute.json

```
* 作成されたJSONファイルを確認する
    * public/data直下
    * public/data/block はブロックごと
* 自動デプロイされたサイトを確認する