import board
import digitalio
import busio
import time
import adafruit_mpu6050

class gyro:
    def __init__(self):
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


    def connect_i2c(self):

        self.i2c = board.I2C()
        self.mpu = adafruit_mpu6050.MPU6050(self.i2c)

    def return_data(self):
        return self.mpu.gyro