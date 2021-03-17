import os
import platform
import random
import socket
from subprocess import getstatusoutput

import requests

import psutil
from flask import jsonify

operational_system = platform.machine()[0:4]

if operational_system == 'armv':
    """Change pin in Raspberry Pi device"""
    import RPi.GPIO as gpio

    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)

    def check_pin(pin_number):
        try:
            gpio.setup(pin_number, gpio.OUT)
            return True
        except ValueError:
            return False

    def set_pin(pin_number):
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
            pass
else:
    """Return a random True or False"""
    import random
    def check_pin(pin_number):
        return bool(random.getrandbits(1))

    def set_pin(pin_number):
        return bool(random.getrandbits(1))


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip


os.environ['IP_INTERNAL'] = get_ip()


def status_info():
    process = getstatusoutput('ps aux | wc -l')[1]
    uptime = getstatusoutput('uptime -p')[1].split(',')[0]
    mem_percent = psutil.virtual_memory()[2]
    disk_percent = psutil.disk_usage('/')[3]
    cpu_percent = psutil.cpu_percent()
    cpu_temp = float(getstatusoutput("cat /sys/class/thermal/thermal_zone0/temp")[1][:3]) / 10
    ip_internal = os.getenv('IP_INTERNAL')
    ip_external = os.getenv('IP_EXTERNAL')
    data = {
        'process': process,
        'uptime': uptime,
        'cpu_temp': cpu_temp,
        'cpu_percent': cpu_percent,
        'mem_percent': mem_percent,
        'disk_percent': disk_percent,
        'ip_internal': ip_internal,
    }
    return jsonify(data)
