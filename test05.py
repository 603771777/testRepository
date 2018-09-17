#!/usr/bin/env python
# __*__ coding:utf-8 _*_
__autor__ = "JACK"

#密码生成器，生成的为0-9,a-z,A-Z其中的随机数，所以需要random模块和stirng模块来生成
import random,string

sum = ""
for i in range(8):
    suijishu = random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    sum += suijishu

print(sum)
