import time, rtc, os
import socketpool, wifi
import adafruit_ntp
import displayio
import terminalio
import board
from adafruit_display_text import bitmap_label

my_tz_offset = -7 # PDT

''''
# don't need to connect, as we are already conected if .env file has WiFi info
ssid = os.getenv('CIRCUITPY_WIFI_SSID')
password = os.getenv('CIRCUITPY_WIFI_PASSWORD')
wifi.radio.connect(ssid, password)
print("Connected, getting NTP time")
'''
pool = socketpool.SocketPool(wifi.radio)
ntp = adafruit_ntp.NTP(pool, tz_offset=my_tz_offset)
rtc.RTC().datetime = ntp.datetime
print()
print(time.localtime())
display = board.DISPLAY
group = displayio.Group()
clock_area = bitmap_label.Label(terminalio.FONT, text='Time', x=45, y=70, scale=3, color=0x208000)
group.append(clock_area)
date_area = bitmap_label.Label(terminalio.FONT, text='Date', x=40, y=20, scale=3, color=0x804000)
group.append(date_area)
display.show(group)
format_date = '%d/%02d/%02d'
format_time = '%d:%02d:%02d'

while True:
    now = time.localtime()
    last_date = ''
    time_str = format_time % (now.tm_hour,now.tm_min,now.tm_sec)
    date_str = format_date % (now.tm_mon,now.tm_mday,now.tm_year)
    if time_str[6:8] == '00': # print when seconds are zero
        print (date_str,time_str)
    clock_area.text = time_str
    # update date if it changes
    if last_date != date_str:
        last_date = date_str
        date_area.text = date_str
    time.sleep(1)