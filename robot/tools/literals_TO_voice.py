#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @describe :  文字转语音

import os
from aip import AipSpeech

APP_ID = '23020052'
API_KEY = 'GgVPBwdOFFznlPSLSyqnDvx5'
SECRET_KEY = 'GaSBlyHwSVxS1IViYyIKy8b58GgqvCzv'
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def say(say,WAV):
    """
    文字转语音
    :param say: 文字， 这里是机器人的回答
    :return:
    """
    result = aipSpeech.synthesis(say, 'zh', 1, {'vol': 5,'per':4}) # 百度api相关方法
    # 检查本目录下是否存在test.mp3文件,如果存在则删除,方便之后创建新的mp3文件
    if os.path.exists(WAV):
        os.remove(WAV)
    # 百度api返回的结果 result 有时候是一个dict类型，写入到mp3会报错
    if not isinstance(result,dict):
        try:
            with open(WAV,'wb') as f:
                f.write(result)
        except IOError as e:
            print e