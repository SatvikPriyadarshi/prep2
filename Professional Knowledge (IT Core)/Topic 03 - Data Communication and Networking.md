# Topic 3: Data Communication & Networking

## 📝 Quick Revision Cheat Sheet (Before you start)

- **OSI Model (7 Layers):** Physical, Data Link, Network, Transport, Session, Presentation, Application. (Mnemonic: Please Do Not Throw Sausage Pizza Away)
- **TCP/IP Model (4 Layers):** Network Access, Internet, Transport, Application.
- **IP Address Classes:** A (1-126), B (128-191), C (192-223), D (224-239, Multicast), E (240-255, Experimental).
- **Private IP Ranges:** 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16.
- **Protocols by Layer:** Application (HTTP, FTP, SMTP, DNS), Transport (TCP, UDP), Internet (IP, ICMP, ARP), Network Access (Ethernet, Wi-Fi).
- **Topologies:** Bus, Star, Ring, Mesh, Tree, Hybrid.

## Part A: OSI Model & TCP/IP (Questions 1-30)


### 1. How many layers are there in the OSI model?
- A) 4
- B) 5
- C) 6
- D) 7

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** The OSI (Open Systems Interconnection) model has 7 layers.

</details>

### 2. Which layer of the OSI model is responsible for physical transmission of data?
- A) Data Link
- B) Physical
- C) Network
- D) Transport

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Physical layer transmits raw bits over a communication channel.

</details>

### 3. Which layer of the OSI model is responsible for framing?
- A) Physical
- B) Data Link
- C) Network
- D) Transport

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Data Link layer converts raw bits into frames and handles error detection.

</details>

### 4. Which layer of the OSI model is responsible for routing?
- A) Data Link
- B) Network
- C) Transport
- D) Session

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Network layer handles logical addressing (IP) and routing of packets.

</details>

### 5. Which layer of the OSI model is responsible for end-to-end delivery?
- A) Network
- B) Transport
- C) Session
- D) Presentation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Transport layer provides reliable end-to-end data transfer (TCP/UDP).

</details>

### 6. Which layer of the OSI model establishes, manages, and terminates sessions?
- A) Transport
- B) Session
- C) Presentation
- D) Application

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Session layer manages dialogue control and synchronization between applications.

</details>

### 7. Which layer of the OSI model is responsible for data translation, encryption, and compression?
- A) Session
- B) Presentation
- C) Application
- D) Transport

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Presentation layer handles data format translation, encryption, and compression.

</details>

### 8. Which layer of the OSI model provides services to the user?
- A) Presentation
- B) Session
- C) Application
- D) Transport

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** The Application layer provides network services directly to user applications (HTTP, FTP, SMTP).

</details>

### 9. Which of the following is NOT a layer of the OSI model?
- A) Transport
- B) Internet
- C) Network
- D) Data Link

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** "Internet" is a layer in the TCP/IP model, not the OSI model.

</details>

### 10. How many layers are there in the TCP/IP model?
- A) 4
- B) 5
- C) 6
- D) 7

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The TCP/IP model has 4 layers: Network Access, Internet, Transport, and Application.

</details>

### 11. Which TCP/IP layer is equivalent to the OSI Physical and Data Link layers?
- A) Internet
- B) Transport
- C) Network Access
- D) Application

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** The Network Access layer combines OSI's Physical and Data Link layers.

</details>

### 12. Which TCP/IP layer is equivalent to the OSI Network layer?
- A) Internet
- B) Transport
- C) Network Access
- D) Application

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The Internet layer (IP) corresponds to the OSI Network layer.

</details>

### 13. Which TCP/IP layer is equivalent to the OSI Transport layer?
- A) Internet
- B) Transport
- C) Network Access
- D) Application

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Transport layer in TCP/IP corresponds directly to the OSI Transport layer.

</details>

### 14. Which TCP/IP layer combines OSI's Session, Presentation, and Application layers?
- A) Internet
- B) Transport
- C) Network Access
- D) Application

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** The TCP/IP Application layer combines the top three OSI layers.

</details>

### 15. Which protocol operates at the Transport layer?
- A) IP
- B) TCP
- C) HTTP
- D) Ethernet

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** TCP (Transmission Control Protocol) operates at the Transport layer.

</details>

