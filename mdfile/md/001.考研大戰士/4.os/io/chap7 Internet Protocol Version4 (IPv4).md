# Introduction
![[Pasted image 20250602191038.png]]
## IP
- A best-effort delivery service
	- 盡力而為的傳輸服務 / 盡力傳送服務
	- 不一定會送到
- An unreliable protocol
	- 不可靠的協定 / 不保證可靠性的協定
# Datagram
![[Pasted image 20250602190620.png]]

| 欄位名稱（英文）                   | 大小（bits） | 中文名稱（台灣常用說法）                                    | 說明                                                            |
| -------------------------- | -------- | ----------------------------------------------- | ------------------------------------------------------------- |
| **Version (VER)**          | 4        | 版本                                              | 指定 IP 協定版本（IPv4 為 4）                                          |
| **Header Length (HLEN)**   | 4        | 標頭長度                                            | 以 4 bytes 為單位，最小為 20 bytes                                    |
| **Service Type**           | 8        | 服務類型                                            | 指定封包處理優先順序與服務要求                                               |
| **Total Length**           | 16       | 封包總長度                                           | 包含標頭與資料，最大為 65535 bytes                                       |
| **Identification**         | 16       | 封包識別碼                                           | 辨識封包的唯一編號，用於分段重組                                              |
| **Flags**                  | 3        | 分段旗標                                            | 控制是否允許分段與最後一段標記                                               |
| **Fragment Offset**        | 13       | 分段偏移量                                           | 指定此段在原始資料中的位置                                                 |
| **Time To Live (TTL)**     | 8        | 生存時間（跳數限制）                                      | 避免封包無限循環傳送，遞減至 0 就丟棄                                          |
| **Protocol**               | 8        | 上層協定類型<br>（IP is network）<br>(TCP is transport) | 指定資料部分所使用的協定<br>（如 TCP=6、UDP=17）<br>,以方便多工解開(De-Multiplexing) |
| **Header Checksum**        | 16       | 標頭檢查碼                                           | 驗證標頭是否傳輸正確                                                    |
| **Source IP Address**      | 32       | 來源 IP 位址                                        | 封包發送端的 IP 位址                                                  |
| **Destination IP Address** | 32       | 目的地 IP 位址                                       | 封包接收端的 IP 位址                                                  |
| **Option**（可選）             | 可變長      | 選擇性欄位                                           | 額外功能，如記錄路徑、<br>時間戳、checksum...（可無）                            |
| **Data**（資料）               | 可變長      | 資料內容                                            | 實際要傳輸的資料，如 TCP/UDP 封包                                         |
> [!question]- 為什麼IP封包最小是20 bytes?
> 因為 **IP 封包的「標頭（Header）」有固定的基本欄位，加起來剛好是 20 bytes（160 bits）**。這是**最基本、沒有任何選用欄位（Option）**的情況下的大小。

> [!question]- 為什麼IP封包最大是65536 bytes?
> IP 標頭中的 `Total Length` 欄位是 16 bits，所以最大能表示的值是 2¹⁶ = 65536。
# Fragmentation
## Maximum Transfer Unit (MTU)
- The maximum length of the IP datagram is 65,536 bytes
	- IP 資料封包的最大長度為 65,536 位元組。
