# Introduction
![[Pasted image 20250603102729.png]]
> [!bug] IP provides unreliable services
> - drawsback
> 	- 缺乏錯誤控制機制 
> 	- 缺乏協助機制
> - solution : ICMP
> 	- A network layer protocol
> 	- However, its message are not passed directly to the data link layer
> 	- The message are first encapsulated inside IP datagram
> 	- 該訊息首先封裝在 IP 資料封包中

![[Pasted image 20250603104541.png]]

# Message
- ICMP messages are divided into
	- Error-reporting message
		- Report problems that a router or a host (destination) may encounter
	- Query message
		- To get specific information
![[Pasted image 20250603105510.png]]

![[Pasted image 20250603105850.png]]

![[Pasted image 20250603105855.png]]

| 欄位名稱               | 長度      | 說明                                                                           |
| ------------------ | ------- | ---------------------------------------------------------------------------- |
| **Type**           | 1 byte  | 指定是哪種 ICMP 訊息（例如：Type 8 表示 Echo Request）                                     |
| **Code**           | 1 byte  | 指定這種類型下的更細部原因（例如：Type 3 是 Destination Unreachable，Code 0 表示 Net unreachable） |
| **Checksum**       | 2 bytes | 用來檢查 ICMP 訊息是否損壞                                                             |
| **Rest of Header** | 4 bytes | 視訊息種類而定，會有不同用途，例如識別碼與序號（ping 用）、封包資訊（錯誤用）等                                   |
## Error Reporting Messages
- ICMP only report error
	- Does not correct error
	- Error correction is left to the higher-level protocol

> [!question] Question: 封包在傳送中出錯了(例如Router丟棄 ), 誰產生ICMP的Message?送給誰呢?
>  -  將封包丟棄的Router或是Host產生,
>  - 送給原本的Source

>[!question] Question: 你覺得需要那些Error-reporting messages?
>![[Pasted image 20250603111917.png]]


### Destination Unreachable(type3)
- 當路由器無法路由資料封包或目標主機無法遞送資料封包時
	- 丟棄數據報Destination Unreachable
	- 路由器或主機將目標不可達訊息傳送回來源主機

| Code | 意義                                                           | 原因/情況                           | 由誰產生  |
| ---- | ------------------------------------------------------------ | ------------------------------- | ----- |
| 0    | **網路無法抵達（Network unreachable）**                              | 網路存在但暫時無法到達（可能是硬體故障）            | 路由器   |
| 1    | **主機無法抵達（Host unreachable）**                                 | 主機存在但暫時無法連線（可能是網卡壞了）            | 路由器   |
| 2    | **協定無法抵達（Protocol unreachable）**                             | 傳送到目的主機後，上層協定（如 TCP/UDP）無法處理    | 目的地主機 |
| 3    | **連接埠無法抵達（Port unreachable）**                                | 該 port 沒有應用程式在聽                 | 目的地主機 |
| 4    | **需要分段但設定為不可分段（DF bit set）**                                 | 送出的封包太大、需要分段，但 DF bit 被設定（不可分段） | 路由器   |
| 5    | **來源路由無法完成（Source route failed）**                            | source routing 中某個路由器無法拜訪       | 路由器   |
| 6    | **目的網路未知（Destination network unknown）**                      | 路由器**不知道這個網路**在哪                | 路由器   |
| 7    | **目的主機未知（Destination host unknown）**                         | 路由器**不知道有這台主機**                 | 路由器   |
| 8    | **來源主機被隔離（Source host isolated）**                            | 來源主機可能被隔離在某段封閉網路中               | 路由器   |
| 9    | **目的網路通訊被管理員封鎖（Network administratively prohibited）**        | 管理員設的 ACL 或防火牆規則阻擋了連線           | 路由器   |
| 10   | **目的主機通訊被管理員封鎖（Host administratively prohibited）**           | 同上，只是針對主機層級                     | 路由器   |
| 11   | **特定服務類型的網路無法抵達（Network unreachable for ToS）**               | 某種服務品質（QoS）下，網路不可達              | 路由器   |
| 12   | **特定服務類型的主機無法抵達（Host unreachable for ToS）**                  | 同上，只是針對主機                       | 路由器   |
| 13   | **主機被管理員設過濾規則而不可達（Communication administratively filtered）** | 通常是防火牆設定擋掉的                     | 路由器   |
| 14   | **主機優先權被拒絕（Host precedence violation）**                      | 封包要求太高的優先權，對方不接受                | 路由器   |
| 15   | **主機優先權被中止（Precedence cutoff in effect）**                    | 對方設定不接受低優先權的連線                  | 路由器   |