### 16. Which protocol operates at the Internet/Network layer?
- A) TCP
- B) UDP
- C) IP
- D) FTP

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** IP (Internet Protocol) operates at the Network/Internet layer.

</details>

### 17. Which protocol operates at the Application layer?
- A) TCP
- B) IP
- C) HTTP
- D) ARP

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** HTTP (Hypertext Transfer Protocol) operates at the Application layer.

</details>

### 18. Which protocol operates at the Data Link layer?
- A) IP
- B) TCP
- C) Ethernet
- D) HTTP

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Ethernet operates at the Data Link and Physical layers.

</details>

### 19. What is the PDU (Protocol Data Unit) for the Transport layer?
- A) Frame
- B) Packet
- C) Segment
- D) Bit

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** The Transport layer PDU is called a segment (TCP) or datagram (UDP).

</details>

### 20. What is the PDU for the Network layer?
- A) Frame
- B) Packet
- C) Segment
- D) Bit

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Network layer PDU is called a packet.

</details>

### 21. What is the PDU for the Data Link layer?
- A) Frame
- B) Packet
- C) Segment
- D) Bit

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The Data Link layer PDU is called a frame.

</details>

### 22. What is the PDU for the Physical layer?
- A) Frame
- B) Packet
- C) Segment
- D) Bit

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** The Physical layer PDU is a bit.

</details>

### 23. Which layer adds a header and trailer to the data?
- A) Transport
- B) Network
- C) Data Link
- D) Physical

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** The Data Link layer adds both a header and a trailer (for error detection) to create a frame.

</details>

### 24. Encapsulation in networking refers to:
- A) Adding headers as data moves down the layers
- B) Removing headers as data moves up the layers
- C) Encrypting data
- D) Compressing data

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Encapsulation is the process of adding protocol headers at each layer as data moves down the stack.

</details>

### 25. De-encapsulation refers to:
- A) Adding headers
- B) Removing headers as data moves up the layers
- C) Encrypting data
- D) Compressing data

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** De-encapsulation removes headers as data moves up the layers at the receiving end.

</details>

### 26. Which layer is responsible for flow control?
- A) Physical
- B) Data Link
- C) Network
- D) Transport

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** The Transport layer handles flow control (and the Data Link layer also does it hop-by-hop).

</details>

### 27. Which layer is responsible for error detection and correction?
- A) Physical
- B) Data Link
- C) Network
- D) Transport

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Data Link layer handles error detection and correction for frames.

</details>

### 28. Which layer provides logical addressing?
- A) Physical
- B) Data Link
- C) Network
- D) Transport

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** The Network layer provides logical addressing (IP addresses).

</details>

### 29. Which layer provides physical addressing?
- A) Physical
- B) Data Link
- C) Network
- D) Transport

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Data Link layer uses MAC addresses for physical addressing.

</details>

### 30. Which of the following is a connection-oriented protocol?
- A) UDP
- B) TCP
- C) IP
- D) ICMP

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** TCP is connection-oriented (establishes a connection before data transfer). UDP is connectionless.

</details>

## Part B: IP Addressing & Subnetting (Questions 31-60)


### 31. What is the size of an IPv4 address?
- A) 16 bits
- B) 32 bits
- C) 64 bits
- D) 128 bits

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** IPv4 addresses are 32 bits long, written as four octets (e.g., 192.168.1.1).

</details>

### 32. What is the size of an IPv6 address?
- A) 32 bits
- B) 64 bits
- C) 128 bits
- D) 256 bits

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** IPv6 addresses are 128 bits long.

</details>

### 33. Which class of IPv4 address is used for multicast?
- A) Class A
- B) Class B
- C) Class C
- D) Class D

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Class D (224.0.0.0 to 239.255.255.255) is reserved for multicast.

</details>

### 34. Which class of IPv4 address is used for experimental purposes?
- A) Class A
- B) Class B
- C) Class C
- D) Class E

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Class E (240.0.0.0 to 255.255.255.255) is reserved for experimental use.

</details>

### 35. What is the default subnet mask for a Class A address?
- A) 255.0.0.0
- B) 255.255.0.0
- C) 255.255.255.0
- D) 255.255.255.255

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Class A default subnet mask is 255.0.0.0 (or /8).

</details>

### 36. What is the default subnet mask for a Class B address?
- A) 255.0.0.0
- B) 255.255.0.0
- C) 255.255.255.0
- D) 255.255.255.255

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Class B default subnet mask is 255.255.0.0 (or /16).

