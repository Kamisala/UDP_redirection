from netfilterqueue import NetfilterQueue
from scapy.all import *
import os
os.system('iptables -A FORWARD -d 10.0.2.3 -j NFQUEUE --queue-num 1')
x=0
def print_and_accept(pkt):
  global x
  data = pkt.get_payload()
  pck = IP(data)
  if(x>=4):

        pck[IP].dst="10.0.2.4"
        del pck[IP].chksum
        del pck[UDP].chksum
        pkt.set_payload(bytes(pck))
  #print("payload:", pkt.get_payload())
  #send(pck)
  pkt.accept()
  x+=1

nfqueue = NetfilterQueue()
nfqueue.bind(1, print_and_accept)

print('ready to try migrate UDP')
try:
    nfqueue.run()
except KeyboardInterrupt:
    print('')
    nfqueue.close()
    os.system('iptables -F')
    os.system('iptables -X')

