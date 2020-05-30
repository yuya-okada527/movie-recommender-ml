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
$ docker build -t movie-recommender/ml-batch .

# コンテナの起動
$ docker run --rm --name ml-batch movie-recommender/ml-batch

```