</details>

### 37. What is the default subnet mask for a Class C address?
- A) 255.0.0.0
- B) 255.255.0.0
- C) 255.255.255.0
- D) 255.255.255.255

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Class C default subnet mask is 255.255.255.0 (or /24).

</details>

### 38. Which of the following is a private IP address?
- A) 8.8.8.8
- B) 192.168.1.1
- C) 172.15.0.1
- D) 11.0.0.1

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** 192.168.0.0/16 is a private IP range. 8.8.8.8 is public DNS. 172.15.x.x is public; 172.16-31.x.x is private.

</details>

### 39. What is the loopback address in IPv4?
- A) 0.0.0.0
- B) 127.0.0.1
- C) 255.255.255.255
- D) 192.168.1.1

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** 127.0.0.1 (localhost) is the loopback address used for testing.

</details>

### 40. What is the broadcast address for a network?
- A) All 0s in host portion
- B) All 1s in host portion
- C) All 0s in network portion
- D) All 1s in network portion

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The broadcast address has all 1s in the host portion (e.g., 192.168.1.255 for /24).

</details>

### 41. How many bits are in each octet of an IPv4 address?
- A) 4
- B) 8
- C) 16
- D) 32

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Each octet is 8 bits (0-255).

</details>

### 42. What is the CIDR notation for a subnet mask of 255.255.255.0?
- A) /8
- B) /16
- C) /24
- D) /32

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** 255.255.255.0 has 24 network bits, so CIDR is /24.

</details>

### 43. What is the CIDR notation for a subnet mask of 255.255.0.0?
- A) /8
- B) /16
- C) /24
- D) /32

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** 255.255.0.0 has 16 network bits, so CIDR is /16.

</details>

### 44. How many usable hosts are in a /24 subnet?
- A) 254
- B) 256
- C) 255
- D) 128

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** 2^8 - 2 = 254 usable hosts (one for network, one for broadcast).

</details>

### 45. How many usable hosts are in a /16 subnet?
- A) 65534
- B) 65536
- C) 256
- D) 1024

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** 2^16 - 2 = 65534 usable hosts.

</details>

### 46. What is subnetting?
- A) Dividing a network into smaller subnetworks
- B) Combining networks
- C) Encrypting data
- D) Routing packets

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Subnetting divides a large network into smaller, manageable subnetworks.

</details>

### 47. What is supernetting?
- A) Dividing a network
- B) Combining multiple networks into a larger one
- C) Encrypting data
- D) Routing packets

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Supernetting (route aggregation) combines multiple smaller networks into a larger one.

</details>

### 48. Which protocol maps IP addresses to MAC addresses?
- A) DNS
- B) DHCP
- C) ARP
- D) RARP

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** ARP (Address Resolution Protocol) resolves IP addresses to MAC addresses.

</details>

### 49. Which protocol maps MAC addresses to IP addresses?
- A) DNS
- B) DHCP
- C) ARP
- D) RARP

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** RARP (Reverse ARP) resolves MAC addresses to IP addresses.

</details>

### 50. Which protocol automatically assigns IP addresses to hosts?
- A) DNS
- B) DHCP
- C) ARP
- D) RARP

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** DHCP (Dynamic Host Configuration Protocol) dynamically assigns IP addresses.

</details>

### 51. Which protocol translates domain names to IP addresses?
- A) DHCP
- B) DNS
- C) ARP
- D) FTP

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** DNS (Domain Name System) translates human-readable domain names to IP addresses.

</details>

### 52. What is the maximum value of an octet in IPv4?
- A) 127
- B) 255
- C) 256
- D) 1024

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** An 8-bit octet can range from 0 to 255.

</details>

### 53. Which of the following is a valid IPv4 address?
- A) 192.168.1.256
- B) 192.168.1.1
- C) 192.168.1
- D) 192.168.1.1.1

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** 192.168.1.1 is valid. 256 is out of range, and the others have incorrect format.

</details>

### 54. What is NAT?
- A) Network Address Translation
- B) Network Access Terminal
- C) Node Address Table
- D) Network Allocation Table

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** NAT translates private IP addresses to public IP addresses for internet access.

</details>

