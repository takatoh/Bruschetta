# Bruschetta API

## 開発用 Docker 環境構築のための手順（メモ）

一通りの手順：
1. 環境変数の設定
2. アプリの設定ファイル
3. 表紙画像用ディレクトリを作成
4. Dockerイメージのビルド
5. コンテナ内で、依存ライブラリをインストール
6. コンテナ内で、データベースの初期化
7. サービスを起動

### 環境変数の設定

設定が必要な環境変数：
- BRUSCHETTA_INSTNACE_DIR
- BRUSCHETTA_ALLOW_ORIGINS

`.env` ファイルに書いてあるので、そのまま利用すればいい。

### アプリの設定ファイル

インスタンス・ディレクトリにコピー。必要なら編集。
```sh
$ cp bruschetta.conf.example instance/bruschetta.conf
```

### 表紙画像用のディレクトリを作成

設定ファイルに合わせて作る。デフォルトでは `instance/covearts` に作成済み。

### Docker イメージのビルド
```sh
$ docker compose build
```

### コンテナ内で依存ライブラリのインストールとデータベースの初期化

コンテナ起動。
```sh
$ docker compose run --rm bruschetta-api-devel bash
```
依存ライブラリのインストール。
```sh
[container] /app $ poetry install
```
データベースの初期化。
```sh
[container] /app $ poetry run flask init-db
```
コンテナから脱出。
```sh
[container] /app $ exit
```

### サービスの起動

準備は整ったので、サービスを起動する。
```sh
$ docker compose up -d
```
