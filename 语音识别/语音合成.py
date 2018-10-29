from aip import AipSpeech
import pygame
import os
import time
os.chdir(r'C:\Users\outao\Desktop\合成的语音')
APP_ID = '14442796'
API_Key = 'FraivQGZbx1HWSyFKoYMFA18'
Secret_Key = 'EPf7caqa68hHDk2doE06Y643D2kuZGfl'
client = AipSpeech(APP_ID, API_Key, Secret_Key)
result = client.synthesis('亲爱的我爱你',  'zh', 1, {'per': '3'})
f = open('test.mp3', 'wb')
f.write(result)
f.close()
# print("播放音乐1")
# pygame.mixer.init()
# # 加载音乐
# pygame.mixer.music.load(r'C:\Users\outao\Desktop\合成的语音\test.mp3')
# while True:
#     # 检查音乐流播放，有返回True，没有返回False
#     # 如果没有音乐流则选择播放
#     if pygame.mixer.music.get_busy() == False:
#         pygame.mixer.music.play()



