#!/usr/bin/env python3
#
# A quick script to generate modbus test data, it requires minimalmodbus.
#
# This is free and unencumbered software released into the public domain.

import time

import minimalmodbus

minimalmodbus.PARITY= 'E'

connection = minimalmodbus.Instrument("/dev/ttyUSB0", 1)

while True:
    try:
        time.sleep(.05)

        # function 1
        a = connection.read_bit(3, functioncode=1)

        # function 2
        b = connection.read_bit(0, functioncode=2)

        # function 3
        connection.read_register(99, functioncode=3)

        # function 4
        connection.read_register(120, functioncode=4)

        # funciton 5
        connection.write_bit(3, True, functioncode=5)

        # function 6
        connection.write_register(1, 0b01010101, functioncode=6)

        # function 15
        connection.write_bit(2, True, functioncode=15)

        # function 16
        connection.write_register(1, 0b10101010, functioncode=16)

    except IOError:
        pass
