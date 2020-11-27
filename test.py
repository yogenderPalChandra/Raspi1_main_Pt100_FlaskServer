import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D8)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

while True:

    chan1 = AnalogIn(mcp, MCP.P0)
    chan2 = AnalogIn(mcp, MCP.P1)

    print('Raw ADC Value at channel1 : ', chan1.value)
    print('ADC Voltage at channel1: ' + str(chan1.voltage) + 'V') 

    print('Raw ADC Value at channe2: ', chan2.value)
    print('ADC Voltage at channel2: ' + str(chan2.voltage) + 'V')
    print ('______________________________________________________')
    time.sleep(1)

'''
import time

import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D8)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

while True:

    chan1 = AnalogIn(mcp, MCP.P0)
    chan2 = AnalogIn(mcp, MCP.P1)

    print('Raw ADC Value at channel1 : ', chan1.value)
    print('ADC Voltage at channel2: ' + str(chan1.voltage) + 'V')

    print('Raw ADC Value at channe2: ', chan2.value)
    print('ADC Voltage at channel2: ' + str(chan2.voltage) + 'V')
    time.sleep(0.5)
'''


'''
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D8)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)


# create an analog input channel on pin 0
chan1 = AnalogIn(mcp, MCP.P0)
chan2 = AnalogIn(mcp, MCP.P1)

print('Raw ADC Value at channel1 : ', chan1.value)
print('ADC Voltage at channel2: ' + str(chan1.voltage) + 'V')

print('Raw ADC Value at channe2: ', chan2.value)
print('ADC Voltage at channel2: ' + str(chan2.voltage) + 'V')


'''

'''
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D8)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P1)

print('Raw ADC Value: ', chan.value)
print('ADC Voltage: ' + str(chan.voltage) + 'V')
'''
