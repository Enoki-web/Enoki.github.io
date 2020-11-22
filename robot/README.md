# robot
基于Python2.7开发的语音聊天机器人

# 要安装的包有: 
- pyaudio  
- baidu-aip  
- mp3play  

# 安装方法: 
``` python
pip install pyaudio
pip install baidu-aip
pip install mp3play
```

# 使用方法:
1. 注册百度语音开发者，得到百度语音API key [点我前往](http://yuyin.baidu.com/ "百度语音") 
2. 注册极速数据，申请智能问答机器人数据，得到智能问答机器人app_key [点我前往](https://www.jisuapi.com/api/iqa/ "极速数据")
3. 打开tools文件夹下*literals_TO_voice.py*和*voice_TO_literals.py*找到需要填入数据的地方，填入你申请到的api_key 等信息
4. 打开*rbot.py* 找到需要填入数据的地方，填入你申请到的app_key
5. 运行*main.py* 开始和机器人聊天
