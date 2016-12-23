@echo off
netsh wlan set hostednetwork ssid=screenshare key=helloworld123
netsh wlan start hostednetwork
set FINAL='0.0.0.0'
set ip_address_string="IPv4 Address"
for /f "usebackq tokens=2 delims=:" %%f in (`ipconfig ^| findstr /c:%ip_address_string%`) do set FINAL=%%f
echo BY shubhamsharma1172@gmail.com
python main.py %FINAL%