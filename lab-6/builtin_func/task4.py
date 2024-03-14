import time
import math

def sqRoot_after_ms(number, msec):
    time.sleep(msec / 1000)
    print(f"Square root of {number} after {msec} milliseconds is {math.sqrt(number)}")

sqRoot_after_ms(int(input()), int(input()))