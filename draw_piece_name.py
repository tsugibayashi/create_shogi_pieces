#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
from PIL import Image
import PIL.ImageDraw
import PIL.ImageFont

### functions
# def print_usage(): {{{
def print_usage():
    print('[使い方]')
    print('      $ python draw_piece_name.py <駒名> <駒の種類> <駒の色>')
    print('  例. $ python draw_piece_name.py K 1 b')
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
    print('   +R : 龍王(先手)')
    print('   +B : 龍馬(先手)')
    print('   +S : 全(先手)')
    print('   +N : 圭(先手)')
    print('   +L : 杏(先手)')
    print('   +P : と(先手)')
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
    print('<駒の種類>:')
    print('    1 : 二文字駒')
    print('    2 : 一文字駒')
    print('    3 : 英文字駒')
    print()
    print('<駒の色>:')
    print('    b : 黒色')
    print('    r : 朱色')
# }}}

### variables
# フォントの色 (R,G,B)
font_color1 = (0, 0, 0)      #黒色
font_color2 = (180, 65, 21)  #朱色


### main routine
# 引数から、
# 駒名(piece_name)、駒の種類 (piece_type)、駒の色 (piece_color) を取得する
args = sys.argv
piece_name  = args[1]
piece_type  = args[2]
piece_color = args[3]

# 引数に駒が指定されているか判定する
if ( len(piece_name) == 1 or len(piece_name) == 2 ):
    if ( piece_name in 'K R B G S N L P +R +B +S +N +L +P \
                        k r b g s n l p +r +b +s +n +l +p' ):
        print('出力する駒の画像:', piece_name)
    else:
        print('[Error] 引数に駒が指定されていない')
        print_usage()
        sys.exit()
else:
    print('[Error] 引数に駒が指定されていない')
    print_usage()
    sys.exit()

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

# 入力するファイル名
if (piece_name1 in 'K R B G S N L P'):
    # 先手の場合
    input_filename = './tmp/piece_' + piece_name1 + '_resize.png'
else:
    # 後手の場合、180度回転した画像を入力する
    input_filename = './tmp/rotated_piece_' + piece_name1 + '.png'

# 出力するファイル名
# 1文字目が + の場合、成駒である
if ( piece_name[0] == '+' ):
    if (piece_name1 in 'K R B G S N L P'):
        output = './images/promoted_piece_' + piece_name1 \
                               + '_' + piece_type \
                               + '_' + piece_color + '.png'
    else:
        # 後手の場合
        output = './tmp/rotated_promoted_piece_' + piece_name1 \
                               + '_' + piece_type \
                               + '_' + piece_color + '.png'
else:
    if (piece_name1 in 'K R B G S N L P'):
        output = './images/piece_' + piece_name1 + '_' + piece_type \
                               + '_' + piece_color + '.png'
    else:
        # 後手の場合
        output = './tmp/rotated_piece_' + piece_name1 + '_' + piece_type \
                               + '_' + piece_color + '.png'

# フォント
if (piece_type == '3'):
    font_ttf = "/usr/share/fonts/opentype/ipafont-mincho/ipag.ttf"  #IPAゴシック
else:
    font_ttf = "/usr/share/fonts/opentype/ipafont-mincho/ipam.ttf"  #IPA明朝

# フォントサイズ
# 一文字駒 と 英文字駒
if (piece_type == '2' or piece_type == '3'):
    # 玉 (一文字駒)
    if (piece_name == 'K' or piece_name == 'k'):
        font_size = 56
    # 飛、角、龍、馬 (一文字駒)
    elif (piece_name == 'R' or piece_name == 'r' or \
         piece_name == 'B' or piece_name == 'b' or \
         piece_name == 'G' or piece_name == 'g' or \
         piece_name == 'S' or piece_name == 's' or \
         piece_name == '+R' or piece_name == '+r' or \
         piece_name == '+B' or piece_name == '+b' or \
         piece_name == '+S' or piece_name == '+S'):
        font_size = 54
    # 桂、香、歩 (一字駒)
    else:
        font_size = 50   #1文字駒(小さい駒)

