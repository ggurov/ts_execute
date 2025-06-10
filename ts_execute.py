#!/usr/bin/python3
import os
import subprocess
import serial
import time
import sys
import zlib
import struct
import re
import binascii


def hex_str(s):
#	return (binascii.hexlify(s))
#        return ':'.join(hex(ord(x))[2:] for x in s)
	data = s
	hex_data = data.hex()

	hex_data_spaced = " ".join(data.hex()[i:i+2] for i in range(0,len(data.hex()),2))
	return (hex_data_spaced) # Output: 01 02 03 04


def parse_messages(text_block, keyword="msg"):
    pattern = re.escape(keyword) + r"`([^`]+)`"

    messages = re.findall(pattern, text_block)


    l = []
    for message in messages:
#	        print(message.strip())
        l.append(message.strip())

    return l



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
# b'\x00\x01\x00\xd2\x02\xef\x8d\x12\x86\x00
	ser.read(5000);
	smsg(b"G")
	s = ser.read(2)
# 	print(hex_str(s[0:32]))
#	len1 = int(s[0]) << 8 + int(s[1])
	len = (s[0] << 8) + (s[1])
# 	print("got Len: " , len)
	s = ser.read(len)
	lines = parse_messages(s[1:].decode())
	for line in lines:
		print(line)

# 	print(parse_messages(s[1:].decode(), 'wave_chart'))
# 	print(s[1])
# 	print("len: ", len1)

# 	print(s)
# 	print_buf(s)
#	s = ser.read(5000)
#	print_buf(s)
#	s = ser.read(5000)
#	print_buf(s)

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
# b'\x00\x01\x00\xd2\x02\xef\x8d  \xc2 \x00    msg`Incor
# b'\x00\x01\x00\xd2\x02\xef\x8d  \x0f \x00    msg`Got co
# b'\x00\x01\x00\xd2\x02\xef\x8d  \x0e \x83\x00msg`Reading egt(s)`msg`egt1: type max31855,
# b'\x00\x01\x00\xd2\x02\xef\x8d  \x19    d\x00msg`Got content [1572]
