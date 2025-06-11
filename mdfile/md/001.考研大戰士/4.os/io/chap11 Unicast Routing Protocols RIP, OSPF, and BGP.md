# Introduction
- Routers forward packets by searching the routing table
	- how to create route table 
	- by routing protocol

# Intra- and Inter-Domain Routing
- internet is so large
	- only  one protocol can not handle all routing  table update
- 因此，整個網際網路會被劃分為多個「自治系統」（AS，Autonomous System）。  
	- 一個自治系統是指在同一個管理單位下，由多個網路與路由器所組成的一個群組。
- 域內路由 (Intra-domain routing)
	- 自治系統內部路由
	- 每個自治系統 (AS) 可以選擇自己的域內路由協定
	- 範例：距離向量和鏈路狀態
- 域間路由 (Inter-domain routing)
	- 自治系統間路由
	- 僅使用一種域間路由協定
	- 範例：路徑向量
	
![[Pasted image 20250610185405.png]]
- Distance-vector routing algorthim
	- Classical Distributed Bellman-Ford algorithm
	- RIP (Routing Information Protocol) protocol
- Link-state routing algorithm
	- Centralized version of the shortest path computation
	- Every router has the whole “picture” of an AS(自己所在的)
	- OSPF (Open Shortest Path First) protocol

![[Pasted image 20250610185924.png]]

# Distance Vector Routing
- Each node maintains a vector (table) of minimum distances to every node
- 所有節點維持一個到任意節點的distance table 
![[Pasted image 20250610190513.png]]
to (目的地)
Cost (distance)
Next (Next hop 中間點)

## Initialization
- 在最一開始所有 node 僅知道自己和直接接觸的鄰居的 distance
	- **Q:** how to know
	- **A:** Send greeting msg to 發現的 neighbor IP and check distance
## Sharing
Idea of distance vector routing: **sharing of information between neighbors**

### who to share?
 each node shares its routing table with its **immediate neighbors(隔壁鄰居)**

### what to share?
**periodically(週期性)** and when there is a change (see the following slide)
### when to share?
- Periodic update
	- A node sends its routing table in a periodic update
	- Normally every 30 seconds
- Triggered update
	- A node receives a table from a neighbor resulting in changes in its own table
		- 收到其他 node 的 table 發生改變
	- A node detects some failure in the neighboring links which results in a distance change to infinity
		- 失連
### Question 3: how much of the table must be shared ?
![[chap 11 2025-06-10 19.46.34.excalidraw]]
只需要前兩個 column，其他的 node  並不需要知道 A & E 之間隔著一個 C
### Updating 如何更新自身的 table
![[Pasted image 20250610201044.png]]
#### 📌 1. 如果目的地 **不在自己的路由表裡**：
👉 就把這筆資訊「**直接加入**」到自己的路由表。
#### 📌 2. 如果目的地 **已經存在於自己的路由表**中，則判斷：
- **2-1. 如果廣播者就是目前這筆目的地的下一跳（next-hop）**：  
    👉 表示是同一條路徑，那就**更新這筆資料**（也就是用新的跳數、計算過的成本來取代舊的）。
- **2-2. 如果新的跳數（hop count）比原本表格裡的還小**：  
    👉 表示找到了**更短的路徑**，那就**用新的資訊取代舊的紀錄**
![[Pasted image 20250610201030.png]]

### Count to Infinity

> [!Question]  當網路有變動時, Distance Vector Routing需要一段時間才會收斂. Why?
> 因為 Distance Vector Routing 是使用一個一個 hop 傳遞擴散新 routing 的方法，所以會需要一段時間才能收斂

> [!note] A well known problem **Count to Infinity**
> 當一個連接斷開時，該 rourter 的 distance 會變為 infinte 
> 但要所有 node 得知此事需要一段時間
> 因此, 一個routers可能會分享過時或是錯誤的資訊

One example of count to infinity is the two-node loop problem.
See the following table
1. both node A and B know how to reach node X
2. the link between A and X fails 
	-  Node A change its table
		1. If node A can send its routing table to B immediately
			- Everything is fine
		2. However, if node B sends its routing table to A first 
			- Node A assumes that B has found a way to reach X
3. A sends its new update to B and B also update its routing table 
4. B sends its new update to A and so on…until the cost reach infinity
5. Then both A and B knows that the link is broken
![[chap 11 2025-06-10 20.59.41.excalidraw|700]]
上述現象可能需要數秒甚至十秒以上網路才會收斂
- 因此，在成本達到無限大之前
	- 發往 X 的封包在 A 和 B 之間來回跳轉
	- 造成環路不穩定性
- Thus, distance vector routing has the problem of instability(不穩定)
	- A network can become unstable
- 複習: 所以才需要TTL(Time-to-Live)欄位
# RIP（skip）

# Link State Routing

> [!question] Question: 如何克服Distance Vector Routing的問題呢?
> Hint: 當網路有變動時, 必須盡快讓所有Router知道
> Ans: 所以不能只跟隔壁(immediate)鄰居分享, 要立刻跟所有鄰居分享

> [!question] Question 2: 分享的資訊也不能是Distance Vector. Why?
> Ans: (1)因為Distance Vector就是需要更新Routing Table後再往外傳遞, 可是我們現在不要這麼做了~
> (2). 分享Hop Count會造成盲目相信鄰居的資訊(即時鄰居的資訊是錯誤的)

> [!question] Question: 那要分享什麼呢?
> Ans: 網路的拓樸

- The idea of link state routing
	- Each node uses the **same global topology** to create its routing table
	- But the **routing table** for each node is **unique**
	  
