#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import math
import cv2
import numpy

#------------------------------------------
# 駒の座標とサイズについて
#------------------------------------------
#        (x5,y5)             -
#        |     |             |
#      |         |           |
#   (x3,y3)     (x4,y4)      |
#    | 角度3        |        b*scale
#    |              |        |
#   |                |       |
#   |角度1           |       |
# (x1,y1)----------(x2,y2)   -
#          a*scale
#------------------------------------------

### functions
# def print_usage(): {{{
def print_usage():
    print('[使い方]')
    print('      $ python create_shogi_piece.py <駒名>')
    print('  例. $ python create_shogi_piece.py K')
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
# }}}

### variables
# 駒を中央に配置する(center) / 下線に近づけて配置する(bottom)
# https://news.yahoo.co.jp/byline/matsumotohirofumi/20190701-00132478/
piece_position = 'center'
#piece_position = 'bottom'

# 線の色(R, G, B)    (白(255,255,255)以外を指定すること)
piece_color = (236, 202, 131)   #木の色
#piece_color = (0, 0, 0)         #黒

# 駒の色(R, G, B)    (白(255,255,255)以外を指定すること)
thickness_color_black  = (168, 132, 72)   #先手の駒の底の色
thickness_color_white1 = (160, 133, 78)   #後手の駒の上部の色(左側)
thickness_color_white2 = (165, 141, 93)   #後手の駒の上部の色(右側)

# 駒の画像の倍率
#scale = 1
scale = 13

# 保存する画像の大きさ
# output_width  の最小値: size_a * scale
# output_height の最小値: size_b * scale
output_width  = 97 * 4
output_height = 106 * 4
#output_width  = 28 * scale
#output_height = 31 * scale
#output_width  = 28 * scale + 5
#output_height = 31 * scale + 5

# 駒の厚さ
piece_thickness = 10
#piece_thickness = 0

# 引数から 駒名(piece_name) を取得する
# {{{
args = sys.argv
piece_name = args[1]

# 引数に駒が指定されているか判定する
if ( len(piece_name) == 1 ):
    if ( piece_name in 'K R B G S N L P k r b g s n l p' ):
        print('出力する駒(文字無し)の画像:', piece_name)
    else:
        print('[Error] 引数に駒が指定されていない')
        print_usage()
        sys.exit()
else:
    print('[Error] 引数に駒が指定されていない')
    print_usage()
    sys.exit()
# }}}

# 保存するファイル名
img_filename = './tmp/piece_' + piece_name + '_org.png'

### これらの変数は修正しないこと ###
# 先手と後手のどちらの駒を生成するか
if piece_name.isupper():
    black_or_white = 'black'   #先手
else:
    black_or_white = 'white'   #後手

# 駒の寸法
# http://kijishi.html.xdomain.jp/komanosize.htm
if piece_name == 'K' or piece_name == 'k':
    size_a = 28.0
    size_b = 31.0
elif piece_name == 'R' or piece_name == 'B' or \
     piece_name == 'r' or piece_name == 'b':
    size_a = 27.0
    size_b = 30.0
elif piece_name == 'G' or piece_name == 'S' or \
     piece_name == 'g' or piece_name == 's':
    size_a = 26.0
    size_b = 29.0
elif piece_name == 'N' or piece_name == 'n':
    size_a = 25.0
    size_b = 28.0
elif piece_name == 'L' or piece_name == 'l':
    size_a = 23.0
    size_b = 28.0
elif piece_name == 'P' or piece_name == 'p':
    size_a = 22.0
    size_b = 27.0
 
# 駒の角度 (度)
angle1 = 80.5
angle3 = 116.5

# 駒の画像の大きさ
img_width = int(size_a * scale)
img_height = int(size_b * scale)

# x,y のオフセット
if piece_position == 'center':
    x_offset = int((output_width - img_width) / 2.0)
    y_offset = int((output_height - img_height) / 2.0)
else:
    x_offset = int((output_width - img_width) / 2.0)
    if black_or_white == 'black':
        # 下線から piece_thickness だけ上にずらす
        y_offset = int(output_height - img_height) - piece_thickness
    else:
        y_offset = 1  # 下線から1ドットずらす (見やすさのため)

### 駒の位置の計算 ###
# (x1,y1): 駒の左下の位置
x1 = 0.0
y1 = 0.0

# (x2,y2): 駒の右下の位置
x2 = size_a * scale
y2 = 0.0

# (x5,y5): 駒の頂点の位置
x5 = x2 / 2.0
y5 = size_b * scale

# 直線(x1,y1)-(x3,y3): y = slope13 * x
# slope13      : 直線 (x1,y1)-(x3,y3) の傾き
slope13 = math.tan(math.radians(angle1))
#print(slope13)

# 直線(x3,y3)-(x5,y5): y = slope35 * x + yintercept35
angle35 = angle1 + angle3 - 180
# slope35      : 直線 (x3,y3)-(x5,y5) の傾き
slope35 = math.tan(math.radians(angle35))
# yintercept35 : 直線 (x3,y3)-(x5,y5) の切片
yintercept35 = y5 - slope35 * x5

# (x3,y3) : 駒の左上の位置は、連立方程式を解いて求める
# y = slope13 * x
# y = slope35 * x + yintercept35
y3 = yintercept35 * slope13 / ( slope13 - slope35 )
x3 = y3 / slope13
#print('x3','y3',x3,y3)

