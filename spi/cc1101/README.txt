-------------------------------------------------------------------------------
CC1101
-------------------------------------------------------------------------------

This directory contains captures of the communication between a CC1101
transceiver, connected to an AVR microcontroller, and another transceiver.


Logic analyzer setup
--------------------

The logic analyzer used was a Saleae Logic clone (at 16 MHz):

  Probe           Description
  ---------------------------
  ch0 (MOSI)      MOSI signal
  ch1 (CLK)       clock signal
  ch2 (MISO)      MISO signal
  ch3 (GDO2)      general purpose output 2 of CC1101, not relevant for the communication
  ch4 (GDO0)      general purpose output 0 of CC1101, used as interrupt signal from CC1101 to AVR microcontroller, active low
  ch5 (CS)        chip select signal, active low


Data
----

The sigrok command line used was:

  sigrok-cli.exe -i cc1101-command-strobe.sr -P spi:clk=SCK:mosi=MOSI:miso=MISO:cs=CS,cc1101

