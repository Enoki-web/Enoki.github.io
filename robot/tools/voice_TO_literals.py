#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @describe :  语音转文字

from aip import AipSpeech
import json

APP_ID = '23020052'
API_KEY = 'GgVPBwdOFFznlPSLSyqnDvx5'
SECRET_KEY = 'GaSBlyHwSVxS1IViYyIKy8b58GgqvCzv'
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
def get_say(WAV):
    content = aipSpeech.asr(get_file_content(r'.\file\demo.wav'), 'wav', 16000, {
        'lan': 'zh',
    })
    data = json.dumps(content)
    say = json.loads(data)['result'][0]     # 得到语音识别成的文字
    return say