>[!bug] ❗️沒有收到 ICMP「目的地無法抵達」訊息 ≠ 封包送達成功
>📌 重點說明：
>1. **ICMP 是一種錯誤回報機制，不是確認機制**
> - 它只在發現明確錯誤時才會送回報
> - 如果封包「靜悄悄地」掉了、或被中途丟棄，可能根本不會有 ICMP 訊息產生
>2. **即使沒有收到 ICMP 錯誤，也不能保證資料真的有送達**
> - 資料可能還是在途中被丟掉（例如被路由器丟包）
> - 也可能被防火牆擋掉，但沒產生任何回應
### Time Exceeded: Two Situations (type 11)
- the packet stock in loop or circle 
	- cause by error in routing table 
	- ttl(time to live ) cut down to zero
	- 路由器丟棄資料封包並發送逾時訊息
- 當組成一則訊息的所有分片未在特定時限內到達目的地時
	- 當第一個資料封包到達目的地時，它會啟動計時器
	- 當計時器到期且所有分片均未到達時
	- 目的地會丟棄所有分片，並發送超時訊息
#### ICMP「時間超過（Time Exceeded）」訊息類型說明：

- **Code 0**：TTL（Time To Live）為 0  
    　→ 封包在網路中傳遞太久，TTL 數值歸零（例如封包陷入路由迴圈）  
    　→ 路由器丟棄封包並回報此錯誤
    
- **Code 1**：碎片重組超時  
    　→ 組成完整訊息的封包碎片沒有在時間限制內全部抵達目的地  
    　→ 目的端丟棄所有已收到的碎片並回報此錯誤
### Parameter Problem
- **當路由器或目的端在處理封包時，發現某個欄位的值不清楚或缺漏，就會發生這種錯誤**
- 換句話說，**封包的某個欄位值有問題（例如格式錯誤、欄位遺失或無法辨識）**
- 這時，接收端會丟棄該封包，並回傳一個 **ICMP「參數問題（Parameter Problem）」** 的錯誤訊息給來源端

> [!example]-
> 這題是在問：為什麼當目的端收到一個 IP 封包，開頭的前 8 個 bits 是 `01000010` 時，會丟棄該封包，並傳送 ICMP 的「參數問題（Parameter Problem）」錯誤訊息給來源端？
>
>IP 封包的**前 8 個位元**對應的是第一個位元組（Byte），其中前 4 個 bits 是 **IP 版本號（Version）**，接下來 4 個 bits 是 **IHL（Header Length，標頭長度）**。
>#### 分析 `01000010`
>- **前 4 bits：`0100` → 十進位 4** → 表示 IP 版本是 IPv4 ✅
>- **後 4 bits：`0010` → 十進位 2** → 表示 IHL = 2 ❌
>---
>
>#### 🧠 為什麼這是錯的？
>
>IHL（IP Header Length）是指 **IP 標頭的長度**，單位是「4-byte words」（即每單位是 4 bytes）。
>- 所以 `IHL = 2` 表示標頭長度為 `2 × 4 = 8 bytes`
>- 但 **IPv4 的最小標頭長度就是 20 bytes（即 IHL = 5）**
>- 所以 IHL = 2 是**非法值**，表示這個封包的格式是錯誤的


### Redirection
- 路由表是動態更新的。
- 然而，為了提高效率，主機不參與路由更新過程。
	- 主機數量非常多。(如果主機參預更新會造成很大的網路負擔)
	- 因此，主機使用靜態路由。
	- 只知道預設路由器的 IP 位址。
-  因為主機**只知道預設路由器**，若設定錯誤或網路拓樸有變化
	- 主機就可能會**把資料封包送錯路由器**
	- 這可能會導致封包無法抵達目的地，或產生額外的延遲與錯誤
- 主機通常從一張小型路由表開始，然後逐漸擴充和更新。
	- 實現此目的的工具之一是重定向訊息。

> [!question]- Question: Error-reporting messages的Data Section要帶什麼呢?
> 發生錯誤或是被丟棄的封包的資訊, 讓original source能知道哪一個封包被丟棄了
> 原始封包的 IP 標頭（Header）＋其後的前 8 個 bytes 的資料（Payload）
> 通常 前 8 bytes payload 就有transport layer 的所有資料（tcp udp）有助於判斷error

- 所有錯誤訊息中的資料部分都包含以下內容：
	- 原始資料封包(packet)的 IP 標頭
	- 這份資料報的前 8 個資料位元組
	- 提供有關連接埠號碼（UDP 和 TCP）和序號（TCP）的信息
- 然後，來源端可以將錯誤告知上層協定（TCP 或 UDP）

 ![[Pasted image 20250607155751.png]]
1. 當有error 發生
2. 在原本的 ip packet 前，接上 ICMP header 用以表達錯誤訊息
3. 在 icmp packet 上加上，ip header 好方便 network 寄送 packet 回 source host


