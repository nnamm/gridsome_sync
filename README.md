# 指定ローカルディレクトリ配下のデータを、リモート先に同期するスクリプト

Gridsomeでビルドしたdist配下を、指定先のリモート環境と同期します。[pyftpsync](https://pyftpsync.readthedocs.io/en/latest/index.html)をFTPSモードで使っています。

## 使用における既知の問題点

* ライブラリのドキュメントにもある通り、基本的な差分検知がファイルサイズと変更日であるため、厳密な比較はできていません。
* ローカルとリモートに専用のメタデータファイルが作られます。それによる差分検知もしていますが、gridsome buildするたびにすべてのファイルが新たに作られるため、結局はほぼすべてのファイルがアップロードされます。
* 個人的にはコマンド1発でアップロードされるため、現状はよしとしています。 

## 使い方

```
// configファイル名変更
$ mv config_sample.ini config.ini

// ローカルパス、リモートパス、FTP
$ vim config.ini  

// モジュールのインストール
$ pip install -r requirements.txt

// 実行
$ python3 sync_gridsome.py

※ログはpyftpsync.logに出力されます
```
