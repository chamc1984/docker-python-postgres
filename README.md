# docker-python-postgres

## ソース取得

```
$ git clone <url>
$ cd docker-python-postgres
```

## Dockerイメージビルド

```
$ docker build -t pytest .
```

## 起動・実行

```
$ docker run --rm -it -v $(pwd):/usr/local/src/pytest pytest bash
root@xxxxxxxxxxxx: cd /usr/local/src/pytest
root@xxxxxxxxxxxx: python sample.py
```
