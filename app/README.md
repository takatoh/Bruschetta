# Bruschetta APP

## 開発用 Docker 環境のための手順（メモ）

一通りの手順：
1. 環境変数の設定
2. Dockerイメージのビルド
3. コンテナ内で、依存ライブラリをインストール
4. サービスを起動

### 環境変数の設定

設定が必要な環境変数：
- VUE_APP_NAME
- VUE_APP_API_ROOT

`.env.dev` ファイルに書いてあるので、そのまま利用すればいい。

### Dockerイメージのビルド

```sh
$ docker compose build
```

### コンテナ内で依存ライブラリのインストール

```sh
$ docker compose run --rm bruschetta-app-devel npm install
```

### サービス（コンテナ）の起動

```sh
$ docker compose up -d
```
