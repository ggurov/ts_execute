#!/usr/bin/python3
import os
import subprocess
import serial
import time
import sys
import zlib
import struct
import re

def parse_messages(text_block, keyword="msg"):
    pattern = r"`" + re.escape(keyword) + r"`\s*(.*?)(?=`" + re.escape(keyword) + r"`|$)"

    messages = re.findall(pattern, text_block)

    for message in messages:
        print(message.strip()) # .strip() removes leading/trailing whitespace



def m_crc32(c):
	return zlib.crc32(c) & 0xffffffff


def smsg(msg):
	msg1 = struct.pack('>H', len(msg))
	msg2 = bytes(msg)
	msg3 = struct.pack('>I', m_crc32(msg))

	ser.write(msg1 + msg2 + msg3)

def ts_execute(cmd):
	smsg(b"E" + bytes(cmd, "utf8"))

def print_buf(s):
	parse_messages(s.decode(errors='ignore'))

#	for i in range(len(s)):
#		if chr(s[i]) == "`":
#			print("")
#		print(chr(s[i]), end="")



def ts_get_text():
	smsg(b"G")
	s = ser.read(50000)
	print_buf(s)
	s = ser.read(50000)
	print_buf(s)

#	print_buf(s)
#	s = ser.read(50000)
#	print_buf(s)


ser = serial.Serial(port="/dev/ttyUSB0", baudrate=115200, timeout=1)
try:
       	ser.open()
except:
        pass

# smsg(b"E" b"reboot_dfu")
# ts_execute("reboot_dfu")

cmds = sys.argv
cmds.pop(0)

if (cmds):
	ts_execute(' '.join(cmds))

ts_get_text()

ser.close()
