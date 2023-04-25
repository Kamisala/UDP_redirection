# UDP_Redirction
This project describes a UDP redirection technique via NetfilterQueue.
## Design Topology
![image](https://user-images.githubusercontent.com/105418310/234156963-c9e6d2d5-277b-43df-938e-718be3527ea0.png)
In a normal case, the Client sends a request_message_1 (for example, "I am client") to Server 1, and Server1 will respond to a response_message_1 (for example, "I am server 1"). Specifically, when the Client connects to Server 1, the Server will print n "I am clients" in the terminal, while the Client will print n "I am server 1". However, when we use UDP redirection technology in Gateway to redirect network traffic, Gateway will redirect network traffic to Server 2 at some point, which will result in subsequent request information from the Client being printed on server 2. At the same time, the subsequent response message received by the Client will be the response_message_2 (for example, "I am server 2") from Server 2. For example, the terminal of Server 1 prints m "I am client" information, the terminal of Server 2 prints n "I am client" information, and the Client terminal prints m "I am server 1" and n "I am server 2" information.
## Setup
1. Running: mn.py in terminal of Virtual Machine, and open the terminal of h1, h2, h3, h4
![截屏2023-04-21 上午11 37 27](https://user-images.githubusercontent.com/105418310/233535166-0e3e01c0-9350-4a61-b502-2a016411ea9d.jpg)
2. Running: nf.py in h2; s1.py in h3; s2.py in h4; c1.py in h1
![截屏2023-04-21 上午11 39 01](https://user-images.githubusercontent.com/105418310/233535352-c67da04a-6409-4c99-a744-74755fcc4b68.jpg)
We can see that:  There are 4 UDP data interactions between h1 and h3，and there are 6 UDP data interactions between h1 and h4.
## Contributing
This project provides an idea of udp redirection based on netfilterqueue.
## Contact
LLY - atomy.lly@gmail.com
