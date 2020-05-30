## movie-recommender-ml

#### バッチ起動方法

```bash
# 仮想環境のアクティベート
$ source venv/bin/activate

# バッチ起動(ローカル)
$ python -m app.main
```

#### コンテナ操作

```bash
# コンテナのビルド
$ docker build -t movie-recommender/ml-batch:0.0.1 .

# コンテナの起動
$ docker run --rm --env-file .env --name ml-batch movie-recommender/ml-batch:0.0.1 

```
