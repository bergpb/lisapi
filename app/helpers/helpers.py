import subprocess
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

def checkPin(pin_number):
    try:
        gpio.setup(pin_number, gpio.OUT)
        state = gpio.input(pin_number)
        return True
    except ValueError:
        return False

def setPin(pin_number):
    try:
        gpio.setup(pin_number, gpio.OUT)
        state = gpio.input(pin_number)
        if state == 0:
            gpio.output(pin_number, 1)
            return True
        elif state == 1:
            gpio.output(pin_number, 0)
            return False
    except:
        pass
    
def statusInfo():
    process = subprocess.getstatusoutput('ps -aux | wc -l')[1]
    uptime = subprocess.getstatusoutput('uptime -p')[1]
    mem_used = subprocess.getstatusoutput('free -h | grep \'Mem\' | cut -c 28-30')[1]
    mem_free = subprocess.getstatusoutput('free -h | grep \'Mem\' | cut -c 41-42')[1]
    sdcard_used = subprocess.getstatusoutput('df -h | grep \'/dev\'| cut -c 23-25 | head -1')[1]
    sdcard_free = subprocess.getstatusoutput('df -h | grep \'/dev\'| cut -c 30-31 | head -1')[1]
    sdcard_percent = subprocess.getstatusoutput('df -h | grep \'/dev\'| cut -c 35-36 | head -1')[1]
    local_ip = subprocess.getstatusoutput('ifconfig wlan0 |  grep inet | cut -c 14-26 | head -1')[1]
    cpu_temp = float(subprocess.getstatusoutput('cat /sys/class/thermal/thermal_zone0/temp')[1]) / 1000
    rx_float_mb = round(float(subprocess.getstatusoutput('cat /sys/class/net/wlan0/statistics/rx_bytes')[1]) / 1024 / 1024, 2)
    tx_float_mb = round(float(subprocess.getstatusoutput('cat /sys/class/net/wlan0/statistics/tx_bytes')[1]) / 1024 / 1024, 2)
    return{
        'process': process,
        'uptime': uptime,
        'cpu_temp': cpu_temp,
        'mem_used': mem_used,
        'mem_free': mem_free,
        'sdcard_used': sdcard_used,
        'sdcard_free': sdcard_free,
        'sdcard_percent': sdcard_percent,
        'local_ip': local_ip,
        'network_in' : rx_float_mb,
        'network_out' : tx_float_mb
    }