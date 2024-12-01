-------------------------------------------------------------------------------
AVR ISP / Atmel ATmega48
-------------------------------------------------------------------------------

This is an example capture of the AVR in-system programming (ISP) protocol.

The device used for ISP was a ESP32-S2 containing code to progam the target using ISP.

The target was a board with an Atmel ATmega48 chip.

The capture contains the serial programming instructions:
  - Programming enable
  - Chip erase
  - Poll RDY/nBSY
  - Load program memory page, high byte
  - Load program memory page, low byte
  - Read signature byte
  - Read program memory, low byte
  - Read lock bits
  - Read fuse bits
  - Read fuse high bits
  - Read extended fuse bits
  - Read calibration byte
  - Write program memory page
  - Write fuse bits
  - Write fuse high bits
  - Write extended fuse bits

Logic analyzer setup
--------------------

The logic analyzer used was a Cypress FX2 development board (at 2MHz):

  Probe       AVR ISP header
  -------------------------
  0 (black)   SCK
  1 (brown)   MISO
  2 (red)     MOSI
  3 (orange)  CS
