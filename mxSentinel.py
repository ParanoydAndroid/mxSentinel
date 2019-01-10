from scapy.all import *
from scapy.layers.inet import *


target = 'matrix4.m4i.local'
spoof = 'INSERT PARTNER IP HERE'
payload = "Deactivate!!"
packets = []

def packet_craft(source_port):
    pkt = IP(dst=target)/UDP(sport=source_port, dport=1337)/payload
    return pkt

for i in range(1000):
    source_port = random.randint(1024, 65535)
    temp_packet = packet_craft(source_port)
    packets.append(packet)

print 'done'


