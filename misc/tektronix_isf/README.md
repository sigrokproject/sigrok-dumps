# Tektronix ISF file format
This directory contains sample Tektronix ISF files organized into two
subdirectories.

Directory `DS1307Z` contains a dump of I<sup>2</sup>C communication
of [DS1307Z RTC module](https://www.analog.com/media/en/technical-documentation/data-sheets/ds1307.pdf).
Each file corresponds to a single line as the ISF format only supports one
channel per file. Files `tek0000CH1.isf` and `tek0000CH2.isf` represent SDL
and SCL, respectively. The corresponding `.csv` and `.sr` files are also
included.

Directory `RF` contains samples of radio communication that were captured
randomly, without any particular context. The purpose of this directory
is to provide examples with different encoding parameters from those in the
`DS1307Z` directory.
