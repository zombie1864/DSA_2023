'''  
    Requires a lot of knowledge and is more geared for mid-senior lvl softwware engineers
    Most of the time, if asked, it would be "How would you design this app/web/etc" 

    [3-clinet-server model]: 
        []_client talks to server via an API. 
            - Client is an app that makes the req for data 

        []_Server provides data by listening for incoming network calls 

        []_client-server model is a paradign which consists of client req for data and 
        server resp with the data 

        []_relies on HTTP, TCP, and IP 
            - HTTP is the standard API used for network calls 
            - TCP (Transmission Control Protocol) is the standard that defines how 
            to establish and maintain a network conversation 
                - types of network calls: 
                    1. HTTP 
                    2. Web socket 
            TCP is under the hood of HTTP and web sockets 
            - IP (internet protocol) defines how packets of data is exchanged 

        []_client-side makes HTTP request and the HTTP makes a DNS query req 
            - DNS query req searches for web-address's IP address 
            - for every URL address there is an associated IP address that goes with it 
            - IPv4 addresses consists of four numbers `a.b.c.d` where all four numbers are 
            between 0 and 255, e.g. localhost is 127.0.0.1
            - Usually IP addresses are provided by an internet entity, AWS or google 
                - these entites provide IP addresses that are associated with a website/server 
            - both the client has the IP address of the server AND the server has the IP 
            address of the client so that both can exchange data 
                - HTTP sends req with IP address of client 
                - HTTP sends resp with IP address of server 
                - in each end TCP is listening and awaiting info from the provided IP address 
                    - a port is used to listen for info 

    [4-Network Protocols]: 
        []_IP address: an address given to each machine connected to the public 
        internet. IPv4 consits of four numbers separated by dots `a.b.c.d` 
            - all four numbers are between 0 and 255 
            - private networks will always be in the following format 
                192.168.c.d
'''