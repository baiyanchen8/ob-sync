![[Pasted image 20250530005232.png]]
# Wired Local Area Networks
|技術名稱|說明|
|---|---|
|**Ethernet LAN（乙太網路）**|最常見、目前最主流的 LAN 技術。使用有線（RJ45）或無線（Wi-Fi）方式，支援從 10 Mbps 到 100 Gbps。|
|**Token Ring LAN（令牌環網路）**|IBM 發展的技術，裝置依順序傳遞「令牌（token）」來控制傳輸權。現已幾乎淘汰。|
|**Token Bus LAN（令牌匯流排網路）**|結合匯流排拓樸與 token 控制方式的網路技術，主要應用於工業用途，現在少見。|
|**FDDI（光纖分散式資料介面）**|使用光纖傳輸、雙環架構，傳輸速率通常為 100 Mbps，適合需要高可靠性與速度的環境。|
|**ATM LAN（非同步傳輸模式區域網路）**|ATM 是高速封包交換技術，支援資料、聲音、影像混合傳輸。過去流行於大型機構，現在幾乎被 IP/Ethernet 取代。|
## IEEE Standard
- IEEE Project 802
	- Specify functions of the physical layer and the data link layer of LAN protocols
- Relationship of the 802 standard to OSI model
	- IEEE subdivide the data link layer into two sub-layers
		- Logical Link Control (LLC)
		- Media Access Control (MAC)

| 子層名稱                          | 中文名稱     | 功能簡介                                                          |
| ----------------------------- | -------- | ------------------------------------------------------------- |
| **LLC（Logical Link Control）** | 邏輯鏈結控制子層 | 負責提供錯誤檢測、流程控制，並將資料與上層（如網路層）連接起來。它讓不同網路協定能在相同的資料鏈結層上運作。        |
| **MAC（Media Access Control）** | 媒體存取控制子層 | 負責「誰可以發送資料」的決策，也就是控制裝置如何在網路媒介（例如乙太網路）上存取資料，包含 MAC 位址、碰撞避免等機制。 |


![[Pasted image 20250530143836.png]]

```
網路層 (IP)
   ↑
LLC  ←←←←← 協定分類與識別
   ↑
MAC  ←←←←← 資料封包建構、位址處理、媒介存取
   ↑
實體層（Ethernet cable, 無線等）← 電子訊號傳輸
```

![[Pasted image 20250530143928.png]]

| 欄位名稱                               | 長度               | 用途說明                                                    |
| ---------------------------------- | ---------------- | ------------------------------------------------------- |
| **Preamble（前置碼）**                  | 7 bytes          | 提供接收端訊號同步的參考，內容是 56 bits 的 101010...                    |
| **SFD（Start Frame Delimiter）**     | 1 byte           | 告訴接收端資料框正式開始（值為 10101011）                               |
| **Destination Address（目的 MAC 位址）** | 6 bytes          | 指明資料要送到哪個網卡（裝置）                                         |
| **Source Address（來源 MAC 位址）**      | 6 bytes          | 說明這筆資料來自哪台裝置                                            |
| **Length or Type**                 | 2 bytes          | 指明 payload 的長度（IEEE 802.3）或類型（EtherType，像是 IPv4, ARP 等） |
| **Data and Padding**               | 46 \~ 1500 bytes | 真正要傳送的資料（payload），不足 46 bytes 會補 0                      |
| **CRC（循環冗餘檢查碼）**                   | 4 bytes          | 用於檢查傳輸中是否發生錯誤（錯誤檢測）<br>CRC-32 for error detection       |

![[Pasted image 20250530151053.png]]

### Why frame Length 有最小限制
- 因為 CSMA/CD 的限制
- 在後面介紹

### Why frame Length 有最大限制
- 在乙太網路設計之初，記憶體成本高昂
- 有助於減少緩衝區大小
- 防止某個站點獨佔共享介質

## Ethernet Evolution
**Designed in 1973 by Xerox**
### Four Gen
#### Standard Ethernet (10 Mbps)
- 其基礎拓普會是個 Bus or a Star
- **Question: bus有什麼特色呢?**
	- 所有佔點共享介質（乙太）
		- 同時只有一個佔點可以使用介質
	- 當有佔點傳輸資料，所有佔點都會收到資訊（只有broadcast）
		- 非目標地點會**自己**刪除資訊
##### Access Method CSMA/CD

