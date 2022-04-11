--------------------------------
PS/2 Mouse
--------------------------------

This is a collection of PS/2 mice communication examples.

For details see:
http://www-ug.eecg.utoronto.ca/desl/nios_devices_SoC/datasheets/PS2%20Protocol.htm
http://www-ug.eecg.utoronto.ca/desl/nios_devices_SoC/datasheets/PS2%20Mouse%20Protocol.htm


ps2_microsoft_mouse_initialize_and_move.sr
------------------------------

This file contains setup and communication between a Windows host and a microsoft mouse.
The host releases the clock simultaneous to pulling the data low, which makes it challenging to 
distinguish between "request-to-send" and a regular start-bit.

Initialize a ps2 mouse, configure it; the mouse then reports movement data.

- host resets device, waits for reset to complete
- host sets sample rate to 200, 100, 80 - this activates reporting scroll wheel data is available
- host sets device to maximum sample rate: 200; resolution=1: 2 count/mm; 1:1 scaling, stream mode
- host gets device id, enable data reporting
- after a delay, the mouse is moved, and reports it's changing location, in sequences of 4 bytes:
    - flags, x movement, y movement, z (scroll wheel) movement.
    - the sample data does not include any button presses or scroll wheel movement

