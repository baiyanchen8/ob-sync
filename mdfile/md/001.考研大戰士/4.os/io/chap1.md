topic : introduction

## A brief history

- Network
	- A group of connected, communicating devices, such as computers and printers
	- 由一坨設備互相連接組成
- **i**nternet(開頭小寫)
	- Two or more networks that can communicate with each other
	- An internet![[Pasted image 20250521160629.png]]
- **I**nternet(開頭大寫)
	- The most notable internet
	- A collaboration of more than hundreds of thousands interconnected networks
	- 最引人注目的互聯網 
	- 數十萬個互聯網絡的協作


---

**1969 年：建立四節點的 ARPANET（網路）**  
加州大學洛杉磯分校（UCLA）、加州大學聖塔芭芭拉分校（UCSB）、史丹佛研究所（Stanford Research Institute）與猶他大學（University of Utah）之間建立連線，是網際網路的雛型。

**1972 年：網際網路誕生，透過「閘道器（gateway）」連接不同網路**  
首次將不同的網路（擁有不同的封包大小、介面與傳輸速率）連接起來，讓網際網路真正開始具備互通能力。

**1973 年：開始發展 TCP/IP 協定套件**  
這是後來支撐整個網際網路運作的核心通訊協定。

**1981 年：加州大學柏克萊分校（UC Berkeley）將 TCP/IP 加入 UNIX 系統**  
這個修改使得 TCP/IP 協定能夠更廣泛地被學術界與企業採用，推動了其普及。

**1983 年：TCP/IP 成為官方通訊協定**  
ARPANET 在這一年正式改用 TCP/IP 作為標準協定，標誌著現代網際網路的真正起點。

---

## Protocols and standards

---

### 📡 **通訊協定（Protocol）**

通訊協定是一組規則，用來規範資料通訊的方式。

---

#### 🔑 **三個關鍵元素**

1. **語法（Syntax）**  
    　資料的結構與格式，例如封包（packet）的編排方式。 
    
2. **語意（Semantics）**  
    　每個位元區段（bit section）所代表的意義。
    
3. **時序（Timing）**  
    　- 資料應該在什麼時間傳送  
    　- 傳送的速度有多快
    

---

### 📏 **標準（Standards）**

目的：

- 維持開放市場，讓各家製造商能公平競爭
    
- 確保資料通訊之間具有**互通性（Interoperability）**
    

#### 兩種類型的標準：

1. **事實標準（De facto）**  
    　指沒有經過正式核准，但因為廣泛使用而成為「事實上的標準」。
    
2. **法定標準（De jure）**  
    　指經由**官方機構立法制定**的標準。
    

---

#### 📦 **TCP/IP 協定套件中的標準機構**

- **IEEE（電機電子工程師學會）**：負責**第 1 層（實體層）與第 2 層（資料連結層）**的標準
    
- **IETF（網際網路工程任務小組）**：負責**第 3 層（網路層）、第 4 層（傳輸層）以及應用層**的標準
    
