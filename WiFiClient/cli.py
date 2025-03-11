import network
import socket
import machine
from time import sleep

# WiFiのSSIDとパスワードを設定
ssid = 'playground2'
password = '7j4ukttf'

def connect():
    # WLANに接続
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    # 接続が完了するまで待機
    while not wlan.isconnected():
        print('Waiting for connection...')
        sleep(1)
    
    # IPアドレスを取得
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

try:
    ip = connect()
except KeyboardInterrupt:
    machine.reset()

import urequests
r = urequests.get("https://www.google.com")
print(r.status_code)
print(r.content)
r.close()
