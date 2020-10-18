#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
from PIL import Image

### functions
# def print_usage(): {{{
def print_usage():
    print('[使い方]')
    print('      $ python rotate_shogi_piece.py <駒名> <ファイル名の種類> ' + \
                   '<駒の種類> <駒の色>')
    print('  例. $ python rotate_shogi_piece.py k 1 1')
    print()
    print('<駒名>:')
    print('    k : 王将(後手)')
    print('    r : 飛車(後手)')
    print('    b : 角行(後手)')
    print('    g : 金将(後手)')
    print('    s : 銀将(後手)')
    print('    n : 桂馬(後手)')
    print('    l : 香車(後手)')
    print('    p : 歩兵(後手)')
    print('   +r : 龍王(後手)')
    print('   +b : 龍馬(後手)')
    print('   +s : 全(後手)')
    print('   +n : 圭(後手)')
    print('   +l : 杏(後手)')
    print('   +p : と(後手)')
    print()
    print('<ファイル名の種類>:')
    print('    1 : 入力ファイル名は、images/piece_<駒名>_org.png')
    print('    2 : 入力ファイル名は、images/rotated_piece_<駒名>_<数字>.png')
    print()
    print('<駒の種類>: <ファイル名の種類>=2のとき必須')
    print('    1 : 二文字駒')
    print('    2 : 一文字駒')
    print('    3 : 英文字駒')
    print()
    print('<駒の色>: <ファイル名の種類>=2のとき必須')
    print('    b : 黒色')
    print('    r : 朱色')
# }}}

### variables


### main routine
# 引数から 駒名(piece_name) を取得する
args = sys.argv
piece_name    = args[1]
filename_type = args[2]
if (filename_type == '2'):
    piece_type    = args[3]
    piece_color   = args[4]

# 引数に後手の駒が指定されているか判定する
if (len(piece_name) == 1 or len(piece_name) == 2):
    if ( piece_name in 'k r b g s n l p +r +b +s +n +l +p' ):
        print('180度回転する駒の画像:', piece_name)
    else:
        print('[Error] 引数に駒が指定されていない')
        print_usage()
        sys.exit()
else:
    print('[Error] 引数に駒が指定されていない')
    print_usage()
    sys.exit()

# 引数にファイルの種類が指定されているか判定する
if (len(filename_type) == 1):
    if ( filename_type in '1 2' ):
        print('ファイル名の種類:', filename_type)
    else:
        print('[Error] 引数に駒が指定されていない')
        print_usage()
        sys.exit()
else:
    print('[Error] 引数に駒が指定されていない')
    print_usage()
    sys.exit()

if (filename_type == '2'):
    # 引数に駒の種類が指定されているか判定する
    if ( len(piece_type) == 1 ):
        if ( piece_type in '1 2 3' ):
            print('出力する駒の種類:', piece_type)
        else:
            print('[Error] 引数に駒の種類が指定されていない')
            print_usage()
            sys.exit()
    else:
        print('[Error] 引数に駒の種類が指定されていない')
        print_usage()
        sys.exit()
    # 引数に駒の色が指定されているか判定する
    if ( len(piece_color) == 1 ):
        if ( piece_color in 'r b' ):
            print('出力する駒の色:', piece_color)
        else:
            print('[Error] 引数に駒の色が指定されていない')
            print_usage()
            sys.exit()
    else:
        print('[Error] 引数に駒の色が指定されていない')
        print_usage()
        sys.exit()

# piece_name1 : piece_name から '+'を削除したもの
piece_name1 = piece_name.replace('+', '')

if (filename_type == '1'):
    # 入力するファイル名
    input_filename = './tmp/piece_' + piece_name1 + '_resize.png'

    # 保存するファイル名
    output         = './tmp/rotated_piece_' + piece_name1 + '.png'
else:
    # 1文字目が + の場合、成駒である
    if (piece_name[0] == '+'):
        # 入力するファイル名
        input_filename = './tmp/rotated_promoted_piece_' + piece_name1 \
                         + '_' + piece_type + '_' + piece_color + '.png'
        # 保存するファイル名
        output         = './images/promoted_piece_' + piece_name1 \
                         + '_' + piece_type + '_' + piece_color + '.png'
    else:
        # 入力するファイル名
        input_filename = './tmp/rotated_piece_' + piece_name1 \
                         + '_' + piece_type + '_' + piece_color + '.png'
        # 保存するファイル名
        output         = './images/piece_' + piece_name1 \
                         + '_' + piece_type + '_' + piece_color + '.png'

# 画像の読み込み
img = Image.open(input_filename)

# 画像のリサイズ
img_rotate = img.rotate(180)

# リサイズした画像の保存
img_rotate.save(output)

