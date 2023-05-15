import asyncio
from os import listdir

from time import time


# list available interfaces
print(listdir('/sys/class/net/'))


# sudo airodump-ng wlan1 --essid ATTBRyYu7C -w asdf --output-format cap

'''
import pyshark
cap = pyshark.FileCapture('asdf-01.cap')
for packet in cap:
    try:
        print(packet.data.data)
        for x in packet:
            print(x)
    except:
        pass
'''

import pyshark
for packet in pyshark.FileCapture("WiFiUFO_211267.cap"):
    if not hasattr(packet, 'ip'):
        continue
    #print(packet.layers)
    '''
    if hasattr(packet, "ip"):
        print(packet.ip.src)
        print(packet.ip.dst)
    if hasattr(packet, 'udp'):
        print(packet.udp.srcport)
        print(packet.udp.dstport)
    if hasattr(packet, "dns"):
        print(packet.dns.name)
    '''
    #if hasattr(packet, 'data'):
    #    print(packet.udp.payload)
    if hasattr(packet, 'dns'):
        print(packet.dns.qry_name)


'''
capture = pyshark.LiveCapture(interface='wlan1')
for packet in capture.sniff_continuously(packet_count=5):
    #if hasattr(packet, 'ip'):
        #print(f"[{packet.ip.src} to {packet.ip.dst}]")
        #print(packet.transport_layer)
        #print(packet.highest_layer)
    print(packet.layers)
    #print(packet.WLAN)
'''



# Findings
'''
wifi name = WiFiUFO_21267
no encryption, but the data sent is in hex anyway

need to skip resent packets
The drone itself is 192.168.28.1
the attached phone is 192.168.28.2

There are occasionally dns requests _from the phone_ for www.google.com and connectivitycheck.gstatic.com
Crappy programming I guess

commands (phone to drone) are 14 bytes (out of 76 byte packet length)
video(?) (drone to phone) is variable in length but mostoften 1472/1534 bytes

it would probably be useful save to new files each time you're trying a new action
    alternatively take pictures between each action
'''