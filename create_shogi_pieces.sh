#!/bin/bash

# ディレクトリ作成
if [ ! -d images ]; then
    mkdir -v images
fi
if [ ! -d tmp ]; then
    mkdir -v tmp
fi

# 文字の無い駒の画像を作成
for i in K R B G S N L P k r b g s n l p ; do
    python create_shogi_piece.py $i
done

# MyShogi の駒サイズ (97x106) に縮小する
for i in K R B G S N L P k r b g s n l p ; do
    python resize_shogi_piece.py $i
done

# 駒の書かれていない画像 (97x106) を作成する
python resize_shogi_piece.py x

# 後手の駒を180度回転する
for i in k r b g s n l p ; do
    python rotate_shogi_piece.py $i 1
done

# 文字の無い駒に、文字を追加する
for i in K R B G S N L P k r b g s n l p ; do
    for j in 1 2 3 ; do
        python draw_piece_name.py $i $j b
    done
done

for i in +R +B +S +N +L +P +r +b +s +n +l +p ; do
    for j in 1 2 3 ; do
        for color in b r ; do
            python draw_piece_name.py $i $j $color
        done
    done
done

# 後手の駒を180度回転する
for i in k r b g s n l p ; do
    for j in 1 2 3 ; do
        python rotate_shogi_piece.py $i 2 $j b
    done
done

for i in +r +b +s +n +l +p ; do
    for j in 1 2 3 ; do
        for color in b r ; do
            python rotate_shogi_piece.py $i 2 $j $color
        done
    done
done

# 作成した駒を結合し、MyShogiのフォーマットに変換する
for j in 1 2 3 ; do
    python concat_shogi_pieces.py $j
done