# (x4,y4) : 駒の右上の位置は、(x3,y3)の線対称な位置に存在する
x4 = x2 - x3
y4 = y3
#print('x4','y4',x4,y4)

# 先手の駒を場合、各点のy軸の値を変換する
if black_or_white == 'black':
    # (x1,y1): 駒の左下の位置
    y1 = size_b * scale
    # (x2,y2): 駒の右下の位置
    y2 = y1
    # (x3,y3) : 駒の左上の位置
    y3 = size_b * scale - y3
    # (x4,y4) : 駒の右上の位置
    y4 = size_b * scale - y4
    # (x5,y5) : 駒の頂点の位置
    y5 = 0

# 線の終端の値を1ドット小さくする (描画のために必要な処理)
# (x2,y2): 駒の右下の位置 (描画のために-1が必要)
x2 = x2 - 1.0
# (x5,y5) : 駒の頂点の位置 (描画のために-1が必要)
if black_or_white == 'white':
    y5 = y5 - 1.0

### 駒画像の作成 ###
# ブランク画像の作成
img = numpy.zeros((img_height, img_width, 3), numpy.uint8)
# 全データ (x, y, BGR) の値を 白色に指定する
img[:, :, :] = 255

# 整数に型変換
ix1 = int(x1)
ix2 = int(x2)
ix3 = int(x3)
ix4 = int(x4)
ix5 = int(x5)
iy1 = int(y1)
iy2 = int(y2)
iy3 = int(y3)
iy4 = int(y4)
iy5 = int(y5)

# 画像 img に将棋の駒を描き、塗りつぶす
piece_points = numpy.array(( (ix1, iy1), (ix2, iy2), (ix4, iy4), 
                             (ix5, iy5), (ix3, iy3) ))
piece_img = cv2.fillPoly(img, [piece_points], piece_color)

### オフセットの追加 ###
# 出力用のブランク画像の作成
img2 = numpy.zeros((output_height, output_width, 3), numpy.uint8)
# 全データ (x, y, BGR) の値を 白色に指定する
img2[:, :, :] = 255

# 2つの画像を合成する
img2[y_offset:y_offset + piece_img.shape[0], 
     x_offset:x_offset + piece_img.shape[1]] = piece_img

### オフセットの追加 ###
# 出力用のブランク画像の作成
img2 = numpy.zeros((output_height, output_width, 3), numpy.uint8)
# 全データ (x, y, BGR) の値を 白色に指定する
img2[:, :, :] = 255

# 2つの画像を合成する
img2[y_offset:y_offset + piece_img.shape[0], 
     x_offset:x_offset + piece_img.shape[1]] = piece_img

### 駒の厚みを描く
if black_or_white == 'black':
    thick_x1 = x_offset
    thick_y1 = y_offset + img_height - 1  # 描画のために下端は -1 する

    thick_x2 = thick_x1 + img_width - 1   # 描画のために右端は -1 する
    thick_y2 = thick_y1

    thick_x3 = thick_x2
    thick_y3 = thick_y2 + piece_thickness

    thick_x4 = thick_x1
    thick_y4 = thick_y3

    piece_points = numpy.array(( (thick_x1, thick_y1),
                                 (thick_x2, thick_y2), 
                                 (thick_x3, thick_y3), 
                                 (thick_x4, thick_y4) ))
    img2 = cv2.fillPoly(img2, [piece_points], thickness_color_black)
else:
    #後手の駒の上部(左側)の色を塗る
    thick_x1 = x_offset + ix3
    thick_y1 = y_offset + iy3 + 1

    thick_x2 = x_offset + ix5
    thick_y2 = y_offset + iy5 + 1

    thick_x3 = thick_x2
    thick_y3 = thick_y2 + piece_thickness - 1  # 描画のために下端は -1 する

    thick_x4 = thick_x1
    thick_y4 = thick_y1 + piece_thickness - 1  # 描画のために下端は -1 する

    piece_points = numpy.array(( (thick_x1, thick_y1),
                                 (thick_x2, thick_y2), 
                                 (thick_x3, thick_y3), 
                                 (thick_x4, thick_y4) ))
    img2 = cv2.fillPoly(img2, [piece_points], thickness_color_white1)

    #後手の駒の上部(右側)の色を塗る
    thick_x1 = x_offset + ix5
    thick_y1 = y_offset + iy5 + 1

    thick_x2 = x_offset + ix4
    thick_y2 = y_offset + iy4 + 1

    thick_x3 = thick_x2
    thick_y3 = thick_y2 + piece_thickness - 1  # 描画のために下端は -1 する

    thick_x4 = thick_x1
    thick_y4 = thick_y1 + piece_thickness - 1  # 描画のために下端は -1 する

    piece_points = numpy.array(( (thick_x1, thick_y1),
                                 (thick_x2, thick_y2), 
                                 (thick_x3, thick_y3), 
                                 (thick_x4, thick_y4) ))
    img2 = cv2.fillPoly(img2, [piece_points], thickness_color_white2)
 
### アルファチャンネルの追加 ###
# img2 にアルファチャンネルを追加した画像 output を作成する
output = cv2.cvtColor(img2, cv2.COLOR_BGR2RGBA)

# img2 に対して白色の位置を 透過色(アルファチャンネルの値が0) に設定する
output[:, :, 3] = numpy.where(numpy.all(img2 == 255, axis=-1), 0, 255)

### output の保存
cv2.imwrite(img_filename, output)

