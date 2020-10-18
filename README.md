# create_shogi_pieces

## 概要

本ソフトウェアを使って、将棋駒の画像、および、[MyShogi](https://github.com/yaneurao/MyShogi)用の将棋駒の画像を作成することができます。

## 対応環境

- Ubuntu 18.04

## 前提作業

実行する前に、以下のパッケージをインストールして下さい。

* python3
* python3-opencv
* python3-pil
* python3-numpy

また、下記を実行し /usr/bin/python3.6 を選択することによって、
python3をデフォルトのpythonにすることができます。

    $ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1
    $ sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 2
    $ sudo update-alternatives --config python

## 使い方

(1) 作業用ディレクトリに移動し、本レポジトリを取得します。

    $ cd <作業用ディレクトリ>
    $ git clone https://github.com/tsugibayashi/create_shogi_pieces

(2) スクリプト "create_shogi_pieces.sh" を実行し、画像を生成します。

    $ cd create_shogi_pieces/
    $ ./create_shogi_pieces.sh

(3) ./images/ に移動し、MyShogiで使用したい画像データをコピーします。

    $ cd images/
    $ cp -pv piece_v1_776_636.png <MyShogiのインストール先>/image/
    $ cp -pv piece_v2_776_636.png <MyShogiのインストール先>/image/
    $ cp -pv piece_v3_776_636.png <MyShogiのインストール先>/image/

## 各画像ファイルの説明

| ファイル名 | 説明 |
----|----
| piece_v1_776_636.png | 二文字駒の画像 |
| piece_v2_776_636.png | 一文字駒の画像 |
| piece_v3_776_636.png | 英文字駒の画像 |

## ライセンス

Apache-2.0 License


以上
