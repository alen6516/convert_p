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

if __name__=='__main__':
    print("***********************************************************")
    print("* this module decodes file in gb and encodes to utf-8 *")
    print("***********************************************************")
    if len(sys.argv) <2:
        file=raw_input("give the file name:")
    else:
        file = sys.argv[1:]
    for file_name in file:
        fo=open(file_name, "r", encoding="gbk", errors="replace")
        result='result_'+file_name
        fw=open(result, 'w')
        
        print("input file_name = %s" % file_name)
        print("output file_name = %s" % result)
        print("converting ...")

        for line in fo.readlines():
            fw.write(S2T(line))
        print("%s done" % file_name)
    print("conversion done")