### 55. What is the main purpose of NAT?
- A) To conserve public IP addresses
- B) To speed up the network
- C) To encrypt data
- D) To route packets

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** NAT allows multiple devices to share a single public IP address, conserving IPv4 addresses.

</details>

### 56. Which of the following is a valid private IP range?
- A) 10.0.0.0/8
- B) 172.16.0.0/12
- C) 192.168.0.0/16
- D) All of the above

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** All three ranges are reserved for private networks.

</details>

### 57. What is the subnet mask for a /30 network?
- A) 255.255.255.0
- B) 255.255.255.252
- C) 255.255.255.248
- D) 255.255.255.240

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** /30 = 255.255.255.252, providing 2 usable hosts.

</details>

### 58. How many subnets can be created from a /24 network if we borrow 3 bits?
- A) 2
- B) 4
- C) 8
- D) 16

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** 2^3 = 8 subnets.

</details>

### 59. What is the network address of 192.168.10.100/24?
- A) 192.168.10.0
- B) 192.168.10.1
- C) 192.168.10.255
- D) 192.168.0.0

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The network address is obtained by ANDing the IP with the subnet mask: 192.168.10.0.

</details>

### 60. What is the broadcast address of 192.168.10.100/24?
- A) 192.168.10.0
- B) 192.168.10.1
- C) 192.168.10.255
- D) 192.168.255.255

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** The broadcast address has all 1s in the host portion: 192.168.10.255.

</details>

## Part C: Network Devices & Topologies (Questions 61-85)


### 61. Which device operates at the Physical layer?
- A) Hub
- B) Switch
- C) Router
- D) Bridge

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A hub is a multiport repeater that operates at the Physical layer.

</details>

### 62. Which device operates at the Data Link layer?
- A) Hub
- B) Switch
- C) Router
- D) Repeater

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A switch operates at the Data Link layer, using MAC addresses.

</details>

### 63. Which device operates at the Network layer?
- A) Hub
- B) Switch
- C) Router
- D) Bridge

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** A router operates at the Network layer, using IP addresses.

</details>

### 64. Which device connects two different networks?
- A) Hub
- B) Switch
- C) Router
- D) Repeater

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** A router connects different networks and routes packets between them.

</details>

### 65. Which device amplifies signals?
- A) Hub
- B) Switch
- C) Router
- D) Repeater

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** A repeater amplifies and regenerates signals to extend the network distance.

</details>

### 66. Which device connects two LANs of the same type?
- A) Hub
- B) Switch
- C) Bridge
- D) Router

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** A bridge connects two LAN segments at the Data Link layer.

</details>

### 67. Which topology has all devices connected to a central device?
- A) Bus
- B) Star
- C) Ring
- D) Mesh

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** In a star topology, all devices connect to a central hub or switch.

</details>

### 68. Which topology has all devices connected in a closed loop?
- A) Bus
- B) Star
- C) Ring
- D) Mesh

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** In a ring topology, data travels in one direction around the loop.

</details>

### 69. Which topology has all devices connected to a single backbone cable?
- A) Bus
- B) Star
- C) Ring
- D) Mesh

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** In a bus topology, all devices share a common backbone cable.

</details>

### 70. Which topology provides the highest redundancy?
- A) Bus
- B) Star
- C) Ring
- D) Mesh

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** In a full mesh topology, every device is connected to every other device, providing maximum redundancy.

</details>

### 71. Which topology is the most expensive to implement?
- A) Bus
- B) Star
- C) Ring
- D) Mesh

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Mesh requires the most cabling and ports, making it the most expensive.

</details>

### 72. Which topology is easiest to troubleshoot?
- A) Bus
- B) Star
- C) Ring
- D) Mesh

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** In a star topology, a faulty device or cable only affects that device, making troubleshooting easier.

</details>

### 73. What is a LAN?
- A) Local Area Network
- B) Long Area Network
- C) Large Area Network
- D) Logical Area Network

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** LAN (Local Area Network) covers a small geographic area like an office or building.

</details>

### 74. What is a WAN?
- A) Wide Area Network
- B) Wireless Area Network
- C) Wired Area Network
- D) Web Area Network

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** WAN (Wide Area Network) covers a large geographic area, connecting multiple LANs.

</details>

### 75. What is a MAN?
- A) Metropolitan Area Network
- B) Main Area Network
- C) Managed Area Network
- D) Multiple Area Network

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** MAN (Metropolitan Area Network) covers a city or metropolitan area.

