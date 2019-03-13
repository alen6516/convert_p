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


def if_encode_by_GB2312(lines):
    count = 0
    for i in range(10):
        if chardet.detect(lines[i])['encoding'] == 'GB2312':
            count += 1
    
    return True if count >=5 else False

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

        if if_encode_by_GB2312(lines):
            print("%s is encode by GB2312" % file_name)
        else:
            print("%s is not encode by GB2312, ignore" % file_name)
            continue

        result='result_'+file_name
        
        print("input file_name = %s" % file_name)
        print("output file_name = %s" % result)
        print("converting ...")

        fw=open(result, 'w')
        for line in lines:
            fw.write(S2T(line.decode('gbk')))
        fw.close()
        print("%s done" % file_name)
    print("conversion done")
