#!/usr/bin/python
#coding=utf-8
def read_file(file):
    with open(file, 'r') as f:
        print(f.read()) # 输出语句
    f.close()

def write_file(file):
    with open(file, 'a') as f:
        for i in range(10):
            f.write(str(i) + '\n')
    f.close()

file = 'test.txt'
write_file(file)
read_file(file)
