#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import libpustema

filename = 'dict.txt'

if (len(sys.argv) == 1 or len(sys.argv) > 3):
	print('Proper usage: python3 ' + sys.argv[0] + ' <string> <dictionary>')
if (len(sys.argv) == 2):
	print('Song:\n' + libpustema.Encrypt(filename, sys.argv[1]))
if (len(sys.argv) == 3):
	print('Song:\n' + libpustema.Encrypt(sys.argv[2], sys.argv[1]))