# 二文字駒
if (piece_type == '1'):
    # 成銀 (一文字駒)
    if (piece_name == '+S' or piece_name == '+s'):
        font_size = 54
    # 成桂、成香、と (一文字駒)
    elif (piece_name == '+N' or piece_name == '+n' or \
         piece_name == '+L' or piece_name == '+l' or \
         piece_name == '+P' or piece_name == '+p'):
        font_size = 50
    # 玉 (二文字駒)
    elif (piece_name == 'K' or piece_name == 'k'):
        font_size = 48   #2文字駒(大きい駒)
        ystep = 3        #二文字駒のときずらす量
    # 飛、角、龍、馬 (二文字駒)
    elif (piece_name == 'R' or piece_name == 'r' or \
         piece_name == 'B' or piece_name == 'b' or \
         piece_name == '+R' or piece_name == '+r' or \
         piece_name == '+B' or piece_name == '+b'):
        font_size = 46   #2文字駒(大きい駒)
        ystep = 5        #二文字駒のときずらす量
    # 金 (二文字駒)
    elif (piece_name == 'G' or piece_name == 'g'):
        font_size = 45   #2文字駒(大きい駒)
        ystep = 5        #二文字駒のときずらす量
    # 銀 (二文字駒)
    elif (piece_name == 'S' or piece_name == 's'):
        font_size = 43   #2文字駒(大きい駒)
        ystep = 5        #二文字駒のときずらす量
    # 桂 (二文字駒)
    elif (piece_name == 'N' or piece_name == 'n'):
        font_size = 41   #2文字駒(大きい駒)
        ystep = 6        #二文字駒のときずらす量
    # 香 (二文字駒)
    elif (piece_name == 'L' or piece_name == 'l'):
        font_size = 40   #2文字駒(大きい駒)
        ystep = 6        #二文字駒のときずらす量
    # 歩 (二文字駒)
    else:
        font_size = 38   #2文字駒(小さい駒)
        ystep = 8        #二文字駒のときずらす量

# 描く文字
if (piece_type == '1'):
    # {{{
    if piece_name == 'K' or piece_name == 'k':
        text1 = '王'
        text2 = '将'
    elif piece_name == 'R' or piece_name == 'r':
        text1 = '飛'
        text2 = '車'
    elif piece_name == 'B' or piece_name == 'b':
        text1 = '角'
        text2 = '行'
    elif piece_name == 'G' or piece_name == 'g':
        text1 = '金'
        text2 = '将'
    elif piece_name == 'S' or piece_name == 's':
        text1 = '銀'
        text2 = '将'
    elif piece_name == 'N' or piece_name == 'n':
        text1 = '桂'
        text2 = '馬'
    elif piece_name == 'L' or piece_name == 'l':
        text1 = '香'
        text2 = '車'
    elif piece_name == 'P' or piece_name == 'p':
        text1 = '歩'
        text2 = '兵'
    elif piece_name == '+R' or piece_name == '+r':
        text1 = '龍'
        text2 = '王'
    elif piece_name == '+B' or piece_name == '+b':
        text1 = '龍'
        text2 = '馬'
    elif piece_name == '+S' or piece_name == '+s':
        text1 = '全'
        text2 = ''
    elif piece_name == '+N' or piece_name == '+n':
        text1 = '圭'
        text2 = ''
    elif piece_name == '+L' or piece_name == '+l':
        text1 = '杏'
        text2 = ''
    elif piece_name == '+P' or piece_name == '+p':
        text1 = 'と'
        text2 = ''
    # }}}
elif (piece_type == '2'):
    # {{{
    if piece_name == 'K' or piece_name == 'k':
        text1 = '王'
    elif piece_name == 'R' or piece_name == 'r':
        text1 = '飛'
    elif piece_name == 'B' or piece_name == 'b':
        text1 = '角'
    elif piece_name == 'G' or piece_name == 'g':
        text1 = '金'
    elif piece_name == 'S' or piece_name == 's':
        text1 = '銀'
    elif piece_name == 'N' or piece_name == 'n':
        text1 = '桂'
    elif piece_name == 'L' or piece_name == 'l':
        text1 = '香'
    elif piece_name == 'P' or piece_name == 'p':
        text1 = '歩'
    elif piece_name == '+R' or piece_name == '+r':
        text1 = '龍'
    elif piece_name == '+B' or piece_name == '+b':
        text1 = '龍'
    elif piece_name == '+S' or piece_name == '+s':
        text1 = '全'
    elif piece_name == '+N' or piece_name == '+n':
        text1 = '圭'
    elif piece_name == '+L' or piece_name == '+l':
        text1 = '杏'
    elif piece_name == '+P' or piece_name == '+p':
        text1 = 'と'
    # }}}