- **🎧 CSMA/CD 傳輸流程（像「對講機」一樣）：**
1. 🔍 **先聽看看**：設備先檢查媒介上有沒有訊號（carrier sense）
2. 🟢 **沒聲音就傳**：如果媒介是空的，就開始傳送資料
3. ⚠️ **若發生碰撞**：如果在傳送途中發現訊號異常 → 表示撞到了
4. 🚨 **發送 jam 訊號**：提醒其他人「撞到了，先不要傳」
5. ⏱️ **等待隨機時間再重傳**（使用 exponential backoff 演算法）
---
雖然有以上算法但不是撞不到，還是可能發生以下請景
![[Pasted image 20250530160156.png]]

| 名稱                      | 中文解釋 | 說明                                                                                                                   |
| ----------------------- | ---- | -------------------------------------------------------------------------------------------------------------------- |
| **Multiple Access**     | 多重存取 | 網路上的每一台設備都有「平等」的機會傳送資料。沒人有優先權，這是一種公平機制。                                                                              |
| **Carrier Sense**       | 載波感測 | 在傳送資料前，先「聽聽看」網路媒介是否正在使用。簡單說就是「**聽完再講**」、「沒人講話再輪到我講」。                                                                 |
| **Collision Detection** | 碰撞偵測 | 若有兩台裝置同時開始傳送資料，會導致「碰撞」這時候裝置會「察覺訊號變形」，並中斷傳輸、發送 jam 訊號通知其他人。<br>If a collision<br>Wait for a random time and try again |
![[Pasted image 20250530162538.png]]
##### ❗ 為何這圖說明「需要最小封包長度」？
如果 A 傳的 frame 太短，可能會在 **還沒偵測到碰撞**前就傳送完了  
👉 **A 會以為傳成功，實際上資料早就撞爛了！**

##### ✅ 為什麼需要這個「最小封包長度限制」？
因為在**最壞情況（worst case）下**，有可能兩台設備剛好位在網路兩端，  
當第一台開始傳資料時，第二台在「還沒收到」訊號之前也開始傳，造成 **碰撞（collision）**。
若封包太短，第一台可能**在還沒發現碰撞之前就已經傳送完畢**，以為成功送出了，但實際上資料早就撞爛了！

##### ✅ **Frame 傳送時間（ transmission time ）≥ 2 × 傳播延遲(propagation)時間**
| 項目   | 傳輸時間 Transmission Time | 傳播時間 Propagation Time |
| ---- | ---------------------- | --------------------- |
| 意義   | 將資料推出去所需時間             | 訊號在媒介中傳送所需時間          |
| 影響因素 | 封包大小、傳輸速率              | 傳輸距離、媒介速度             |
| 例子   | 將 1 KB 封包推出去需要幾毫秒      | 訊號從台北傳到台中需要幾微秒        |

這樣一來，就能保證：
- 如果有碰撞發生
- 傳送端**一定還在傳資料**
- 就能即時偵測到錯誤 → 發送 jam 訊號 → 等待重傳

>[!Example]-
>![example](/001.考研大戰士/4.os/io/else/example1)


