# Terminology and Acronyms

| [A](#a) | [B](#b) | [C](#c) | [D](#d) | [E](#e) | [F](#f) | [G](#g) | [H](#h) | [I](#i) | [L](#l) | [M](#m) | [N](#n) | [O](#o) | [P](#p) | [Q](#q) | [R](#r) | [S](#s) | [T](#t) | [U](#u) | [V](#v) | [W](#w) |

### A
* **AAC:** Advanced Audio Coding
  * An audio compression technique created by Apple
  * Similar to MP3
* **ACKs:** Acknowledgements
* **AES:** Advanced Encryption Standard
  * A popular block cipher
* **AH:** Authentication Header
  * one of two principal IPsec protocols
  * provides source authentication and data integrity but does not provide confidentiality
* **AIMD:** Additive-increase, Multiplicative-decrease
* **AON:** Active Optical Network
* **AP:** access point
  * the base station in a basic service set (BSS) within the 802.11 wireless LAN architecture
* **AQM algorithm:** Active Queue Management algorithm
  * algorithm for packet-dropping or marking
* **ARP:** Address Resolution Protocol
  * provides a mechanism to translate IP addresses to link layer addresses
* **ARQ protocols:**  Automatic Repeat reQuest protocols
  * ie acknowledgement/retransmission scheme
* **AS:** Autonomous System
  * Routers within the same AS all run the same routing algorithm and have information about each other
* **ASN:** Autonomous System Number
  * A globally unique number that identifies an AS

### B
* **BER:** Bit Error Rate
  * the probability that a transmitted bit is received in error at the receiver
* **BGP:** Border Gateway Protocol
  * the inter-AS routing protocol run by all ASs in the Internet
* **BGP connection**
  * The semi-permanent TCP connection between a pair of routers along with all the BGP messages sent over the connection
* **BIOS:** Basic Input/Output System
* **BSC:** Base Station Controller
  * A controller in a GSM network that will typically service several tens of base transceiver stations
* **BSS:** Block Started by Segment
* **BSS:** basic service set
  * Part of the 802.11 wireless LAN (WiFi) architecture
  * consists of one or more wireless stations and a central base station
* **BSS:** Base Station Subsystem
  * A base station controller along with its controlled base transceiver stations.
* **BTS:** Base Transceiver Station
  * A station within a cell of a cellular network that transmits signals to and receives signals from the mobile stations in its cell.

### C
* **CA:** Certification Authority
  * A body whose job is to validate identities and issue certificates
  * responsible for binding a public key to a particular entity
* **CBC:** Cipher Block Chaining
  * A block cipher technique
  * Uses an IV c(0) and then randomly permutes the ith block, m(i), with the (i-1)th encrypted block, c(i-1)
* **CDMA:** Code Division Multiple Access
  * A channel partitioning protocol
  * Assigns a different code to each node and each node sends data with its code
  * used to avoid collisions
* **CDN::** Content Distribution Network
* **channel propagation delay**
  * the end-to-end channel propagation delay of a broadcast channel is the time it takes for a signal to propagate from one of the nodes to another
* **CIDR:** Classless Interdomain Routing
  * The Internet's address assignment strategy
* **Clos Network:** A kind of multistage circuit-switching network
  * the network is parameterized by 3 integers: n, m, and r
    * n represents the number of sources
    * each of the n sources feed into each of r ingress stage crossbar switches
    * each ingress stage crossbar switch has m outlets and there are m middle stage crossbar switches
* **CMTS:** Cable Modem Termination System
* **COA:** Care-of Address
  * The address assigned to a mobile agent in a foreign network
* **COTS:** Components Off The Shelf
* **CRC:** Cyclic Redundancy Check
  * An error-detection technique used widely in today's computer networks
  * also known as polynomial codes
* **CRDTs:** Commutative Replicated Data Types
* **CSMA:** Carrier Sense Multiple Access
  * There is also CSMA/CA - CSMA with collision avoidance
    * used by 802.11 Wireless LANs (WiFi)
  * There is also CSMA/CD - CSMA with collision detection.
  * A link-layer random access protocol with two components:
    1. carrier sensing - a node listens to the channel before transmitting
    2. collision detection - a transmitting node listens to the channel while it is transmitting
* **CTS:** Clear to Send
  * Under the MAC protocol it is a control frame broadcast by the AP telling a device that it is clear to send data for the specified duration and telling all other frames not to send.
* **CWR:** Congestion Window Reduced

### D
* **DASH:** Dynamic Adaptive Streaming over HTTP
  * A type of streaming that uses multiple versions of the video, each compressed at a different rate
* **DCCP:** Datagram Congestion Control Protocol
* **DCTCP:** Data Center TCP
* **DDoS:** Distributed Denial of Service
* **DES:** Data Encryption Standard
  * A popular block cipher
* **DHCP:** Dynamic Host Configuration Protocol
  * allows a host to obtain (be allocated) an IP address automatically
* **DHT:** Distributed Hash Table
* **DIFS:** Distributed Inter-frame Space
  * Under the 802.11 wireless LANs (WiFi) protocol, if the station senses the channel idle, it transmits its frame after a short period of time known as the DIFS
* **DMZ:** Demilitarized Zone
 * lower security region within an organization
* **DNS:** Domain Name System
* **DOCSIS:** Data-Over-Cable Service Interface Specifications
  * specifies the cable data network architecture and its protocols
  * it is the link layer protocol for cable internet access
* **DoS:** Denial-of-Service
* **DPI:** Deep Packet Inspection
* **DSL:** Digital Subscriber Line
* **DSLAM:** Digital Subscriber Line Access Multiplexer
* **DV Algorithm:** Distance vector algorithm
  * A decentralized routing algorithm where each node maintains a vector of estimates of the costs to all other nodes in the network.

### E
* **EAP:** Extensible Authentication Protocol
  * defines the end-to-end message formats used in a simple request/response mode of interaction
* **eBGP:** external BGP
  * a BGP connection that spans two ASs
* **ECE:** Explicit Congestion Notification Echo
* **ECMP:** Equal-cost multi-path routing
  * A routing strategy where packet forwarding to a single destination can occur over multiple best paths with equal routing priority.
* **ECN:** Explicit Congestion Notification
* **EMS:** Encrypted Master Secret
  * The Master Secret for an SSL session that has been encrypted with the public key
* **EPC:** Enhanced Packet Core
  * In 4G, UE datagrams are encapsulated at the eNodeB and tunneled to the P-GW through the 4G network's all IP EPC
* **ESP:** Encapsulation Security Payload
  * One of two principal IPsec protocols
  * Provides source authentication, data integrity, and confidentiality

### F
* **FCT:** Flow Completion Time
* **FDM:** Frequency-Division Multiplexing
  * Technique used to partition a broadcast channel's bandwidth among all nodes sharing that channel based on frequency
  * if the channel has a rate of R bits per second (bps) and there are N nodes then the channel is divided into N channels, each with a rate of R/N bps
* **FEC:** Forward Error Correction
  * The ability of the receiver to both detect and correct errors
  * A loss anticipation scheme
  * Used in VoIP to deal with packet loss
  * Adds redundant information to the original packet, which can be used to reconstruct approximations or exact versions of some of the lost packets
* **FHSS:** Frequency Hopping Spread Spectrum
  * Used in IEEE 802.15.1 (Bluetooth)
  * Bluetooth operates in a TDM manner
  * During each time slot, a sender transmits on one of 79 channels, with the channel changing in a known but pseudo-random manner from slot to slot
* **FiOS:** Fiber Optic Service
* **FSM:** Finite State Machine
* **FTP:** File Transfer Protocol
  * a protocol that provides for the transfer of files between two end systems
* **FTTH:** Fiber to the Home

### G
* **GBN:** Go-Back-N
* **GGSN:** Gateway GPRS Support Node
  * acts as a gateway, connecting multiple SGSNs into the larger Internet
* **GMSC:** Gateway Mobile services Switching Center
  * a switch in the home network which helps route the caller from the home network to the visited network
* **GPRS:** General Packet Radio Service
  * An early cellular data service in 2G networks
* **GRAM:** Grid Resource Allocation Manager
* **GSI:** Grid Security Infrastructure
* **GSM:** Global System for Mobile communications

### H
* **HaaS:** Hardware as a Service
* **HDLC:** high-level data link control
  * A link-layer protocol for point-to-point links
* **HFC:** Hybrid Fiber Coaxial Cable
* **HLR:** Home Location Register
  * A database containing the permanent cell phone number and subscriber profile information
  * the home PLMN maintains this database with a record for each of its subscribers
* **HOL blocking:** Head-of-the-line blocking
* **home PLMN:** home public land mobile network
  * A mobile user's home network in GLM
* **HPC:** High Performance Computing
* **HSS:** Home Subscriber Service
  * Part of a 4G network
  * it contains UE information including roaming capabilities, quality of service profiles, and authentication information
* **HTTP:** HyperText Transfer Protocol
  * a protocol that provides for Web document request and transfer

### I
* **IaaS:** Infrastructure as a Service
* **iBGP:** internal BGP
  * a BGP connection between routers in the same AS
* **ICANN:** Internet Corporation for Assigned Names and Numbers
  * manages IP addresses
* **ICMP:** Internet Control Message Protocol
  * used by hosts and routers to communicate network-layer information to each other
* **IDS:** Intrusion Detection System
  * A device that generates alerts when it observes potentially malicious traffic
* **IETF:** Internet Engineering Task Force
* **IKE:** Internet Key Exchange
  * A protocol acting like an automated mechanism for creating SA information
* **IMAP:** Internet Mail Access Protocol
* **IP:** Internet Protocol
* **IPS:** Intrusion Prevention System
  * A device that filters out suspicious traffic
* **IPsec:** IP Security Protocol
  * provides security at the network layer
  * secures IP datagrams between any two network entities, including hosts and routers
* **ISP:** Internet Service Provider
* **IXP:** Internet Exchange Point

### L
* **L1d:** Level 1 Cache - data
* **L1i:** Level 1 Cache - instruction
* **LAN:** Local Area Network
* **LEO:** Low Earth Orbiting
* **LS Algorithms:** Link-State Algorithms
  * Algorithms with global state information about the network
* **LTE:** Long Term Evolution

### M
* **MAC:** Medium Access Control
  * A MAC protocol specifies the rules by which a frame is transmitted onto the link
* **MAC:** Message Authentication Code
  * Two parties have a shared secret `s` and hash function `H`
  * If Alice wants to send message `m` to Bob she calculates `H(m + s)` as the MAC
* **MAN:** Metropolitan Area Network
* **MANET:** Mobile ad hoc networks
  * A type of multi-hop, infrastructure-less network where nodes are mobile with connectivity changing among nodes.
* **MDC:** Modular data center
  * A factory builds, within a standard 12-meter shipping container, a mini data center and ships the container to the data center location.
* **MIB:** Management Information Base
  * The collected information of a managed object within a managed device
* **MIMO:** Multiple input multiple output
* **MIPS:** Microprocessor without Interlocked Pipeline Stages
* **MME:** Mobility Management Entity
  * In a 4G network it performs connection and mobility management on behalf of the UEs resident in the cell it controls
* **MMU:** Memory Management Unit
* **MPLS:** Multiprotocol Label Switching
  * a packet-switched, virtual-circuit network
* **MPP:** Massively Parallel Processing
* **MS:** Master Secret
  * The secret key used for a single SSL session
* **MSC:** Mobile Switching Center
  * Plays the central role in user authorization and accounting, call establishment and teardown, and handoff in a cellular network.
* **MSRN:** Mobile Station Roaming Number
  * A roaming number that is temporarily assigned to a mobile when it enters a visited network.
* **MSS:** Maximum Segment Size
* **MTTF:** Mean Time to Failure
* **MTU:** Maximum Transmission Unit
  * The maximum amount of data that a link layer frame can carry

### N
* **NAKs:** Negative Acknowledgements
* **NAT:** Network Address Translation
  * The process of translating IPs in a LAN to IPs to be used in the broader internet
* **NCP:** Network Control Protocol
* **NFS:** Network File System
* **NFV:** Network Functions Virtualization
  * a generalization of SDN aimed at disruptive replacement of sophisticated middleboxes with simple commodity servers, switching, and storage.
* **NIC:** Network Interface Card
  * A network adapter on which the link layer is implemented.
* **NOC:** Network Operations Center
* **NTP:** Network Time Protocol

### O
* **OC:** Optical Carrier
* **OFDM:** Orthogonal Frequency Division Multiplexing
  * Used in 4G LTE on the downstream channel
  * A combination of frequency division multiplexing and time division multiplexing
* **OLT:** Optical Line Terminator
* **ONT:** Optical Network Terminator
* **OS:** Operating System
* **OSI:** Open Systems Interconnection
* **OSPF:** Open Shortest Path First
  * widely used for intra-AS routing in the internet
  * a link-state protocol that uses flooding of link-state information and a Dijkstra's least-cost path algorithm

### P
* **P2P:** Peer-to-Peer
* **PaaS:** Platform as a Service
* **PBS:** Portable Batch System
* **PCM:** Pulse Code Modulation
  * Encoding technique for converting an audio signal to a digital signal
* **PGP:** Pretty Good Privacy
  * Provides secure email
  * one of the first security technologies to be broadly used in the Internet
* **P-GW:** Packet Data Network Gateway
  * Part of a 4G network
  * allocates IP addresses to the UEs and performs QoS enforcement
* **PHB:** Per-hop behaviour
* **PKI:** Public Key Infrastructure
* **PMS:** Pre-Master Secret
* **PON:** Passive Optical Network
* **PoP:** Point of Presence
* **POP3:** Post Office Protocol - Version 3
* **POST:** Power-on Self Test
* **PPP:** Point-to-Point Protocol
  * A link layer protocol for point-to-point communication

### Q
* **QoS:** Quality of Service

### R
* **RAII:** Resource Acquisition is Initialization
* **RAM:** Random Access Memory
* **RED:** Random Early Detection
  * An AQM algorithm
* **RFC:** Request for Comments
* **RLS:** Replica Location Service
* **RMTP:** Reliable Multicast Transport Protocol
* **RNC:** Radio Network Controller
  * In a 3G radio access network it typically controls several base transceiver stations
* **ROM:** Read Only Memory
* **RTO:** Retransmission Timeout
* **RTP:** Real-Time Transport Protocol
  * A protocol used for video where the server encapsulates video chunks within transport packets specially designed for transporting audio and video
  * Typically runs on top of UDP
* **RTS:** Request to Send
  * Under the 802.11 MAC protocol it is a request by a host to send data to the AP
* **RTSP:** Real-Time Streaming Protocol
  * A protocol for the control connection maintained in UDP streaming over which the client sends commands regarding session state changes (ie pause, resume, reposition, etc)
* **RTT:** Round Trip Time
* **RVO:** Return Value Optimization

### S
* **SA:** Security Association
  * Before sending IPsec datagrams from source entity to destination entity, the source and destination entities create a network-layer logical connection
  * unidirectional, if you want data flowing back and forth you need two SAs.
* **SAD:** Security Associate Database
  * data structure in an IPsec entity's OS kernel
  * stores the state information for all of its SAs
* **SaaS:** Software as a Service
* **SDN:** Software Defined Network
* **SGSN:** Serving GPRS Support Node
  * responsible for delivering datagrams to/from the mobile nodes in the radio access network to which it is attached.
* **S-GW:** Serving Gateway
  * the data-plane mobility anchor point in a 4G network
  * all UE traffic will pass through the S-GW
* **SHA-1:** Secure Hash Algorithm
  * A major hash algorithm in use today
  * Produces a 160-bit message
* **SIFS:** Short Inter-frame Spacing
  * The short period of time between when a destination receives a frame that passes the CRC and when it sends back an acknowledgement frame
  * Under 802.11 wireless LANs (WiFi) protocol
* **SIP:** Session Initiation Protocol
  * An open and lightweight protocol for real-time conversational applications (ie VoIP)
  * Provides mechanisms for establishing calls between a caller and a callee over an IP network
  * Provides mechanisms for the caller to determine the current IP address of the callee
  * Provides mechanisms for call management
  * SIP messages can be sent over UDP or TCP
* **SMTP:** Simple Mail Transfer Protocol
  * A protocol that provides for the transfer of email messages.
* **SNMP:** Simple Network Management Protocol
  * An application-layer protocol used to convey network-management control and information messages between a managing server and an agent executing on behalf of the managing server
* **SNR:** Signal-to-Noise Ratio
  * A relative measure of the strength of the received signal (ie the information being transmitted) and the noise introduced during transmission.
* **SOA:** Service Oriented Architecture
* **SPD:** Security Policy Database
  * a database in an IPsec entity
  * indicates what type of datagrams are to be IPsec processed; and for those that are to be IPsec processed, which SA should be used.
* **SPI:** Security Parameter Index
  * A 32-bit identifier for the SA
* **SPoF:** Single Point of Failure
* **SR:** Selective Repeat
* **SRM:** Scalable Reliable Multicast
* **SSD:** Solid State Disk
* **SSID:** Service Set Identifier
  * the one or two words assigned to an AP when it is installed
  * (ie the nice name that comes up on your phone when you try to connect to different WiFi APs)
* **SSL:** Secure Sockets Layer
  * An enhanced version of TCP with security services including confidentiality, data-integrity, and end point authentication
* **SSRC:** Synchronization Source Identifier
  * A 32-bit field identifying the source of an RTP stream
* **SSTable:** Stored String Table
* **SWIM:** Scalable Weakly-consistent Infection-style Membership

### T
* **TCAM:** Ternary Content Addressable Memory
* **TCP:** Transmission Control Protocol
* **TDM:** Time-Division Multiplexing
 * Technique used to partition a broadcast channel's bandwidth among all nodes sharing that channel based on time
 * time is divided into frames and if there are N nodes then a frame has N slots
 * each node can send a packet in its allocated slot
* **TLS:** Transport Layer Security
  * A slightly modified version of SSL version 3
  * has been standardized
* **TOR switch:** Top of Rack Switch
  * The switch at the top of each rack in a data center
  * it interconnects hosts in the rack with each other and with other switches in the data center.
* **TOS:** Type of Service
* **TTL:** Time to Live

### U
* **UDP:** User Datagram Protocol
* **UE:** User Equipment
  * A wireless device in a 4G network
* **UMTS:** Universal Mobile Telecommunications Service
* **UPS systems: Uninterruptable power supplies systems
* **UTP:** Unshielded Twisted Pair

### V
* **VANET:** Vehicular ad hoc network
  * A mobile ad hoc network (MANET) where the mobile nodes are vehicles
* **VLAN:** Virtual Local Area Network
  * a switch that supports VLANs allows multiple virtual local area networks to be defined over a single physical local area network Infrastructure.
* **VLR:** Visitor Location Register
  * a database maintained by the visited network
  * contains an entry for each mobile user that is currently in the portion of the network served by the VLR
* **VoIP:** Voice-over-IP
  * Real-time conversational voice over the Internet
* **VPN:** Virtual Private Network
  * An institution's data is sent over the public Internet
  * But the institution's data is encrypted before it enters the public Internet

### W
* **WAN:** Wide Area Network
* **WEP:** Wired Equivalent Privacy
  * Security mechanisms initially standardized in the 802.11 (WiFi) specification
  * Meant to provide a level of security similar to that found in wired networks
  * 802.11i standard is more secure
* **WiMAX:** World Interoperability for Microwave Access
  * An additional 4G wireless technology
  * A family of IEEE 802.16 standards that differ significantly from LTE
* **WPAN:** Wireless Personal Area Network
