# coding:utf-8
# 2018-09-06
# 動作チェック完了：正常
# Pukiwiki のエンコードされたファイル名をデコードするプログラム。
# 引数なし
# stdout に結果を表示。
# 
# 実行結果の末尾部分が下。
#------------------------------
#wiki\C6FCCBDCB8EC.txt ---> 日本語
#wiki\flist_dec.txt ---> flist_dec
#wiki\愛飢えカ・キ・ク・ケ・コ コピー.txt ---> 愛飢えカ・キ・ク・ケ・コ コピー
# ------------------

import binascii
import codecs

#--------------------
# 
#--------------------
def f_name_decode(a_str):
    try:
        ret_str = str(binascii.unhexlify(a_str), 'euc_jp')
    except :
        ret_str = a_str
    return ret_str

#--------------------
# main()
#--------------------
def main():
    # テスト用ディレクトリ：ファイル名がエンコードされたファイルが大量に存在
    enc_file_dir = r".\wiki"

    from pathlib import Path

    p = Path(enc_file_dir)
    f_list = list(p.glob("*.txt"))

    out_path = "out.text"
    fout = codecs.open(out_path, 'w', 'utf-8')

    for a_file in f_list:
        # print(a_file)
        a_name = a_file.stem
        dec_name = f_name_decode(a_name)
        print(a_file, "--->", dec_name)
        
        out_str = dec_name + "<---" + a_name + "\n"
        fout.write(out_str)
    
    fout.close()
    return


#--------------------
if __name__ == '__main__':
    main()

