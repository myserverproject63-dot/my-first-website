import os
import time
from flask import Flask
import psycopg2 # PostgreSQLに接続するためのライブラリ

app = Flask(__name__)

# データベース接続を試みる関数
def get_db_connection():
    # docker-compose.ymlで設定した環境変数を読み込む
    db_name = os.environ.get('POSTGRES_DB')
    db_user = os.environ.get('POSTGRES_USER')
    db_pass = os.environ.get('POSTGRES_PASSWORD')
    # Dockerが自動的に名前解決してくれるホスト名（サービス名）
    db_host = "db" 

    conn = None
    retries = 5
    while retries > 0:
        try:
            # データベースへの接続を試みる
            conn = psycopg2.connect(
                dbname=db_name,
                user=db_user,
                password=db_pass,
                host=db_host,
                port="5432" # PostgreSQLのデフォルトポート
            )
            # 接続に成功したらループを抜ける
            print("Database connection successful!")
            return conn
        except psycopg2.OperationalError as e:
            # 接続に失敗した場合（DBがまだ起動していないなど）
            print(f"Database connection failed: {e}")
            retries -= 1
            time.sleep(5) # 5秒待ってから再試行
    
    print("Failed to connect to the database after several retries.")
    return None

@app.route('/')
def hello():
    conn = get_db_connection()
    if conn:
        # 接続に成功した場合
        conn.close()
        return '<h1 style="text-align: center;">Hello, Python!</h1><p style="text-align: center;">Successfully connected to the PostgreSQL database!</p>'
    else:
        # 接続に失敗した場合
        return '<h1 style="text-align: center; color: red;">Error:</h1><p style="text-align: center;">Could not connect to the database.</p>'

if __name__ == '__main__':
    # 0.0.0.0でリッスンし、コンテナ外からのアクセスを許可
    app.run(host='0.0.0.0', port=5000)
