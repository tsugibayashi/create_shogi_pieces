#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import cv2
import numpy as np

### functions
# def print_usage(): {{{
def print_usage():
    print('[使い方]')
    print('      $ python concat_shogi_pieces.py <駒の種類>')
    print('  例. $ python concat_shogi_pieces.py 1')
    print()
    print('<駒の種類>:')
    print('    1 : 二文字駒')
    print('    2 : 一文字駒')
    print('    3 : 英文字駒')
# }}}

# def hconcat_8files (output, file1, file2, file3, file4,
#                     file5, file6, file7, file8):
# {{{
def hconcat_8files (output, file1, file2, file3, file4, \
                    file5, file6, file7, file8):
    # 画像を読み出す (RGBA画像を読み出す)
    img1 = cv2.imread(file1, -1)
    img2 = cv2.imread(file2, -1)
    img3 = cv2.imread(file3, -1)
    img4 = cv2.imread(file4, -1)
    img5 = cv2.imread(file5, -1)
    img6 = cv2.imread(file6, -1)
    img7 = cv2.imread(file7, -1)
    img8 = cv2.imread(file8, -1)

    # 画像を水平結合する
    img_h = cv2.hconcat([img1,  img2])
    img_h = cv2.hconcat([img_h, img3])
    img_h = cv2.hconcat([img_h, img4])
    img_h = cv2.hconcat([img_h, img5])
    img_h = cv2.hconcat([img_h, img6])
    img_h = cv2.hconcat([img_h, img7])
    img_h = cv2.hconcat([img_h, img8])

    # 結合した画像を保存する
    cv2.imwrite(output, img_h)
# }}}

# def vconcat_6files (output, file1, file2, file3, file4,
#                     file5, file6):
# {{{
def vconcat_6files (output, file1, file2, file3, file4, \
                    file5, file6):
    # 画像を読み出す (RGBA画像を読み出す)
    img1 = cv2.imread(file1, -1)
    img2 = cv2.imread(file2, -1)
    img3 = cv2.imread(file3, -1)
    img4 = cv2.imread(file4, -1)
    img5 = cv2.imread(file5, -1)
    img6 = cv2.imread(file6, -1)

    # 画像を垂直結合する
    img_v = cv2.vconcat([img1,  img2])
    img_v = cv2.vconcat([img_v, img3])
    img_v = cv2.vconcat([img_v, img4])
    img_v = cv2.vconcat([img_v, img5])
    img_v = cv2.vconcat([img_v, img6])

    # 結合した画像を保存する
    cv2.imwrite(output, img_v)
# }}}


### main routine
# 引数から、駒の種類 (piece_type) を取得する
args = sys.argv
piece_type  = args[1]

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

# 出力ファイル名
output1 = './tmp/hconcat1.png'
output2 = './tmp/hconcat2.png'
output3 = './tmp/hconcat3.png'
output4 = './tmp/hconcat4.png'
output5 = './tmp/hconcat5.png'
output6 = './tmp/hconcat6.png'
output  = './images/piece_v' + piece_type + '_776_636.png'

# 画像ファイル名
# 1段目
filename1 = './images/blank.png'
filename2 = './images/piece_P_' + piece_type + '_b.png'
filename3 = './images/piece_L_' + piece_type + '_b.png'
filename4 = './images/piece_N_' + piece_type + '_b.png'
filename5 = './images/piece_S_' + piece_type + '_b.png'
filename6 = './images/piece_B_' + piece_type + '_b.png'
filename7 = './images/piece_R_' + piece_type + '_b.png'
filename8 = './images/piece_G_' + piece_type + '_b.png'

# 2段目
filename9  = './images/piece_K_' + piece_type + '_b.png'
filename10 = './images/promoted_piece_P_' + piece_type + '_b.png'
filename11 = './images/promoted_piece_L_' + piece_type + '_b.png'
filename12 = './images/promoted_piece_N_' + piece_type + '_b.png'
filename13 = './images/promoted_piece_S_' + piece_type + '_b.png'
filename14 = './images/promoted_piece_B_' + piece_type + '_b.png'
filename15 = './images/promoted_piece_R_' + piece_type + '_b.png'
filename16 = './images/blank.png'

# 3段目
filename17 = './images/blank.png'
filename18 = './images/piece_p_' + piece_type + '_b.png'
filename19 = './images/piece_l_' + piece_type + '_b.png'
filename20 = './images/piece_n_' + piece_type + '_b.png'
filename21 = './images/piece_s_' + piece_type + '_b.png'
filename22 = './images/piece_b_' + piece_type + '_b.png'
filename23 = './images/piece_r_' + piece_type + '_b.png'
filename24 = './images/piece_g_' + piece_type + '_b.png'

# 4段目
filename25 = './images/piece_k_' + piece_type + '_b.png'
filename26 = './images/promoted_piece_p_' + piece_type + '_b.png'
filename27 = './images/promoted_piece_l_' + piece_type + '_b.png'
filename28 = './images/promoted_piece_n_' + piece_type + '_b.png'
filename29 = './images/promoted_piece_s_' + piece_type + '_b.png'
filename30 = './images/promoted_piece_b_' + piece_type + '_b.png'
filename31 = './images/promoted_piece_r_' + piece_type + '_b.png'
filename32 = './images/blank.png'

# 5段目
filename33 = './images/blank.png'
filename34 = './images/promoted_piece_P_' + piece_type + '_r.png'
filename35 = './images/promoted_piece_L_' + piece_type + '_r.png'
filename36 = './images/promoted_piece_N_' + piece_type + '_r.png'
filename37 = './images/promoted_piece_S_' + piece_type + '_r.png'
filename38 = './images/promoted_piece_B_' + piece_type + '_r.png'
filename39 = './images/promoted_piece_R_' + piece_type + '_r.png'
filename40 = './images/blank.png'

# 6段目
filename41 = './images/blank.png'
filename42 = './images/promoted_piece_p_' + piece_type + '_r.png'
filename43 = './images/promoted_piece_l_' + piece_type + '_r.png'
filename44 = './images/promoted_piece_n_' + piece_type + '_r.png'
filename45 = './images/promoted_piece_s_' + piece_type + '_r.png'
filename46 = './images/promoted_piece_b_' + piece_type + '_r.png'
filename47 = './images/promoted_piece_r_' + piece_type + '_r.png'
filename48 = './images/blank.png'

# 8つの画像を結合する
hconcat_8files(output1, filename1, filename2, filename3, filename4, \
                        filename5, filename6, filename7, filename8)
hconcat_8files(output2,  filename9, filename10, filename11, filename12, \
                        filename13, filename14, filename15, filename16)
hconcat_8files(output3, filename17, filename18, filename19, filename20, \
                        filename21, filename22, filename23, filename24)
hconcat_8files(output4, filename25, filename26, filename27, filename28, \
                        filename29, filename30, filename31, filename32)
hconcat_8files(output5, filename33, filename34, filename35, filename36, \
                        filename37, filename38, filename39, filename40)
hconcat_8files(output6, filename41, filename42, filename43, filename44, \
                        filename45, filename46, filename47, filename48)

# 6つの画像を結合する
vconcat_6files(output, output1, output2, output3, \
                       output4, output5, output6)

