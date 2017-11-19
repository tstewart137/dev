from scapy.all import *
 
def arp_detect(pkt):
    if pkt[ARP].op == 1: #network request
	
        
        print sniff(prn=arp_display, filter="arp", store=0)