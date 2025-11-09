## STEP 1: ベースとなるNginx（軽量版）のイメージを持ってくる
#FROM nginx:alpine

## STEP 2: index.html を、コンテナ内のNginxがWebページを置く場所へコピーする
#COPY index.html /usr/share/nginx/html/index.html

# STEP 1: Python 3.10-slim をベースイメージとして使用
FROM python:3.10-slim

# STEP 2: コンテナ内の /app フォルダを作業ディレクトリに設定
WORKDIR /app

# STEP 3: 必要なライブラリ一覧をコンテナにコピー
COPY requirements.txt requirements.txt

# STEP 4: requirements.txt を使ってライブラリをインストール
RUN pip install --no-cache-dir -r requirements.txt

# STEP 5: アプリ本体（app.py）とその他のファイル（.）をコンテナにコピー
COPY . .

# STEP 6: コンテナが起動したときに実行するコマンドを設定
# "flask run --host=0.0.0.0" を実行するのと同じ
CMD ["flask", "run", "--host=0.0.0.0"]