## Query message
- 除了錯誤通報（Error messages）之外，ICMP 還有一些「查詢型訊息」，常用來測試與診斷網路連線狀況。 
	- Timestamp request and reply (skipped!)
	- Echo request and reply
### Echo Request and Reply

| 訊息名稱              | Type | 用途               | 常見工具   |
| ----------------- | ---- | ---------------- | ------ |
| Echo Request      | 8    | 測試主機可達           | `ping` |
| Echo Reply        | 0    | 回應 ping          | `ping` |
![[Pasted image 20250607192132.png]]
# Debugging Tools





## Ping
你這段描述的是「**ICMP Echo Request / Reply 機制**」，通常就是我們在電腦中使用的 `ping` 指令背後的原理。以下我幫你整理成**台灣用語與流程重點**，方便你複習與教學用：

---

## 🟢 如何判斷一台主機是否「存活並有回應」？

### 操作流程（以 `ping` 為例）：

1. **來源主機**發送一個 **ICMP Echo Request** 封包
    
    - Type: `8`
        
    - Code: `0`
        
    - 加入一個**序列號（sequence number）**，通常從 0 開始，每次發送加 1
        
    - 在資料區塊中放入「**發送時間戳記**」
        
2. **目的主機（如果在線上）**會回傳一個 **ICMP Echo Reply** 封包
    
    - Type: `0`
        
    - Code: `0`
        
3. **來源主機收到回應後**：
    
    - 用「目前時間 - 發送時間」計算 **RTT（Round Trip Time，來回時間）**
        

---

### 🕓 RTT 計算方式：

```text
RTT = 到達回應的時間點 - 當初送出 request 的時間點
```

這可以幫你測試：

- 目標主機是否在線上
    
- 從你的位置到對方的網路延遲（例如：延遲 20ms）
    

---

### ✅ 小結：

|項目|值|
|---|---|
|Request 類型|ICMP Type 8, Code 0|
|Reply 類型|ICMP Type 0, Code 0|
|檢查內容|主機是否在線上、有無封包遺失、RTT|
|工具|`ping` 指令|

---

如果你有興趣，我可以幫你用 Wireshark 分析 `ping` 封包的實際內容，或用程式（Python / Rust）模擬發送 ICMP 封包。要試試看嗎？






你這段是在說明 **`tracert`（Windows）或 `traceroute`（Linux/macOS）** 的原理。這個工具可以幫助我們「**追蹤封包從來源一路到目的地的路徑**」。以下是簡明的流程與台灣用語說明：

---

## 📍 `tracert`/`traceroute` 的原理與流程

這個工具其實是**用應用程式模擬 UDP 封包**，再**靠 ICMP 錯誤訊息來判斷每一跳（router）的位置**。

---

### 🧪 操作流程：

1. `tracert` 傳送一個 UDP 封包（目標是目的地，但設定一個非常小的 TTL 值）
    
    - 例如：TTL = 1
        
2. 第一台路由器收到封包時 TTL 減一 → TTL = 0  
    → 丟棄封包並送回 **ICMP Time Exceeded（type 11）**
    
3. `tracert` 收到這個 ICMP 回應 → 紀錄「第一跳 IP」與時間
    
4. 接著 `tracert` 傳 TTL=2 的封包 → 到第二跳 router，同樣會收到 ICMP time exceeded
    
5. 直到封包成功到達目的主機，但主機會丟棄這個奇怪的 UDP 封包（通常發送到不存在的 port）  
    → 回傳 **ICMP Destination Unreachable（type 3, code 3）**
    

---

### 💡 用到的兩種 ICMP：

|類型|用途|
|---|---|
|ICMP Time Exceeded (type 11)|中繼路由器 TTL 為 0 時發送，用來得知路徑中的每一跳|
|ICMP Destination Unreachable (type 3)|目的地主機收到無效 UDP 封包時回應，表示路徑已結束|

---

### 🧭 範例：

```bash
C:\> tracert www.google.com
```

可能看到：

```text
1   <1ms   192.168.1.1
2   10ms   140.113.1.1
3   25ms   203.78.xxx.xxx
...
10  50ms   142.251.xx.xx ← Google 伺服器
```

---

### ✅ 小結：

|功能|說明|
|---|---|
|工具名稱|`tracert`（Windows）、`traceroute`（Linux）|
|傳送方式|模擬 UDP 封包|
|依靠回應|ICMP Time Exceeded、Destination Unreachable|
|作用|找出「封包路徑」與「每一跳延遲」|

---

如果你想看實際封包，我可以教你怎麼用 Wireshark 抓出 `tracert` 的過程，要試試嗎？