</details>

### 76. What is a PAN?
- A) Personal Area Network
- B) Public Area Network
- C) Private Area Network
- D) Packet Area Network

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** PAN (Personal Area Network) is a small network for personal devices (e.g., Bluetooth).

</details>

### 77. Which cable is immune to electromagnetic interference?
- A) Twisted Pair
- B) Coaxial
- C) Fiber Optic
- D) STP

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Fiber optic cables use light, making them immune to EMI.

</details>

### 78. Which cable is the most commonly used in LANs?
- A) Coaxial
- B) Fiber Optic
- C) Twisted Pair (UTP)
- D) STP

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** UTP (Unshielded Twisted Pair) is the most common and cost-effective LAN cable.

</details>

### 79. What is the maximum speed of Cat 6 UTP cable?
- A) 100 Mbps
- B) 1 Gbps
- C) 10 Gbps
- D) 100 Gbps

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Cat 6 supports up to 10 Gbps for limited distances.

</details>

### 80. What is the maximum length of a UTP cable segment?
- A) 50 meters
- B) 100 meters
- C) 200 meters
- D) 500 meters

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** UTP cable segments are limited to 100 meters.

</details>

### 81. Which connector is used with UTP cable?
- A) BNC
- B) RJ-45
- C) ST
- D) SC

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** RJ-45 is the standard connector for UTP Ethernet cables.

</details>

### 82. Which connector is used with fiber optic cable?
- A) RJ-45
- B) BNC
- C) ST/SC
- D) USB

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** ST and SC are common fiber optic connectors.

</details>

### 83. What is a MAC address?
- A) A 32-bit logical address
- B) A 48-bit physical address
- C) A 64-bit address
- D) A 128-bit address

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A MAC address is a 48-bit hardware address burned into the NIC.

</details>

### 84. How many bits are in a MAC address?
- A) 32
- B) 48
- C) 64
- D) 128

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** MAC addresses are 48 bits (6 bytes).

</details>

### 85. What is the purpose of a NIC?
- A) To connect a device to a network
- B) To route packets
- C) To amplify signals
- D) To encrypt data

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A Network Interface Card (NIC) connects a device to a network.

</details>

## Part D: Protocols & Security (Questions 86-115)


### 86. What does TCP stand for?
- A) Transmission Control Protocol
- B) Transport Control Protocol
- C) Transfer Control Protocol
- D) Transmission Communication Protocol

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** TCP (Transmission Control Protocol) is a reliable, connection-oriented protocol.

</details>

### 87. What does UDP stand for?
- A) User Datagram Protocol
- B) Universal Datagram Protocol
- C) User Data Protocol
- D) Unified Datagram Protocol

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** UDP (User Datagram Protocol) is a connectionless, unreliable protocol.

</details>

### 88. Which protocol is faster: TCP or UDP?
- A) TCP
- B) UDP
- C) Both are equal
- D) Depends on the network

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** UDP is faster because it has no connection setup, acknowledgments, or flow control.

</details>

### 89. Which protocol is used for reliable file transfer?
- A) UDP
- B) TCP
- C) IP
- D) ICMP

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** TCP is used for reliable file transfer (e.g., FTP uses TCP).

</details>

### 90. Which protocol is used for video streaming?
- A) TCP
- B) UDP
- C) FTP
- D) SMTP

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** UDP is preferred for real-time streaming because it minimizes latency.

</details>

### 91. What is the port number for HTTP?
- A) 21
- B) 25
- C) 80
- D) 443

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** HTTP uses port 80.

</details>

### 92. What is the port number for HTTPS?
- A) 80
- B) 443
- C) 21
- D) 25

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** HTTPS uses port 443.

</details>

### 93. What is the port number for FTP?
- A) 21
- B) 25
- C) 80
- D) 110

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** FTP uses port 21 for control and port 20 for data.

</details>

### 94. What is the port number for SMTP?
- A) 21
- B) 25
- C) 80
- D) 110

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** SMTP (Simple Mail Transfer Protocol) uses port 25.

</details>

### 95. What is the port number for POP3?
- A) 25
- B) 110
- C) 143
- D) 443

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** POP3 (Post Office Protocol 3) uses port 110.

</details>

### 96. What is the port number for DNS?
- A) 53
- B) 80
- C) 443
- D) 21

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** DNS uses port 53.

