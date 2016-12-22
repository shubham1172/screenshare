@echo off
netsh wlan set hostednetwork ssid='screenshare' key='helloworld123'
netsh wlan start hostednetwork
echo BY shubhamsharma1172@gmail.com
python main.py 