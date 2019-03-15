#####
# File Name: convert.py
# Author: alen6516
# Created Time: 2017-10-14
#####
import sys
import chardet
from langconv import *

def S2T(string):
    return Converter('zh-hant').convert(string)
    

def T2S(string):
    return Converter('zh-hans').convert(string)


def get_encode(lines):
    big5_count = 0
    gb2312_count = 0
    for i in range(20):
        if chardet.detect(lines[i])['encoding'] == 'Big5':
            big5_count += 1
        elif chardet.detect(lines[i])['encoding'] == 'GB2312':
            gb2312_count += 1

    return 'Big5' if big5_count >= gb2312_count else "GB2312"


if __name__=='__main__':
    print("***********************************************************")
    print("* this module decodes file in gb and encodes to utf-8 *")
    print("***********************************************************")
    if len(sys.argv) <2:
        file=raw_input("give the file name:")
    else:
        file = sys.argv[1:]
    for file_name in file:

        fo=open(file_name, 'rb')
        lines = fo.readlines()
        fo.close()

        encode_type = get_encode(lines)

        if encode_type == "GB2312":
            print("%s is encoded by GB2312" % file_name)
        elif encode_type == "Big5":
            print("%s is encoded by Big5" % file_name)

        result='result_'+file_name
        
        print("input file_name = %s" % file_name)
        print("output file_name = %s" % result)
        print("converting ...")

        fw=open(result, 'w')
        for line in lines:
            fw.write(S2T(line.decode(encode_type, errors="replace")))
        fw.close()
        print("%s done" % file_name)
    print("conversion done")
