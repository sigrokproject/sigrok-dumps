##
## This file is part of the sigrok project.
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
## along with this program; if not, write to the Free Software
## Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA
##

VERSION = "0.1.0"

DESTDIR ?= /usr/local/share/sigrok-dumps

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
	@mkdir -p $(DESTDIR)
	@cp -r * $(DESTDIR)
	@rm -f $(DESTDIR)/Makefile

