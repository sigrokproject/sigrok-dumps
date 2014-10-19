#!/usr/bin/env python3
##
## This file is part of the sigrok-dumps project.
##
## Copyright (C) 2014 Jens Steinhauser <jens.steinhauser@gmail.com>
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA
##

## This script generates test cases for the nrf24l01 protocol decoder.

import csv
import subprocess
import tempfile

class SPI:
    def __init__(self, filename):
        self._filename = filename
        self._data = []

    def CSlow(self):
        self._data.append([1, 0, 0, 0])
        self._data.append([0, 0, 0, 0])

    def CShigh(self):
        self._data.append([0, 0, 0, 0])
        self._data.append([1, 0, 0, 0])

    def add(self, mosi, miso):
        for _ in range(8):
            mo = (mosi & 0x80) >> 7
            mi = (miso & 0x80) >> 7
            mosi <<= 1
            miso <<= 1
            self._data.append([0, 0, mo, mi])
            self._data.append([0, 1, mo, mi])

        self._data.append([0, 0, 0, 0])

    def write(self):
        with tempfile.NamedTemporaryFile() as tf:
            with open(tf.name, 'w') as tff:
                w = csv.writer(tff)
                w.writerow(['CS', 'CLK', 'MOSI', 'MISO'])
                w.writerows(self._data)

            fn = '{}.sr'.format(self._filename)
            I = 'csv:header=true:samplerate=1000'
            subprocess.check_call(['sigrok-cli', '-I', I, '-i', tf.name, '-o', fn])

spi = SPI('nrf24l01-test-activate')
spi.CSlow()
spi.add(0x50, 0x00) # ACTIVATE
spi.add(0x73, 0x00) # correct payload
spi.CShigh()
spi.CSlow()
spi.add(0x50, 0x00) # ACTIVATE
spi.add(0x74, 0x00) # wrong payload
spi.CShigh()
spi.write()

spi = SPI('nrf24l01-test-excess-bytes')
spi.CSlow()
spi.add(0x00, 0x00) # R_REGISTER, reg = CONFIG
spi.add(0x00, 0x00)
spi.CShigh()
spi.CSlow()
spi.add(0x00, 0x00) # R_REGISTER, reg = CONFIG
spi.add(0x00, 0x00)
spi.add(0x00, 0x00) # excess
spi.CShigh()
spi.CSlow()
spi.add(0x20, 0x00) # W_REGISTER, reg = CONFIG
spi.add(0x00, 0x00)
spi.add(0x00, 0x00) # excess
spi.CShigh()
spi.CSlow()
spi.add(0x20, 0x00) # W_REGISTER, reg = CONFIG
spi.add(0x00, 0x00)
spi.add(0x00, 0x00) # excess
spi.add(0x00, 0x00) # excess
spi.CShigh()
spi.CSlow()
spi.add(0x2a, 0x00) # W_REGISTER, reg = RX_ADDR_P0
spi.add(0x00, 0x00)
spi.add(0x00, 0x00)
spi.add(0x00, 0x00)
spi.add(0x00, 0x00)
spi.add(0x00, 0x00)
spi.add(0x00, 0x00) # excess
spi.CShigh()
spi.CSlow()
spi.add(0x2c, 0x00) # W_REGISTER, reg = RX_ADDR_P2
spi.add(0x00, 0x00)
spi.add(0x00, 0x00) # excess
spi.CShigh()
spi.CSlow()
spi.add(0xa0, 0x00) # W_ACK_PAYLOAD, pipe = 0
for i in range(33):
    spi.add(i, 0x00) # write 33 bytes, command only expects 32
spi.CShigh()
spi.write()

spi = SPI('nrf24l01-test-missing-bytes')
spi.CSlow()
spi.add(0x00, 0x00) # R_REGISTER, reg = CONFIG
spi.CShigh()
spi.CSlow()
spi.add(0xb0, 0x00) # W_TX_PAYLOAD_NOACK
spi.CShigh()
spi.write()

spi = SPI('nrf24l01-test-no-command')
spi.CSlow()
spi.CShigh()
spi.CSlow()
spi.CShigh()
spi.CSlow()
spi.add(0x00, 0x00) # R_REGISTER, reg = CONFIG
spi.add(0x00, 0x00)
spi.CShigh()
spi.CSlow()
spi.CShigh()
spi.CSlow()
spi.add(0x00, 0x00) # R_REGISTER, reg = CONFIG
spi.add(0x00, 0x00)
spi.CShigh()
spi.write()

spi = SPI('nrf24l01-test-unknown-register')
spi.CSlow()
spi.add(0x1f, 0x00) # R_REGISTER, reg = 0x1f
spi.add(0x00, 0x00)
spi.CShigh()
spi.write()

spi = SPI('nrf24l01-test-unknown-command')
spi.CSlow()
spi.add(0x00, 0x00) # R_REGISTER, reg = CONFIG
spi.add(0x00, 0x00)
spi.CShigh()
spi.CSlow()
spi.add(0xf0, 0x00) # wrong command
spi.add(0x00, 0x00)
spi.CShigh()
spi.CSlow()
spi.add(0x20, 0x00) # W_REGISTER, reg = CONFIG
spi.add(0x00, 0x00)
spi.CShigh()
spi.write()

spi = SPI('nrf24l01-test-misc')
spi.CSlow()
spi.add(0xe3, 0x00) # REUSE_TX_PL
spi.CShigh()
spi.CSlow()
spi.add(0x60, 0x00) # R_RX_PL_WID
spi.add(0x00, 0x09)
spi.CShigh()
spi.CSlow()
spi.add(0x60, 0x00) # R_RX_PL_WID
spi.CShigh()
spi.CSlow()
spi.add(0x60, 0x00) # R_RX_PL_WID
spi.add(0x00, 0x09)
spi.add(0x00, 0x09) # excess
spi.CShigh()
spi.CSlow()
spi.add(0xa9, 0x00) # W_ACK_PAYLOAD, pipe = 1
for i in range(5):
    spi.add(i, 0x00)
for c in 'abcdef':
    spi.add(ord(c), 0x00)
for i in range(5):
    spi.add(i, 0x00)
spi.CShigh()
spi.write()

spi = SPI('nrf24l01-test-incomplete-cmd')
spi.add(0xff, 0xff) # some bytes from a command
spi.add(0xff, 0xff) # that was captured incompletely
spi.CShigh()
spi.CSlow()
spi.add(0xe1, 0x00) # FLUSH_TX
spi.CShigh()
spi.write()