> [!question] Question: How to Build the Global Topology in Each Node?如何讓所有節點知道整個 as 的拓普
 
 1. 🧭 如何建立整體的網路拓撲（Global Topology）？
雖然**每個節點（router）本身並不知道整張網路拓撲的全貌**，但每個節點都會有**部分的網路資訊**。而這些部分資訊之間會有**重疊的區域（overlap）**，這種重疊性讓我們可以做到以下這件事：
2. 🔗 部分資訊 + 重疊 = 組出完整拓撲圖
- 每個節點只知道**它自己與鄰居的連線關係**（例如連到誰、成本是多少）。
- 不同節點的這些資訊會**互相重疊、互相補充**。
- 因此，只要收集到**每個節點的鏈路狀態資訊**（例如透過 OSPF 廣播的 LSA 資料），就可以將它們**整合成整張網路拓撲圖**。
## Buliding Routing Tables
 - Four sets of actions in link state routing
	 - Creation of the states of the links by each node
		- Create the Link State Packet(LSP)
	- Dissemination of LSPs to every other router, called flooding
		- **將 LSP 傳播到其他每個路由器，稱為泛洪**
	- Formation of a shorten path tree for each node
		- 為每個節點形成一棵縮短路徑樹
	- Calculation of a routing table based on the shortest path tree
		- 基於最短路徑樹的路由表計算
## Creation of Link State Packet (LSP)
- Assume a LSP carries
	- The node identity, 
	- The list of links 
	- A sequence number
		- Distinguishes new LSPs from old ones

| 項目       | 說明                        |
| -------- | ------------------------- |
| LSP 產生時機 | 1. 拓撲變動時 2. 定期（60~120 分鐘） |
| 傳播方式     | Flooding（泛洪傳播到整個 AS）      |
| 為什麼要泛洪傳播 | 確保所有路由器的拓撲資料一致，避免路由錯誤     |
## Flooding of LSPs (Skip!)
## Build to Global Topology
- 當所有節點都收到 flood ,Bulid the global topology 
	- How ?
![[Pasted image 20250611124945.png]]
![[Pasted image 20250611124952.png]]
- 有了完整的拓樸, 就可以產生Shortest Path Tree.
	- How?
	  
| 步驟編號 | 操作內容（Dijkstra）                                | 說明                          |
| ---- | --------------------------------------------- | --------------------------- |
| 1    | 將本地節點（root）設為起點，放入暫存清單（Tentative List）        | 開始建立最短路徑樹。                  |
| 2    | 檢查暫存清單是否為空                                    | 若為空表示所有節點都處理完畢，演算法結束。       |
| 3    | 從暫存清單中挑選「到目前為止距離最短」的節點，移至永久清單（Permanent List） | 表示已確認這條是最短路徑，之後不再更新這個節點的資訊。 |
| 4    | 檢查剛移入永久清單的節點的所有「尚未處理」的鄰居節點                    | 目的是要更新那些鄰居節點的最短路徑成本。        |
| 5    | 對每個鄰居節點進行以下處理：                                |                             |
| 5-1  | 若鄰居**不在暫存清單** → 新增到暫存清單，並計算成本                 | 把從起點經過目前節點到這個鄰居的總成本記下來。     |
| 5-2  | 若鄰居已在暫存清單中，且目前計算的成本**更小** → 用新成本取代原本的紀錄       | 找到更短的路，就要更新記錄（即更新距離與上一跳路由）。 |
| 6    | 回到步驟 2                                        | 持續從暫存清單中選最短者，直到所有節點都處理完。    |
## Calculation of a routing table based on the shortest path tree
- 有了Shortest Path Tree, 就可以產生Routing Table.
	- How ?
	- 其實就是簡單的把剛建立的 loacl node's shortest path tree轉換為表格
	  
| 步驟  | 操作內容                                         | 說明                           |
| --- | -------------------------------------------- | ---------------------------- |
| 1   | 從最短路徑樹中取得所有節點到本地節點的**最短路徑成本**                | 每個節點對應一個「距離值」                |
| 2   | 對於每一個目的地節點，從最短路徑樹反推：到該節點的**下一跳（next hop）是誰** | 找到從本地出發、經過的第一個節點，就是發送封包時的下一跳 |
| 3   | 為每個目的地建立一筆路由紀錄：`(目的地 IP, 下一跳 IP, 路徑成本)`      | 一個節點會對每個可達的網路建立這樣一筆資料        |
| 4   | 重複以上步驟直到所有節點都處理完，形成完整的路由表                    | 最後會得到一張「目的地 → 最佳路徑」的完整對照表    |
![[Pasted image 20250611125606.png]]
![[Pasted image 20250611125659.png]]

|項目|說明|
|---|---|
|Count-to-infinity 是什麼？|是 Distance Vector Routing（像 RIP）中常見的問題，因為節點間只能靠鄰居交換路徑資訊，一旦路徑失效，有可能彼此錯誤更新路徑，導致跳數無限增加。|
|Link State 的做法不一樣|Link State Routing（像 OSPF）每個節點都有**整張網路的拓撲圖**，它不是靠鄰居傳話，而是**直接計算出整體最短路徑**，不會發生錯誤反覆更新。|
|使用 Dijkstra 演算法|有了完整的拓撲資訊，每個路由器用 Dijkstra 演算法計算路徑，**只算一次、不需要等待鄰居修正資訊**。|
|拓撲改變會立即觸發重計|一旦有鏈路失效，節點會廣播新的 LSP 給整個 AS，所有路由器都同步更新並重算最短路徑，不會有逐跳誤傳的情況。|
# OSPF(skip)

# Path Vector Routing(skip)

# BGP(skip)