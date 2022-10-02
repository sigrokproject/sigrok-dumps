##
## This file is part of the sigrok-dumps project.
##
## Copyright (C) 2012 Uwe Hermann <uwe@hermann-uwe.de>
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
## along with this program; if not, see <http://www.gnu.org/licenses/>.
##

VERSION = "0.1.0"

# TODO Ideally instructions would use autotools, cmake, or some other
# higher level abstraction instead of DIY shell commands. Which would
# improve portability and robustness (by picking the most appropriate
# install tool that is available on the target), and would transparently
# enable support for --prefix and DESTDIR et al, including out of source
# builds when desired.
PREFIX ?= /usr/local
INSTALL_DIR = $(PREFIX)/share/sigrok-dumps

# Be explicit about which files or subdirectories to install.
# Update this list when adding a new top level subdirectory to the
# set of example captures. It's assumed that this event is rare.
# The list is phrased such that users can specify additional items
# when they invoke the 'make install' command.
FILES_DIRS += ac97 am230x arm_trace aud avr_isp avr_pdi
FILES_DIRS += caliper can cec
FILES_DIRS += dac dali dcc dcf77 display dmx512 dsi
FILES_DIRS += flexray fsk
FILES_DIRS += gpib graycode
FILES_DIRS += i2c i2s ir
FILES_DIRS += jtag
FILES_DIRS += led lens_mounts lpc
FILES_DIRS += maple_bus mcs48 mdio microwire miller misc morse mouse_sensors
FILES_DIRS += nfc nonstandard_eeproms
FILES_DIRS += onewire ook
FILES_DIRS += pjon ps2 pwm
FILES_DIRS += qi
FILES_DIRS += rc rfid
FILES_DIRS += sae-j1850 sdcard sdq sht7x signature sle44xx spdif spi
FILES_DIRS += stepper_motor swd swim
FILES_DIRS += tdm_audio
FILES_DIRS += uart usb usb_power_delivery
FILES_DIRS += vfd
FILES_DIRS += wiegand
FILES_DIRS += xy2-100
FILES_DIRS += z80

all:
	@echo "Run 'make dist' to create a tarball."

ChangeLog:
	git log > ChangeLog || touch ChangeLog

dist: ChangeLog
	@tar -c -v -z --exclude=.git --exclude=Makefile \
		--exclude=sigrok-dumps-$(VERSION).tar.gz \
		-f sigrok-dumps-$(VERSION).tar.gz *
	@rm -f ChangeLog

install:
	@mkdir -p $(DESTDIR)$(INSTALL_DIR)
	@cp -r $(FILES_DIRS) $(DESTDIR)$(INSTALL_DIR)
