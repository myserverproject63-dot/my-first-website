# STEP 1: ベースとなるNginx（軽量版）のイメージを持ってくる
FROM nginx:alpine

# STEP 2: index.html を、コンテナ内のNginxがWebページを置く場所へコピーする
COPY index.html /usr/share/nginx/html/index.html
