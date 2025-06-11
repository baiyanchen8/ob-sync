# Protocol layers
## Protocols
- A protocol is needed when two entities(實體) need to commu.

## 1 layer commu v.s. 3 layer commu
![[Pasted image 20250527103156.png]]
![[Pasted image 20250527103146.png]]

# The OSI model
OSI 模型（**Open Systems Interconnection Model，開放式系統互連模型**）是由 ISO（國際標準化組織）制定的一個網路通訊架構，目的是讓不同系統或設備之間能夠透過統一的標準進行資料傳輸與溝通。這個模型總共有 **7 層**，每一層都負責不同的功能，從應用程式到實體媒介，層層遞交資料。

![[Pasted image 20250527103227.png]]

---
- Single machine
	- Each layer calls upon the services of the layer just below it
	- 每一層只未上一層提供服務，並享用下一層的服務
- Between machines
	- Layer x on one machine communicates with layer x on another machine
	- This communication is governed by protocols

| 層級  | 名稱（英文）             | 功能簡介（台灣說法）                                                                                                             |
| --- | ------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| 7   | Application Layer  | 應用層，像是網頁瀏覽器、email、FTP 這類應用                                                                                             |
| 6   | Presentation Layer | 表示層，負責資料格式轉換（例如編碼、解碼、加密、解密）                                                                                            |
| 5   | Session Layer      | 工作階段層，建立、管理與結束通訊會話                                                                                                     |
| 4   | Transport Layer    | 傳輸層，像 TCP、UDP，保證資料完整性與順序                                                                                               |
| 3   | Network Layer      | 網路層，負責 IP 定位與路由選擇（像 IP 位址、Router）                                                                                      |
| 2   | Data Link Layer    | 資料連結層，處理 MAC 位址、錯誤檢測<br>**Trailer（後面）**：最常見的就是 **FCS（Frame Check Sequence）**，用來檢查傳輸過程中有沒有資料毀損。<br>通常在第二層加入 **Trailer** |
| 1   | Physical Layer     | 實體層，網路線、電壓訊號、無線電波等物理傳輸方式                                                                                               |

## Physical layer
![[Pasted image 20250527144015.png]]

| 功能項目                    | 中文解釋             | 舉例說明                                |
| ----------------------- | ---------------- | ----------------------------------- |
| Representation of bits  | 位元轉訊號的方式（編碼方式）   | 電壓高低、光強弱、相位變化等                      |
| Data rate               | 每秒傳輸位元的數量（速度）    | 100 Mbps 網路                         |
| Synchronization of bits | 送收端資料對齊的方式（同步機制） | Manchester Encoding、start/stop bits |
### 物理層的溝通模式 #Duplex

| 模式          | 中文名稱  | 資料傳輸方式     | 常見範例       |     |
| ----------- | ----- | ---------- | ---------- | --- |
| Simplex     | 單工模式  | 單向傳輸       | 電視廣播、滑鼠輸入  |     |
| Half-Duplex | 半雙工模式 | 雙向但一次只能一邊傳 | 對講機、老式網路設備 |     |
| Full-Duplex | 全雙工模式 | 雙向且可同時傳輸   | 手機、現代乙太網路  |     |

>[!Question]
>![[Pasted image 20250527145514.png]]
>Ans: The physical layer is responsible for sending/receiving individual bits.

### Data Link Layer
> [!Question] 我們想將資料從file serve送到user station, 在physical layer的基礎上, 我們需要另外提供什麼服務呢?
>The data link layer is responsible for sending/receiving frames from one node to another node in the same network.
>資料鏈結層負責在同一網路內從一個節點傳送/接收訊框到另一個節點。

| 功能名稱                | 中文解釋            | 補充說明               |
| ------------------- | --------------- | ------------------ |
| Physical Addressing | 實體位址（MAC 位址）    | 區域網路內用來辨識裝置        |
| Access Control      | 控制誰可以傳資料        | 預防碰撞、掌控媒介          |
| Framing             | 把資料打包成一個個 Frame | 含標頭與尾端             |
| Error Control       | 檢查資料有無損壞與重傳機制   | 通常用 CRC 與 ACK/NACK |
## Network Layer

$\Huge{\textcolor{red}{實現跨網路的封包傳送/接收}}$
>[!question] Question: 欲實現跨網路的封包傳遞與接收需要解決什麼問題?