elif (piece_type == '3'):
    # {{{
    if piece_name == 'K' or piece_name == 'k':
        text1 = 'Ｋ'
    elif piece_name == 'R' or piece_name == 'r':
        text1 = 'Ｒ'
    elif piece_name == 'B' or piece_name == 'b':
        text1 = 'Ｂ'
    elif piece_name == 'G' or piece_name == 'g':
        text1 = 'Ｇ'
    elif piece_name == 'S' or piece_name == 's':
        text1 = 'Ｓ'
    elif piece_name == 'N' or piece_name == 'n':
        text1 = 'Ｎ'
    elif piece_name == 'L' or piece_name == 'l':
        text1 = 'Ｌ'
    elif piece_name == 'P' or piece_name == 'p':
        text1 = 'Ｐ'
    elif piece_name == '+R' or piece_name == '+r':
        text1 = '+R'
    elif piece_name == '+B' or piece_name == '+b':
        text1 = '+B'
    elif piece_name == '+S' or piece_name == '+s':
        text1 = '+S'
    elif piece_name == '+N' or piece_name == '+n':
        text1 = '+N'
    elif piece_name == '+L' or piece_name == '+l':
        text1 = '+L'
    elif piece_name == '+P' or piece_name == '+p':
        text1 = '+P'
    # }}}

# 画像の読み込み
img = Image.open(input_filename)
draw = PIL.ImageDraw.Draw(img)

# フォント
font = PIL.ImageFont.truetype(font_ttf, font_size)

# テキストの大きさを取得
text_size1 = font.getsize(text1)
if (piece_type == '1'):
    text_size2 = font.getsize(text2)

# 文字の場所
if (piece_type == '2' or piece_type == '3'):
    text_pos1 = ((img.size[0] - text_size1[0]) / 2, 
                 (img.size[1] - text_size1[1]) / 2)
else:
    if (piece_name == '+S' or piece_name == '+s' or \
         piece_name == '+N' or piece_name == '+n' or \
         piece_name == '+L' or piece_name == '+l' or \
         piece_name == '+P' or piece_name == '+p'):
        text_pos1 = ((img.size[0] - text_size1[0]) / 2, 
                     (img.size[1] - text_size1[1]) / 2)
    else:
        text_pos1 = ((img.size[0] - text_size1[0]) / 2, 
                      img.size[1] / 4 - text_size1[1] / 2 + ystep)
        text_pos2 = ((img.size[0] - text_size2[0]) / 2, 
                      img.size[1] * 3 / 4 - text_size2[1] / 2 - ystep)

# 文字を描く
if (piece_type == '2' or piece_type == '3'):
    # 一字駒
    if (piece_color == 'b'):
        # 黒色
        draw.text(text_pos1, text1, font=font, fill=font_color1)
    else:
        # 朱色
        draw.text(text_pos1, text1, font=font, fill=font_color2)
else:
    if (piece_name == '+S' or piece_name == '+s' or \
         piece_name == '+N' or piece_name == '+n' or \
         piece_name == '+L' or piece_name == '+l' or \
         piece_name == '+P' or piece_name == '+p'):
        # 一字駒
        if (piece_color == 'b'):
            # 黒色
            draw.text(text_pos1, text1, font=font, fill=font_color1)
        else:
            # 朱色
            draw.text(text_pos1, text1, font=font, fill=font_color2)
    else:
        # 二字駒
        if (piece_color == 'b'):
            # 黒色
            draw.text(text_pos1, text1, font=font, fill=font_color1)
            draw.text(text_pos2, text2, font=font, fill=font_color1)
        else:
            # 朱色
            draw.text(text_pos1, text1, font=font, fill=font_color2)
            draw.text(text_pos2, text2, font=font, fill=font_color2)

# 画像の保存
img.save(output)

