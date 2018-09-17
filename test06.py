#!/usr/bin/env python
# __*__ coding:utf-8 _*_
__autor__ = "JACK"

# 设计并实现一款菜单
# 	要求：
# 		操作方便，可由用户选择是否退出。

#思路：写一个让用户选择1.话费充值，2.流量充值，3.人工服务，4.退出
import sys
xuanze = ""
def dayin():
    print("""请输入您选择的服务：
    1.话费充值
    2.流量充值
    3.人工服务
    4.退出
    """)
    global xuanze
    xuanze = input("请输入您的选择：")
dayin()

while xuanze == "":
    dayin()
if xuanze == "1":
    print("您选择了话费充值")
elif xuanze == "2":
    print("您选择了流量充值")
elif xuanze == "3":
    print("您选择了人工服务")
elif xuanze == "4":
    print("程序退出")
    sys.exit()
else:
    print("请重新选择")