</details>

### 97. Which protocol is used for sending emails?
- A) POP3
- B) IMAP
- C) SMTP
- D) FTP

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** SMTP is used for sending emails. POP3 and IMAP are for receiving.

</details>

### 98. Which protocol is used for receiving emails?
- A) SMTP
- B) POP3
- C) FTP
- D) HTTP

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** POP3 and IMAP are used for receiving emails.

</details>

### 99. What is a firewall?
- A) A security system that monitors and controls network traffic
- B) A type of router
- C) A network cable
- D) A protocol

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A firewall filters incoming and outgoing network traffic based on security rules.

</details>

### 100. What is a VPN?
- A) Virtual Private Network
- B) Virtual Public Network
- C) Very Private Network
- D) Verified Private Network

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A VPN creates a secure, encrypted tunnel over a public network.

</details>

### 101. What is encryption?
- A) Converting plaintext to ciphertext
- B) Converting ciphertext to plaintext
- C) Compressing data
- D) Deleting data

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Encryption converts readable data (plaintext) into unreadable data (ciphertext).

</details>

### 102. What is decryption?
- A) Converting plaintext to ciphertext
- B) Converting ciphertext to plaintext
- C) Compressing data
- D) Deleting data

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Decryption converts ciphertext back to plaintext.

</details>

### 103. Which of the following is a symmetric encryption algorithm?
- A) RSA
- B) AES
- C) Diffie-Hellman
- D) ECC

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** AES (Advanced Encryption Standard) is symmetric. RSA, Diffie-Hellman, and ECC are asymmetric.

</details>

### 104. Which of the following is an asymmetric encryption algorithm?
- A) DES
- B) AES
- C) RSA
- D) 3DES

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** RSA is an asymmetric (public-key) encryption algorithm.

</details>

### 105. What is a DoS attack?
- A) Denial of Service
- B) Data of Service
- C) Domain of Service
- D) Digital of Service

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A DoS attack floods a system with traffic to make it unavailable.

</details>

### 106. What is a DDoS attack?
- A) Distributed Denial of Service
- B) Direct Denial of Service
- C) Data Denial of Service
- D) Domain Denial of Service

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A DDoS attack uses multiple compromised systems to flood a target.

</details>

### 107. What is phishing?
- A) A fraudulent attempt to obtain sensitive information
- B) A type of firewall
- C) A network protocol
- D) A type of cable

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Phishing tricks users into revealing passwords or credit card numbers.

</details>

### 108. What is malware?
- A) Malicious software
- B) Management software
- C) Monitoring software
- D) Main software

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Malware is software designed to harm or exploit systems (viruses, worms, trojans).

</details>

### 109. What is a virus?
- A) A self-replicating program that attaches to files
- B) A standalone self-replicating program
- C) A hardware failure
- D) A network protocol

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A virus attaches itself to legitimate files and spreads when those files are executed.

</details>

### 110. What is a worm?
- A) A self-replicating program that spreads over networks
- B) A program that attaches to files
- C) A hardware failure
- D) A network protocol

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A worm is a standalone malware that replicates itself to spread to other computers.

</details>

### 111. What is a Trojan horse?
- A) Malware disguised as legitimate software
- B) A self-replicating program
- C) A network protocol
- D) A type of firewall

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A Trojan horse appears to be useful software but performs malicious activities.

</details>

### 112. What is ransomware?
- A) Malware that encrypts files and demands payment
- B) A type of firewall
- C) A network protocol
- D) A type of cable

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Ransomware locks or encrypts files and demands a ransom for their release.

</details>

### 113. What is a Man-in-the-Middle (MitM) attack?
- A) An attacker intercepts communication between two parties
- B) An attacker floods a network
- C) An attacker sends phishing emails
- D) An attacker installs a virus

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** In a MitM attack, the attacker secretly relays and possibly alters communication between two parties.

</details>

### 114. What is SSL/TLS used for?
- A) Secure communication over the internet
- B) Routing packets
- C) Assigning IP addresses
- D) Resolving domain names

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** SSL/TLS encrypts data between a client and server (HTTPS).

</details>

### 115. What is the purpose of a digital signature?
- A) To verify the authenticity and integrity of a message
- B) To encrypt the message
- C) To compress the message
- D) To route the message

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A digital signature verifies the sender's identity and ensures the message has not been altered.

</details>
