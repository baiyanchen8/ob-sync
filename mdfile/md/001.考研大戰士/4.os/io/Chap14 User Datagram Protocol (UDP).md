# Introduction
![[Pasted image 20250611160333.png]]
- A transport layer protocol has two responsibilities
	- Create a process-to-process communications

- Provide control mechanism, e.g., flow control, error control, and congestion control
	- UDP does this task at a very minimal level
	- It only provides very limited error control, i.e., checksum
- UDP is a connectionless, unreliable transport protocol
	- Only add process-to-process communication to the IP
	- And perform checksum
- Advantages
	- UDP is very simple protocol with a minimum of overhead
![[Pasted image 20250611190002.png]]
# User datagram
- UDP packets: called user datagrams
	- The header fields are 
	- Source port number: 16-bits
	- Destination port number: 16-bits
	- Total Length: 16 bits:
		- Header plus data of the user datagram
	- Checksum: 16 bits
		- Detect errors over the entire user datagram (header plus data)

# UDP Services
- UDP Service: services provided by UDP to the applications in upper layer, i.e., application layer
	- Process-to-Process Communication
	- Connectionless Services
	- Error Control
	- Encapsulation and De-capsulation
	- Full-Duplex Communication
	- Multiplexing and De-mutiplexing
## Process-to-Process Communication
![[Pasted image 20250611212600.png]]

## Connectionless Services
- No connection establishment and no connection termination

- Each user datagram is an **independent** datagram
	- Even coming from the same source process and send to the same process
## Error Control
- No error control except for the checksum
	- Message may be lost, out-of-order or duplicated
## Encapsulation and De-capsulation
![[Pasted image 20250611212932.png]]

## Full-Duplex Communication
![[Pasted image 20250611213001.png]]
## Multiplexing and De-mutiplexing(skip!)


# UDP Applications
| 應用類型                       | 為什麼用 UDP？                                         |
| -------------------------- | ------------------------------------------------- |
| 📩 **簡單請求－回應的通訊**          | 不需要建立連線、不需要確認封包、速度快。例如 DNS 查詢、SNMP。               |
| 🧾 **內部已經有錯誤/流量控制的應用**     | 應用程式自己就會處理錯誤與流控，不需要依賴 TCP。例如：TFTP（簡易檔案傳輸協定）。      |
| 📡 **多點傳送（Multicasting）**  | TCP 不支援多點傳送，而 UDP 可以配合 IP Multicast 傳送同一資料給多個接收端。 |
| ⏱️ **即時應用（Real-time App）** | 即時音訊、視訊（如 VoIP、視訊串流）更重視「延遲低」而非「資料完整」，UDP 更適合。     |
| 🎮 **即時遊戲或互動式應用**          | 遊戲中掉一兩個封包沒差，但延遲太高會讓體驗變差，因此使用 UDP（如 FPS 遊戲）。       |