-------------------------------------------------------------------------------
AVR ISP / Atmel ATmega328/P
-------------------------------------------------------------------------------

This is an example capture of the AVR in-system programming (ISP) protocol.

The device used for ISP was a Bus Pirate v3.5 with firmware v6.1.

The target was an Arduino UNO board with an Atmel ATmega328/P chip.

The PC software used for controlling the programmer was avrdude 7.1.


Logic analyzer setup
--------------------

The logic analyzer used was a Saleae Logic Clone (at 4MHz):

  Probe       AVR ISP header
  -------------------------
  1           MOSI
  2           MISO
  3           SCK
  4           RST


Data
----

The following avrdude commands were captured:

    avrdude -p atmega328p -c buspirate -P /dev/ttyUSB0 -v
