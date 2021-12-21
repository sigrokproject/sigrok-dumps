# TPM transactions over SPI

This is an example capture of TPM 2.0 transactions over SPI.

The logic analyzer used to capture this signal was a DSLogic Pro.

## Logic analyzer setup

The logic analyzer used was a DSLogic Pro (at 250MHz):

  Probe       SPI connector
  -------------------------------------
  1 (black)   CLK
  2 (brown)   CS
  3 (red)     MOSI
  4 (orange)  MISO


## Capture (tpm_spi.sr)

PulseView GUI was used to perform the capture.
Here is the detail of the configuration:

### SPI decoder configuration

CS#: CS (Probe 2)
MOSI: MOSI (Probe 3)
CLK: CLK (Probe 1)
MISO: MISO (Probe 4)

CS# Polarity: Active low 
Clock polarity: 0
Clock phase: 0
Bit order: msb-first
Word size: 8

### SPI TPM stack decoder configuration
Stack Decoder: SPI TPM
TPM Wait transfer Mask: 0x00

## Output 

TPM transactions are shown on the `TPM transactions` label.
If the BitLocker Volume Master Key (VMK) is found, it should show it through the `BitLocker Volume Master Key` label.
