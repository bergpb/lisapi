import os
import random
import platform
import requests
from flask import jsonify
from subprocess import getstatusoutput, getoutput

operational_system = platform.machine()[0:4]
os.environ['IP_EXTERNAL'] = requests.get('https://bot.whatismyipaddress.com/').content.decode('utf-8')

if operational_system == 'armv':
    import RPi.GPIO as gpio

    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)

    def checkPin(pin_number):
        try:
            gpio.setup(pin_number, gpio.OUT)
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
        except ValueError:
            print('Fail to set pin.')
else:
    def checkPin(pin_number):
        return random.choice([True, False])

    def setPin(pin_number):
        return random.choice([True, False])


def statusInfo():
    process = getstatusoutput('ps aux | wc -l')[1]
    uptime = getstatusoutput('uptime -p')[1].split(',')[0]
    mem_used = int(getoutput("free -m | grep Mem. | awk '{print $6}'"))
    mem_free = int(getoutput("free -m | grep Mem. | awk '{print $7}'"))
    if os == 'armv':
        sdcard_used = getoutput("df -h | grep /dev/root | awk '{print $3}'")
        sdcard_free = getoutput("df -h | grep /dev/root | awk '{print $4}'")
        sdcard_percent = getoutput("df -h | grep /dev/root | awk '{print $5}'")
    else:
        sdcard_used = getoutput("df -h | grep /dev/sda | awk '{print $3}'")
        sdcard_free = getoutput("df -h | grep /dev/sda | awk '{print $4}'")
        sdcard_percent = getoutput("df -h | grep /dev/sda | awk '{print $5}'")
    cpu_temp = float(getstatusoutput("cat /sys/class/thermal/thermal_zone0/temp")[1][:3]) / 10
    ip_internal = getoutput("hostname -I | awk '{print $1}'")
    ip_external = os.getenv('IP_EXTERNAL')
    data = {
        'process': process,
        'uptime': uptime,
        'cpu_temp': cpu_temp,
        'mem_used': mem_used,
        'mem_free': mem_free,
        'sdcard_used': sdcard_used,
        'sdcard_free': sdcard_free,
        'sdcard_percent': sdcard_percent,
        'ip_internal': ip_internal,
        'ip_external': ip_external
    }
    return jsonify(data)
