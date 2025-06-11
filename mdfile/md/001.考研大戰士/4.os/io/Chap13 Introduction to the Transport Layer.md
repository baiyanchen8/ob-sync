# Transport-layer services
## Process-to-process communication
![[Pasted image 20250611131251.png]]
- How to find process ? 
	- use port number
![[Pasted image 20250611131915.png]]![[Pasted image 20250611131928.png]]

|項目|說明|
|---|---|
|🎯 通訊的主體|在網路上通訊的是「行程對行程」（process-to-process），也就是兩個程式在彼此溝通，而不是主機對主機。|
|🧩 架構類型|**Client-Server 模式**（用戶端－伺服器模式）是目前最常見的實作方式。|
|🖥️ Server（伺服器）|提供資源或服務的端，例如網站、資料庫、API 等。通常是常駐、固定運作的一方。|
|💻 Client（用戶端）|發出請求的一方，例如瀏覽器、APP、終端機程式。通常是動態連線、使用者主動發起的。|
|🔁 通訊方向|通常是：Client 發送請求 → Server 處理並回應。|
### IAAA Ranges 
| 類型                                                     | 範圍                 | 說明                                                                     |
| ------------------------------------------------------ | ------------------ | ---------------------------------------------------------------------- |
| ✅ Well-known ports（通常Server’s port number）             | **0 \~ 1023**      | IANA 授權並控制，用於知名服務（像 HTTP、FTP、SSH）。伺服器端必須使用**固定的、通用的 port 號碼**才能讓用戶端找到。 |
| 📝 Registered ports                                    | **1024 \~ 49151**  | 雖然 IANA 不會控制，但開發者可以向 IANA**登記（註冊）**，避免跟別人重複使用。                         |
| 🔄 Dynamic / Private ports<br>（通常Client’s port number） | **49152 \~ 65535** | 不由 IANA 控管，也不能註冊，**由系統動態分配**。通常是 **用戶端臨時開出來的 port（ephemeral port）**。   |
### Socket Addresses
- Transport layer protocol needs two identifiers at each end
	- The IP addresses (from network layer) 
	- The port numbers
- Socket address
	- The combination of an IP address and a port number
## Encapsulation and De-capsulation(skip)

## Multiplexing and De-multiplexing
![[Pasted image 20250611155741.png]]

## Full-Duplex Communication 
- Full-duplex service
	- Data can flow in both directions
## Connectionless and Connection-Oriented Services
### Connectionless Services
- UDP提供的服務
- 資料傳送前沒有先建立連線
- 直接傳送封包
### Connection-Oriented Services
- TCP提供的服務
- 資料傳送前會先建立連線
- As shown in the next slide, need three phase
	- Connection establishment
	- Data transfer
	- Tear-down phases
![[Pasted image 20250611160053.png]]
![[Pasted image 20250611160049.png]]
![[Pasted image 20250611160122.png]]

# Transport-layer protocols
![[Pasted image 20250611160113.png]]