#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
from PIL import Image
import cv2
import numpy

### functions
# def print_usage(): {{{
def print_usage():
    print('[使い方]')
    print('      $ python resize_shogi_piece.py <駒名>')
    print('  例. $ python resize_shogi_piece.py K')
    print()
    print('<駒名>:')
    print('    K : 王将(先手)')
    print('    R : 飛車(先手)')
    print('    B : 角行(先手)')
    print('    G : 金将(先手)')
    print('    S : 銀将(先手)')
    print('    N : 桂馬(先手)')
    print('    L : 香車(先手)')
    print('    P : 歩兵(先手)')
    print('    k : 王将(後手)')
    print('    r : 飛車(後手)')
    print('    b : 角行(後手)')
    print('    g : 金将(後手)')
    print('    s : 銀将(後手)')
    print('    n : 桂馬(後手)')
    print('    l : 香車(後手)')
    print('    p : 歩兵(後手)')
    print('    x : 無し')
# }}}

### variables
resize_width = 97
resize_height = 106

### main routine
# 引数から 駒名(piece_name) を取得する
# {{{
args = sys.argv
piece_name = args[1]

# 引数に駒が指定されているか判定する
if ( len(piece_name) == 1 ):
    if ( piece_name in 'K R B G S N L P k r b g s n l p x' ):
        print('縮小する駒の画像:', piece_name)
    else:
        print('[Error] 引数に駒が指定されていない')
        print_usage()
        sys.exit()
else:
    print('[Error] 引数に駒が指定されていない')
    print_usage()
    sys.exit()
# }}}

# 入力するファイル名
input_filename = './tmp/piece_' + piece_name + '_org.png'
# 保存するファイル名
if piece_name == 'x':
    output         = './images/blank.png'
else:
    output         = './tmp/piece_' + piece_name + '_resize.png'

# 画像の読み込み
if piece_name != 'x':
    img = Image.open(input_filename)

    # 画像のリサイズ
    img_resize = img.resize((resize_width, resize_height), 
                            resample=Image.ANTIALIAS)

    # リサイズした画像の保存
    img_resize.save(output)
else:
    # 出力用のブランク画像の作成
    img = numpy.zeros((resize_height, resize_width, 3), numpy.uint8)
    # 全データ (x, y, BGR) の値を 白色に指定する
    img[:, :, :] = 255

    # img にアルファチャンネルを追加した画像 img_output を作成する
    img_output = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)

    # img に対して白色の位置を 透過色(アルファチャンネルの値が0) に設定する
    img_output[:, :, 3] = numpy.where(numpy.all(img == 255, axis=-1), 0, 255)

    ### img_output の保存
    cv2.imwrite(output, img_output)

