-------------------------------------------------------------------------------
Microchip MCP23017 I/O expander with I2C interface
-------------------------------------------------------------------------------

This is a set of example captures of the MCP23017 16-bit I/O expander with
an I2C interface. For details see the MCP23017/MCP23S17 datasheet which is
titled "16-Bit I/O Expander with Serial Interface":

  http://ww1.microchip.com/downloads/en/DeviceDoc/20001952C.pdf


Logic analyzer setup
--------------------

The logic analyzer used was a Saleae clone (samplerate 1MHz). In addition
to the I2C datalines, 6 output pins are captured too.

The host was a Raspberry Pi using Python to access the I2C port. The bitrate
decreased after a few 100ms.

  Probe       MCP23017
  -------------------
  0           A0
  1           A1
  2           A2
  3           B0 / A3
  4           B1 / A4
  5           B2 / A5
  6           SDA
  7           SCL


mcp23017_counter_a_write.sr
---------------------------

Count the Registers OLATA ascending. The lowest 6 bits of the Output A Port
are captured too (A0 - A5).


mcp23017_counter_init_ab_write.sr
---------------------------------

Reset all registers, then count the registers OLATA ascending and OLATB
descending. Both registers are set using one word write operation. The
lowest 3 bits of both output ports are captured too (A0 - A2, B0 - B2).


mcp23017_counter_init_ab_write_read.sr
-------------------------------------

Reset all registers, then count the registers OLATA ascending and OLATB
descending. Both registers are set and read using one word write operations.
The lowest 3 bits of both output ports are captured too (A0 - A2, B0 - B2).