| 問題類型     | 說明                 |
| -------- | ------------------ |
| 封裝格式不同   | 不同網路的 frame 結構無法通用 |
| 協定不一致    | 例如 IPv4 與 IPv6 要互通 |
| IP 位址不連通 | 要透過路由找路徑、或做 NAT    |
| 傳輸速率不一   | 封包可能需暫存、分段         |
| MTU 限制不同 | 封包可能需被分段重組         |
| 多網路轉送需求  | 要有路由表與路由器協助        |
### 🧠 結論：

> 欲實現跨網路的資料傳輸，必須仰賴「**網路層（如 IP 協定）**」來提供統一格式、尋找路徑，  
> 並透過「**閘道器（gateway）**」來轉換不同網路之間的封包格式與協定，才能讓資料順利送達不同網段中的設備。

### ❓**為什麼需要 Logical Addressing？**

---

### ✅ 1. **Physical Addressing 是「區域性」的位址系統**

- 實體位址（像 MAC address）只在「**同一個網路（LAN）**」裡有效
    
- 例如兩台電腦連在同一個 switch，它們靠 MAC 位址就可以互相通訊
    
- 但只要封包要跨到別的網路（例如跨 router），**MAC 位址就不適用**
    

---

### ✅ 2. **跨網路傳輸需要「邏輯位址」**

- 一旦封包要離開原本的網段（例如要從 192.168.x.x 傳到 140.112.x.x），就不能再靠 MAC 了
    
- 所以我們需要一個「**全球唯一、有階層結構的位址**」來辨識主機在哪裡  
    ➡️ 這就是 **IP 位址（Logical Addressing）**
    

---

### 🧠 總結一下：

| 位址類型   | 作用範圍      | 是否能跨網路 | 範例                             |
| ------ | --------- | ------ | ------------------------------ |
| MAC 位址 | 區域網路（LAN） | ❌ 不能   | `00:1A:2B:3C:4D:5E`            |
| IP 位址  | 全球網際網路    | ✅ 可以   | `192.168.1.1`、`140.112.123.45` |

---

### ❓**為什麼需要 Routing（路由）？**

---

### ✅ 原因：**IP 封包只知道目的地 IP，但不知道怎麼走過去**

- 想像你有一封信要寄到「台北市中正區忠孝西路一段 100 號」  
    ➡️ 你知道地址，但你不知道哪條路、哪個郵局負責幫你送到那裡
- 網路世界也是一樣，**路由器（Router）就像郵局一樣**
    - 根據「目的 IP」來判斷下一跳（next hop）     
    - 再一步步幫你把封包轉送出去

### Node-to-Node (Hop-to-Hop) Delivery v.s. Host-to-Host Delivery

| 比較項目 | Node-to-Node Delivery | Host-to-Host Delivery |
| ---- | --------------------- | --------------------- |
| 傳遞層級 | 資料連結層（Layer 2）        | 網路層（Layer 3）          |
| 傳遞對象 | 相鄰節點（下一跳）             | 起點主機 → 終點主機           |
| 位址類型 | MAC 位址（實體）            | IP 位址（邏輯）             |
| 傳遞範圍 | 同一網路內                 | 跨多個網路                 |
| 重點用途 | 點對點傳送                 | 源到目的地資料送達             |
| 範例   | 電腦 ↔ 路由器              | 家裡電腦 ↔ Google Server  |
## Transport layer
reliable process-to-process message **delivery**
✅ 負責 **Process-to-Process（程式對程式）之間的完整資料傳遞**  
✅ 不只是把封包送到目的地主機，而是送到主機上「正確的應用程式（例如：瀏覽器、郵件伺服器）」

|控制功能|說明|解決問題|
|---|---|---|
|Error Control|確保資料正確送達，可重傳錯誤資料|錯誤/遺失封包|
|Flow Control|控制傳送速率，避免接收端爆掉|接收端超載|
|Congestion Control|根據網路情況調整速度，防止整體壅塞|網路擁擠、掉包|
# TCP /IP protocol suite

1. TCP/IP 協定套件是在 OSI 模型之前就已經開發出來。
2. 最初的 TCP/IP 協定是建立在硬體之上的四層軟體結構。
3. 現在我們通常把 TCP/IP 看作是五層模型：**實體層、資料鏈結層、網路層、傳輸層、應用層**。
 ![[Pasted image 20250529050918.png]]

在 TCP/IP 協定架構裡，**應用層不只等同於 OSI 模型的「應用層」而已**，它其實還包含了：
1. **應用層（Application Layer）**
2. **表示層（Presentation Layer）**
3. **會議層（Session Layer）**
也就是說，TCP/IP 的「應用層」是一個**整合了 OSI 模型最上面三層功能的集合**，包括資料格式的轉換（像是編碼/解碼）、資料加密/解密、建立與管理應用端的溝通階段等。

