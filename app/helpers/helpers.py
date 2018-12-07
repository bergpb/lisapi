# import RPi.GPIO as gpio

# gpio.setmode(gpio.BCM)
# gpio.setwarnings(False)

# def checkPin(pin_number):
#     try:
#         gpio.setup(pin_number, gpio.OUT)
#         state = gpio.input(pin_number)
#         return True
#     except ValueError:
#         return False

# def setPin(pin_number):
#     try:
#         gpio.setup(pin_number, gpio.OUT)
#         state = gpio.input(pin_number)
#         if state == 0:
#             gpio.output(pin_number, 1)
#             return True
#         elif state == 1:
#             gpio.output(pin_number, 0)
#             return False
#     except:
#         pass

def checkPin(pin_number):
    return True
    
def setPin(pin_number):
    return True