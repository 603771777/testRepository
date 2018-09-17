#!/usr/bin/env python
# __*__ coding:utf-8 _*_
__autor__ = "JACK"

# 先读取一个文件，然后写入新文件中

def copyFile(path):
    oldFile = open(path,"r")
    newFile = open("/tmp/6.txt","a")
    for line in oldFile:
        newFile.write(line)
        if line == "":
            break
    oldFile.close()
    newFile.close()

copyFile("/home/6")



