from aip import AipSpeech
from playsound import playsound
import glob

""" 你的 APPID AK SK """
APP_ID = '24935549'
API_KEY = 'Ke2nV0X66RwfGiQtSTo64Fa3'
SECRET_KEY = 'vvsfmYSuo0QkAdeRaLxaEu3kLAs5iIE0 '

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result  = client.synthesis('大家好，欢迎来到黄谦敏帅哥的直播间', 'zh', 1, {
    'vol': 5,'per':4
})


# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)
f.close()

song = glob.glob("audio.mp3")[0]
playsound(song)