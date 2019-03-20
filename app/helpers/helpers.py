import random
import platform
import subprocess

os = platform.machine()[0:4]

# check if platform is a arvm* processor
# and then import RPi.GPIO
if os == 'armv':
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
else:
    def checkPin(pin_number):
        return random.choice([True, False])
    def setPin(pin_number):
        return random.choice([True, False])

def statusInfo():
    process = subprocess.getstatusoutput('ps -o pid')[1].count('\n')
    uptime = subprocess.getstatusoutput('uptime -p')[1]
    mem_used = subprocess.getstatusoutput('free -m | grep \'Mem\' | cut -c 27-29')[1]
    mem_free = subprocess.getstatusoutput('free -m | grep \'Mem\' | cut -c 38-40')[1]
    sdcard_used = subprocess.getstatusoutput('df -h | grep \'overlay\'| cut -c 36-40')[1]
    sdcard_free = subprocess.getstatusoutput('df -h | grep \'overlay\'| cut -c 46-49')[1]
    sdcard_percent = subprocess.getstatusoutput('df -h | grep \'overlay\'| cut -c 26-30')[1]
    cpu_temp = float(subprocess.getstatusoutput('cat /sys/class/thermal/thermal_zone0/temp')[1][:3]) / 10
    return{
        'process': process,
        'uptime': uptime,
        'cpu_temp': cpu_temp,
        'mem_used': mem_used,
        'mem_free': mem_free,
        'sdcard_used': sdcard_used,
        'sdcard_free': sdcard_free,
        'sdcard_percent': sdcard_percent,
    }
