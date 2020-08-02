-------------------------------------------------------------------------------
AVR ISP / Atmel ATmega8L
-------------------------------------------------------------------------------

This is a set of example captures of the AVR in-system programming (ISP)
protocol. The target was a board with an Atmel ATmega8L chip, and another
microcontroller was used as master for the ISP process.

Details:
http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-2486-8-bit-AVR-microcontroller-ATmega8_L_datasheet.pdf


Logic analyzer setup
--------------------

The logic analyzer used was a Saleae Logic (at 4MHz):

  Probe       AVR ISP header
  -------------------------
  5 (green)   MOSI
  6 (blue)    CLK
  7 (violet)  MOSI