- However, each data link layer protocol has its maximum transfer unit (MTU
	- 但是，每個資料鏈路層協定都有其最大傳輸單元 (MTU)
![[Pasted image 20250602193549.png]]
- Question: 如果IP封包大於MTU呢?
- 解決方案：分片
	- 拆分 IP 資料報，使其能夠通過底層網絡
	- 當 IP 資料封包被分片時
	- 每個分片都有自己的 IP 標頭
![[Pasted image 20250602193526.png]]
- 資料封包可以由來源主機或路徑上的任何路由器進行分片。
	- 但重組只能由目標主機完成。
	- 每個分片都會成為一個獨立的datagram，因此可能會經過不同的路徑。
- 
IP需要紀錄什麼資訊才可以在Destination重組封包?
✅ 總結：IP 需要紀錄 3 個關鍵欄位，才能在 Destination 把所有 fragments 正確還原成原始封包：

| 功能                 | 對應欄位                | 說明                                                    |
| ------------------ | ------------------- | ----------------------------------------------------- |
| 1️⃣ 判斷是否為同一個封包     | **Identification**  | 所有來自同一個 datagram 的 fragments，這個欄位會是一樣的。               |
| 2️⃣ 決定 fragment 順序 | **Fragment Offset** | 告訴接收端「這個 fragment 在原始封包中的位置」，單位是 8 bytes。             |
| 3️⃣ 判斷最後一段         | **Flags（MF 位元）**    | 如果 **More Fragments（MF）= 0**，代表這是最後一段；反之 MF=1 表示還有後續。 |

# Options(skip)

# Checksum
- Errors in IP header can be a disaster
	- 試想Destination IP address錯了, protocol欄位錯了…
- Solution: checksum
	- A error detection method




---

### ✅ 一補數加法（One’s Complement Arithmetic）與 Checksum 計算原理

#### 🔹 傳送端計算流程：

1. 將封包資料分成 `k` 段，每段為 `n` 位元。
2. 對所有段落使用 **一補數加法** 加總。
   - 若產生進位（carry），需加回總和的最低位（wrap-around carry）。
3. 對加總結果取 **一補數**（bitwise NOT）作為 checksum。
4. 傳送封包（資料 + checksum）。

#### 🔹 接收端驗證流程：

1. 接收端將所有段落（包含 checksum）一起用一補數加法相加。
2. 結果應為 **-0**（一補數的「全 1」）。
3. 再次取一補數 → 得到 `0`。
4. 若結果為 `0` → 資料正確；否則 → 資料有錯誤。

---

### ✅ 一補數加法的數學邏輯

- 假設加總所有 section 得到總和 `T`
- Checksum = `-T`（一補數的反轉）
- 接收端相加：`T + (-T) = -0`
- `~(-0) = 0`，驗證成功 ✅

---

### ✅ 為什麼每個路由器都要重新計算 IP Header Checksum？

#### 原因：

- 每個路由器轉送封包時，會將 IP header 中的 `TTL` 欄位減 1。
- Checksum 是針對整個 header 計算的，TTL 改變後 checksum 就失效。
- 所以，每個路由器都必須：
  - 更新 TTL
  - 重新計算 checksum

#### 小結（考試用）：

> IP Header Checksum 必須由每個路由器重新計算，因為 TTL 欄位在轉送時會被修改，而 checksum 是根據整個 header 計算出來的。

---

### ✅ 為什麼 IP 的 Checksum 只涵蓋 Header 而不包括資料（Payload）？

#### 原因：

1. **資料驗證由上層協定處理**：
   - TCP、UDP 等協定會針對資料部分加上自己的 checksum。
   - 沒必要在 IP 層重複驗證。

2. **IP 層職責有限**：
   - IP 協定（在網路層）只負責封包的轉送與路由。
   - 不需關心資料內容，只需確保 header 沒錯。

3. **效能考量**：
   - 資料可能很大，計算整包 checksum 成本高。
   - 只檢查 header 可大幅減少運算量，提升轉送效率。

#### 小結（口訣）：

> IP Checksum 只檢查 Header，因為：
> - IP 層不管資料內容（只管送到哪）
> - 資料驗證由上層處理（TCP/UDP）
> - 降低運算負擔，提高轉送效率

---

### ✅ 補充範例（8 位元簡易示範）：

資料段：
```

10101010  
01010101  
11110000
 → 資料正確；否則 → 資料有錯誤。
```

加總後：
```

10101010 + 01010101 = 11111111  
11111111 + 11110000 = 1_11101111 → 加回進位 → 11110000

```

取反得到 checksum：
```

~11110000 = 00001111

```

接收端加總（含 checksum）：
```

11110000(所有段落的加總) + 00001111 = 11111111  
~11111111 = 00000000 ✅

```

---

📌 **參考應用：**
- IPv4 Header Checksum
- 使用在 OSI 模型的「網路層」
- TCP、UDP、ICMP 則有各自的資料 checksum 機制