**定義：Link（連結）**  
在網路中，「連結」是指連接兩個或多個裝置，使它們能夠彼此通訊的**實體或邏輯媒介**。
一個「連結」可以是：
- **區域網路（LAN，Local Area Network）**：例如辦公室、學校內部的網路
- **廣域網路（WAN，Wide Area Network）**：例如跨城市或跨國的網路（像是電信公司提供的骨幹網）
這些不同的連結之間，會透過稱為 **路由器（router）** 或 **交換器（switch）** 的設備來互相連接。

## Physical Layer
**TCP/IP 並沒有定義任何特定的實體層協定**（參見下一張投影片）  
在這個層級中，**通訊的基本單位是一個 bit（位元）**。
![[Pasted image 20250529162433.png]]
## Data Link Layers
- TCP/IP does not define any specific protocol
- The unit of communication is a packet called a frame
## Network Layer
1. 應用層（Application Layer）
2. 表示層（Presentation Layer）
3. 會議層（Session Layer）
### 📚 網路層（Network Layer）介紹 - TCP/IP 架構中的第三層

#### ✅ 主要功能：
網路層的主要任務是**實現資料封包在不同網路之間的傳送與路由選擇**，它負責從來源主機將封包轉送到目的主機，**即使這兩台主機不在同一個區域網路上**也沒問題。
#### 📦 資料單位：
- 網路層處理的資料單位稱為 **「封包（Packet）」**
#### 🌐 關鍵任務：
1. **邏輯位址指派與處理**
    - 使用 **IP 位址（Internet Protocol Address）** 作為裝置在網路中的邏輯識別
2. **路由選擇（Routing）**
    - 根據目的地 IP 位址，選擇合適的路徑將封包從來源送往目的地
3. **分割與重組（Fragmentation/Reassembly）**
    - 若封包太大超過底層網路的傳輸限制（MTU），會進行切割與重組
#### 🔧 代表性協定：
- **IPv4 / IPv6**：負責 IP 位址編址與封包轉送
- **ICMP（Internet Control Message Protocol）**：提供錯誤回報與診斷（例如 ping）
- **IGMP（Internet Group Management Protocol）**：管理多播群組
#### 📍 注意事項：
- 網路層不保證封包的可靠傳送（例如：封包可能會遺失、延遲或順序錯亂）
- 封包傳送的可靠性由上層的「**傳輸層（Transport Layer）**」來處理（像是 TCP）
- datagram 
	- 指的是 packet header 中的包含 Source IP 、Target IP 、TTL(Time to live)等資訊的部份稱為 Datagram
![[Pasted image 20250530000421.png]]

> [!question] Why intermediate nodes need Layers 1, 2 and 3?
---
> [!answer] Layer 1 &2 : 負責傳輸 （Node-to-node）; Layer 3 : Routing（Where A to B）


## Transport Layer
- difference between Network & transport 
	- 只有最前＆最後兩個節點需要 Tramsport layer,而 Network 全都需要。
- Deliver the whole message, which is called a segment, a user datagram, or a packet, from A to B
- a segment may slice into rens of IP datagrams
![[Pasted image 20250530003235.png]]
- Three transport layer protocols
	- UDP (User Datagram Protocol)
	- TCP (Transmission Control Protocol)
	- SCTP (Stream Control Transmission Protocol)
- Many protocols are defined in this layer
	- DHCP,DNS, TELNET, SSH, FTP, TFTP, HTTP, SMTP, POP, IMAP, MIME, SNMP

| 層級（Layer）                  | 封包名稱（Packet Name）                              | 說明                                                   |
| -------------------------- | ---------------------------------------------- | ---------------------------------------------------- |
| **資料鏈結層（Data Link Layer）** | 🔹 **Frame（幀）**                                | 封包在實體網路中傳送的單位，包含 MAC 位址與錯誤檢查資訊（如 FCS）。例如以太網路的 frame。 |
| **網路層（Network Layer）**     | 🔹 **Datagram（資料報）**                           | IP 封包。包含來源與目的地的 IP 位址，用來實現不同網路間的路由與傳遞。               |
| **傳輸層（Transport Layer）**   | **User datagram ** **segment**  <br>**packet** | 用來實現主機之間的可靠或不可靠資料傳送。包含 port、序號、檢查碼等控制資訊。             |
![[Pasted image 20250530003701.png]]