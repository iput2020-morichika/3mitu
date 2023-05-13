import os 
import datetime
import RPi.GPIO as GPIO
import time
import sys

#センサーポート番号
pin1 = 17

#GPIOの設定
GPIO.setmode(GPIO.BCM)

#GPIOを入力モードに設定してプルダウン抵抗を有効にする
GPIO.setup(pin1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#GPIOの入力を読み取る
#while文で無限ループ
while True:
    try:
        #print(GPIO.input(pin1))
        now = datetime.datetime.now()

        if GPIO.input(pin1) == 0:
            final_time = now
        
        print ("最終ドア開閉時刻：",final_time,)
        print("最後にドアを開閉してから",now.minute-final_time.minute,"分",now.second - final_time.second,"秒経過しています")
        print(pin1)
        time.sleep(1)


    except KeyboardInterrupt:
        GPIO.cleanup()