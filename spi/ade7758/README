50MHz capture of an ADE7758 SPI communications.
Note that Chip Select is _optional_ on this device, provided that you are
careful to only use valid, full length spi read/write requests.

In this case, the chip is configured to provide interrupts on voltage zero
crossings, and the host MCU is reading the status register, and then the
appropriate (phase B) voltage/current registers.

It is largely an example of SPI without CS, in spi mode 0,1.

Two captures are provided.
ade7758-phaseB-zx-irq-context.sr: trigger with precapture on the IRQ pin falling edge.
ade7758-phaseB-zx-irq-nocontext.sr: trigger on spi CLK rising edge.

Correct decodings with the ADE7758 decoder should show
RSTATUS: 0x400
FREQ: 0x0 (frequency is from phase A, not connected on this device)
BVRMS: 0x10cd0c (context) or 0x10ccfa (nocontext)
BIRMS: 0x2ac    (context) or 0x2a8    (nocontext)

Anything else has gotten the SPI decoding wrong due to the lack of chip select.
