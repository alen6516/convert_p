#####
# File Name: convert.py
# Author: alen6516
# Created Time: 2017-10-14
#####
import sys
import chardet
from langconv import *

def S2T(line):
    line = Converter('zh-hant').convert(line.decode('utf-8'))
    return line.encode('utf-8')

def T2S(line):
    line = Converter('zh-hans').convert(line.decode('utf-8'))
    return line.encode('utf-8')

if __name__=='__main__':
    print("********************************************************")
    print("*this module convert file encoding from gb2312 to utf-8*")
    print("********************************************************")
    if len(sys.argv) <2:
        file_name=raw_input("give the file name:")
    else:
        file_name = sys.argv[1]
    r=open(file_name)
    result='result_'+file_name
    w=open(result, 'w')

    
    print("input file_name = %s" % file_name)
    print("output file_name = %s" % result)
    print("converting ...")

    for line in r:
        w.write(S2T(line.decode('GB2312', 'replace').encode('utf-8')))
        #w.write(S2T(line))
    print("conversion done")
