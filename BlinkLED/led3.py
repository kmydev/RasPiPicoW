import machine
import time

led = machine.PWM(machine.Pin(15))  # GPIO 16に接続したLEDをPWMで制御
led.freq(1000)  # PWM周波数を1kHzに設定

while True:
    # フェードイン（0% → 100%）
    for duty in range(0, 65536, 1024):
        led.duty_u16(duty)
        time.sleep(0.01)

    # フェードアウト（100% → 0%）
    for duty in range(65535, -1, -1024):
        led.duty_u16(duty)
        time.sleep(0.01)
