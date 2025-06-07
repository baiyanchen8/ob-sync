# Delivery
- Two methods
	- Direct versus indirect delivery
	- *直接*或**間接**

- 定義Direct delivery
	- 在**同一個物理網路**之間傳輸資料稱為 delivery
	- 當來源和目標位於同一實體網路時
	- 或在最後一個路由器和目標主機之間進行傳輸

- **How ?** 認定 direct delivery
	- compare network address between destinate host ^& current net 
	- if equal => direct 

# Forwarding
## define
Forwarding 是指資料封包（packet）在網路設備（像是路由器或交換器）之間轉發的過程，也就是把收到的封包根據其目的地，送往下一個適當的設備。
## 困境
在indirect delivery中，我們需要將封包轉送到其他網路，轉送需要主機/路由器擁有routing  table;然而，隨著網路數量的增加，路由表中的項目數量也會增加。
因此我們需要尋找減少 routing table size 的技術。
## Next-Hop routing
與其在每張 routing table 中紀錄整個路徑，不如只紀錄下個中轉站的address，可以大幅減少長途轉送的 size。

![[Pasted image 20250601142539.png]]

## Network-Specific Routing
把整個 loacl aera 轉為使用 Hole Network address 而不是單獨紀錄，以減少 Routing table size
![[Pasted image 20250601142946.png]]
## Default Routing 
將不知道要去哪（即不再 routing table 中的 destination），全部送往 default route


## Forwarding with Classful Addressing
- A forwarding module would consists of **3** tables
	- One for each unicast class(A/B/C)
- 欄位
	- 目的網路位址（Network Address）
		- 這是你想要送資料到的目標網段（不一定是一台主機）。  
		- 這裡假設使用的是「網段為單位的路由」（network-specific forwarding），而不是一對一主機的路由（host-specific forwarding）。
	- 下一跳地址（Next-hop Address）
		- 如果是**間接轉送（Indirect Delivery）**，就要指定下一個 Router 的 IP 位址。 
		- 如果是**直接轉送（Direct Delivery）**（目的地在同一個網段），這一欄可以是空的或「自己處理」。
	- 界面/接口編號（Interface Number）
		- 指出這筆資料要從哪一個網路介面送出去（像 eth0、eth1）。這對一台有多個網卡的 router 很重要，決定資料從哪裡出去。
![[Pasted image 20250601144329.png]]
![[Pasted image 20250601144829.png]]
## Forwarding with Classless Addressing
就是把 CIDR（/n） 標記法加入
![[Pasted image 20250601150254.png]]

# Structure of a Router
![[Pasted image 20250601150743.png]]

| 元件名稱                     | 層級/角色         | 功能說明                                                              |
| ------------------------ | ------------- | ----------------------------------------------------------------- |
| 🔌 **Input Port**        | 實體層 / 資料鏈結層   | - 從線路接收訊號並轉為位元（bit）<br>- 從資料幀中解封（decapsulate）出封包<br>- 暫存封包於輸入佇列   |
| 🔁 **Switching Fabric**  | 核心傳輸模組 / 資料平面 | - 將封包從輸入埠移動至輸出埠- 負責「資料轉送」的內部搬運<br>- 例：交叉開關（Crossbar）              |
| 📤 **Output Port**       | 資料鏈結層 / 實體層   | - 將封包加入輸出佇列<br>- 封裝成資料幀（encapsulate）<br>- 傳送封包到實體媒介               |
| 🧠 **Routing Processor** | 控制平面 / 網路層    | - 根據目的位址查詢路由表（routing table）<br>- 做出下一跳決策<br>- 負責執行路由協定如 OSPF、BGP |
