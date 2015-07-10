#-*- coding:utf-8 -*-
#파일 입출력 및 예외처리 예제
filename = raw_input("input file name: ")
try:
    f = open(filename + '.txt','r')
except IOError:
    f = open(filename + '.txt', 'w')
    inputtxt = raw_input("input the content: ")
    f.write(inputtxt)
else:
    print f.readline()
    f = open(filename + '.txt', 'a+')
    inputtxt = raw_input("input the content: ")
    f.write(inputtxt)