#### Fast Ethernet (100 Mbps)     
- 從 Hub & Bus 改為 Switch 
- 從 Half-Duplex 改為 Full-Duplex [[chap2 The OSI Model and TCP IP Protocol Suite#物理層的溝通模式 Duplex|Duplex]]
	- 因此不會碰撞,不需要碰撞處理
- 網路長度（實體長度）
	- 不再是因為為了維護CSMA/CD的運作了!而是因為訊號品質的原因!
- 網路封包大小的限制呢?
	- 還是維持!
#### Gigabit Ethernet (1 Gbps)
#### Ten-Gigabit Ethernet (10 Gbps)

# Wireless LANs
|項目|DCF（分散式協調功能）|PCF（集中式協調功能）|
|---|---|---|
|**中文名稱**|分散式協調功能|集中式協調功能|
|**英文全名**|Distributed Coordination Function|Point Coordination Function|
|**主要原理**|**CSMA/CA**（避免碰撞）|**Polling**（輪詢機制）|
|**是否有中央控制者？**|❌ 沒有|✅ 有（AP 當控制者）|
|**媒體存取方式**|自行聆聽→等待→傳送|AP 控制誰可以傳送|
|**碰撞情況**|可能碰撞→用 CA 避免|幾乎不會碰撞（有排程）|
|**適用場景**|多數 Wi-Fi 使用場景|需要高即時性或 QoS 場景|
|**技術難度與硬體需求**|簡單、適合一般設備|複雜，需要 AP 支援|
|**使用情境**|家用 Wi-Fi、筆電、手機|企業級 Wi-Fi、VoIP、視訊串流|
## CSMA/CA （collision avoidance）
- Why 不使用CSMA/CD
	- 因為無線介質中無法方便的檢測碰撞
	- The distance between stations would be great
		- Signal fading could prevent a station from hearing a collision at the other end
#### CSMA/CA Flow chart [[flow1]]
![[Pasted image 20250530221015.png]]![[Pasted image 20250530221516.png]]

| 項目      | 說明                                              |
| ------- | ----------------------------------------------- |
| NAV 是什麼 | 一個用來「避免碰撞」的虛擬計時器                                |
| 怎麼設定    | 根據收到的 RTS、CTS、DATA 裡的 Duration 欄位設定             |
| 有什麼用    | 讓其他裝置知道什麼時候不能發送資料（即使看不到發送者），避免 hidden node 碰撞問題 |
| 類比      | 像是聽到別人要發言時，自己倒數計時「現在不能講話」                       |
### SIFS & DIFS 的愛恨情仇
> [!question]- 為什麼需要等DIFS的時間?
> - 給「想要開始傳資料」的裝置用來等待的時間
> - 確保大家都有公平的機會搶得通道控制權
> - 如果通道是空的，裝置要等 DIFS 才能開始傳送
    >
>- 而 DIFS 比 SIFS 長，**這樣就不會和 CTS、ACK 這些優先訊號搶通道**
    >
>- 換句話說，**SIFS 保護正在進行的通訊，DIFS 提供公平的起跑點**
---
> [!question]- 為什麼需要等SIFS的時間?

| 項目       | 時間長度（以 802.11b 為例） | 用途                                       | 優先權 |
| -------- | ------------------ | ---------------------------------------- | --- |
| **SIFS** | 10 微秒              | 正在通訊的雙方在傳完訊息後，等一下再傳下一個（RTS→CTS、DATA→ACK） | 高   |
| **DIFS** | 50 微秒              | 其他設備觀察到媒介空了後，等一段時間才可以傳資料，避免插話            | 低   |
### Network Allocation Vector

Network Allocation Vector (NAV) 是 CSMA/CA 機制中的一個關鍵概念，主要用於協助無線網絡設備避免碰撞。

每個 RTS（發送請求）、CTS（允許發送）和 DATA（數據）幀的標頭都包含一個「持續時間字段」，該字段表示發送端需要佔用信道的時間長度。當其他設備收到這些幀時，它們會根據該持續時間字段啟動一個稱為 NAV 的計時器。只要 NAV 計時器未到期，其他設備就應該避免感測媒介並暫停傳輸，以確保當前的通訊不受干擾。


![[Pasted image 20250530230046.png]]
## Hidden Station Problem
![[Pasted image 20250530232218.png]]
### 🕵️‍♂️ Hidden Station Problem（隱藏站問題）是什麼？

在無線網路（如 Wi-Fi）中，有些設備可能 **彼此聽不到對方的訊號**，但卻會同時與同一個設備溝通，導致資料碰撞。
### 解法 RTS/CTS 
在 RTS/CTS 中加入 nav timer 以告知佔用時間用以避免干擾
### Question: 使用RTS/CTS就完全解決Hidden Stations的問題嗎?
| 問題                      | 說明                                                        |
| ----------------------- | --------------------------------------------------------- |
| 是否能完全解決 Hidden Station？ | ❌ 無法百分百                                                   |
| RTS/CTS 主要解決什麼？         | 預約通道，讓其他站台知道有人要傳資料                                        |
| 有哪些無法解決的情況？             | 聽不到 CTS、控制訊號碰撞(CTS撞CTS)、小封包未開啟 RTS/CTS、Exposed Station 問題 |
| 效果如何？                   | ✅ **能大幅改善 Hidden Station 問題，但不是萬靈丹**                      |

|問題名稱|問題描述|為什麼 RTS/CTS 解不了？|結果／影響|
|---|---|---|---|
|**聽不到 CTS**|有些隱藏站雖然聽得到 RTS，但因距離太遠或遮蔽，**聽不到 CTS**|聽不到 CTS → 不會啟動 NAV → 不知道有人佔用通道 → 可能亂入|發生碰撞|
|**控制訊號碰撞**|RTS、CTS 自身是封包，**彼此也可能在空中碰撞**|RTS/CTS 沒有優先權保護，也不保證不會碰撞|無法建立連線、通訊延遲|
|**小封包未啟用 RTS/CTS**|實務中通常設定「超過某個大小的封包」才啟用 RTS/CTS，**小封包直接送**|小封包沒經 RTS/CTS → 沒有 NAV 保護 → 其他站不知道有人在通訊|小封包之間更容易碰撞|
|**Exposed Station 問題**|一個裝置雖然**聽到附近有傳輸（例如 CTS），但其實可以與其他方向的裝置傳輸**|RTS/CTS 沒有判斷方向性，只要聽到 CTS 就會退讓，即使實際上沒衝突|效能下降，頻寬浪費|
# Connecting Devices
![[Pasted image 20250530234725.png]]
