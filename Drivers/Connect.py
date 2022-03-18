import board
import digitalio
import busio
import time
import adafruit_adx134x

def check_connections():
    try:
        pin = digitalio.DigitalInOut(board.D4)
    except:
        print("problems with DIO")
    try:
        i2c = busio.I2C(board.SCL, board.SDA)
    except:
        print("I2C not working properly")

    try:
        spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
    except:
        print("SPI not working properly")


def connect_i2c():

    i2c = board.I2C()
    accel = adafruit_adx134x.ADXL343(i2c)

    while True:
        print(accel.acceleration)
        time.sleep(0.2)