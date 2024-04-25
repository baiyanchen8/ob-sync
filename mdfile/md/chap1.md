---
title: chap1
tags: ['#計組']

---


# 簡介
對計組的簡單介紹
# 主題
## A world full of computers
### six classes of computer

#### Personal computer
1. 個人電腦(一般家用主機)
2. 高度訂製化
3. 有許多軟件，通用用途
4. 會在成本/能效上做取捨
#### Server
1. 基於network提供各種服務
2. high **perform** ,reliable，capacity
3. 可以從個人主機到巨大
#### Super computer
1. high perform ,reliable，capacity
2. 超級計算機就是要有超級算力
#### Embeding Device
1. 單一功能居多
2. 多為一個系統中的一部份 ex : 車載系統
3. 因為系統大多不大 →嚴格限制 功率、性能、成本
#### personal mobile device(PMD)
1. 多由電池供電 → low power
2. 多數皆能上網 
3. 便宜 
#### cloud computing
1. 多與PMD結合，software run on pwd ,data run on cloud database
2. Portion of software run on a PMD and a portion run in the Cloud
3. [SIP](/SIP.md)
4. [四種部屬雲](/四種部屬雲.md)
5. 延伸介紹: industry 3.0 vs 4.0
    
    | ----         | Industry 3.0                             | Industry 4.0                                                 |
    | ------------ |:---------------------------------------- |:------------------------------------------------------------ |
    | 人為干預部分 | 會需要人在事先設定好程序靠本地端電腦執行 | 多數生產過程使用大量數據和智慧互聯機器，不依賴任何人為干預。 |
    
    詳細介紹:[industry](/hxL487ZzR3iXJlU1twpUlg)
    
![](image/BJUVc6obT.png)

## Looking at hardware and software from a single computer
### hardware
#### input
keyborad、mouse
##### [POSTPC](https://hackmd.io/o_E6p7YNTTSVn-a8lqwLiQ) 後PC時代
![](image/By_Ay6jW6.png)


#### output
**[CRT](https://hackmd.io/TepuCGZWRpi9m4aKCLO-uw)**

#### memory


| nonvalid   | valid                |
| ------- | ----------------------- |
| magnetic、flash、CDROM、DVD|       memory、cache、register                  |
由於valid and nonvalid 使memory分為兩種大類型，一種用於快速存取，另一種用於保存資料。
##### valid memory
memory、cache、register \
![](image/r1PoWaoZp.png)

**由於其價格差異，因此才會分為多層使用(越快越貴)**

#### network
![](image/BJWnZTo-6.png)
**WAN** : wide area netwwork → 輸入(通常只有一孔)\
**LAN** : Local area netwwork → 輸入(通常有多孔)\
**Wireless network**: WiFi, Bluetooth


#### cpu
##### [逢紐曼電腦架構](https://hackmd.io/YfbDHi5pRVWlcmcQ1kKQVw)
![](image/HJt6-piZp.png)
![](image/S1YaZps-T.png)

隨著功率、指令級並行性和記憶體延遲被限制
#### wafer
![](image/H1Oi7pi-p.png)
$Cost\ Per\ Dies=Cost\ Per\ Wafer/Dies\ Per\ Wafer\times Yelid$

$Dies\ Per\ Wafer≓Wafer\ Area/Dies\ Area$

$Yelid =1/(1+Defect\ Per\ Area×Dies\ Area)^N$\
通常N各家晶片廠自定義,like 三星為130
### SOFTWARE
![](image/rJzp7pjbp.png)

#### system software

window and linux kernel and so on 

###### 四大os管理
1. CPU
2. main MEMORY
3. DEVICE
4. INFORMATION

#### function Marco

- fuctoin :  \
    it need to return address, so it will cost more tme

- Marco : \
    it will insert data into stack , so it did't need return address,but it will cost many space


#### compiler
| ---- | exe              | immediate                       | 直接執行 |
| ---- | ---------------- | ------------------------------- | -------- |
| pros | 執行速度快       | 只要有中間檔(&java庫)就可以執行 |    只要有程式碼就能執行      |
| cons | 換台電腦就不能用 |                 比exe慢                |    跑到才會出錯，比im更慢，會野外露出程式碼   |
| 舉例 |     C&C++             |     java                            |  python、ruby        |
#### from code to execute
![](image/BkR8ETibp.png)

### cloud system
#### [SIP](/BrG766-wQt6feIWi-3hfug)
#### [四種部屬雲](/aqnyVtnyTu-m3vCcXOBJLQ)
#### 五大功能
-  按需求自助服務(On-Demand Self-Service) 
	- 消費者可據需求自己來
-  普遍的網路存取(Broad Network Access) 
	- 不受限制的通過網路使用服務
-  資源彙整(Resource Pooling)
	- 務供應者透過多重租賃模式服務消費者，可依據消費者要求 指派實體及虛擬資源
	- 消費者通常無法確知資源所在地點。
- 高度彈性(Rapid Elasticity)
	- 因應消費者要求隨時且快速地調整資源規模
- 可計算的服務(Measured Service)
	- 自動控制、最佳化與量測各類服務資源
#### 八大特色
-  大規模的可伸縮性(Massive Scale) 
	- 因為有巨大的資源，所以可以為所欲為
-  可修復能力(Resilience) 
	- 因為不會只有1台sever而且一定會有備份
-  同質性(Homogeneity) 
	- 系統中的各個組件或節點在硬體和軟體上具有相似性，這有助於簡化管理和維護
	- 把異質性的設備轉成同質性的虛擬资源
-  廣泛的地理分布 
	- 如題
-  虛擬化(Virtualization)
	- 使用虛擬化技術，將硬體資源（例如伺服器、儲存和網路）抽象化，從而實現更高的資源利用率和靈活性。
-  服務導向特性(Service Oriented) 
	- 系統被設計成由多個獨立的服務組成，這些服務可以相互協作，以實現特定的功能或目標。
-  低費用(Low Cost) 
	- 指優化成本，以確保系統的運營和維護不會造成過高的開支。
-  先進的安全措施(advanced security)
	- 指系統具有強化的安全功能，以保護資訊和資源免受潛在的風險和威脅。
## Seven great ideas in computer organization 
- Use abstraction to simplify design 
	- 抽象使用多個級別，每個級別隱藏 低於它的級別。 例如：
		- 處理器的指令集隱藏了活動的細節 參與執行指令。
		- 高級語言隱藏了指令序列的細節 需要完成一項任務。
		- 操作系統隱藏了處理輸入和 輸出設備。
-  Make the common case fast 
	- 對common case 做加速
- Performance via parallelism 
	- process and thread
- Performance via pipelining 
	-  一旦指令的第一個活動完成，您就可以將其移動到 第二個活動啟動新活動的第一個活動 指令。
	- 分工(專業化?)
- Performance via prediction
	- 根據條件測試執行的下一條指令。
- Hierarchy of memories
	- 多分層的
- Dependability via redundancy
	- 透過冗餘實現備份


## How to evaluate the performance of a computer performance


### Concept of multiple criteria
因為電腦是一種由多種零件組合起來的集合，所以不能只用單一的標準去判斷電腦的好壞


####  Five criteria of Performance of hardware
1. Response time
    - 回應時間  
    - 個人電腦尤為在意
2. Throughput
    - Server 會很在意
3. Performance
    - Performance = 1/Execution Time 
4. related Performance
    -  A is 3 times faster than B
        - A'excution time × 3 = B'excution time
        - A'performance / 3 = B'performance
5. CPU rate
    - 單位(次/秒)
    - 3.xHz \
![](image/BJEYHF3bT.png)


#### Five criteria of Performance of software
1. Elapsed time
    - 使用者時間
2.  CPU time
    - code 在 cpu 上執行的時間
    - $Cpu\ Time=Cpu\ Clock\ Cycle\times Cpu\ Cycle\ Times$
        - Cputime ( Sec ) 
        - CpuClockCycle ( Times )  
            - 一次執行所需的時脈數
        - CpuCycleTimes ( Sec/Times )
            - 一次Cycle的時間 ( 週期 )
    - $Cpu\ Time=\frac{Cpu\ Clock\ Cycle} {Cycle\ Rate}$
        - CycleRate ( Times/Sec )
            - 一秒幾個Cycle( 頻率 or 時脈 )
3. CPI(cycle per instruction)
    - 每個instruction平均有多少週期
    - $CPI=Cp\ Clock\ Cycle/Instruction\ Num$
        - InstructionNum(次數)
            - Instruction 的數量
        - CPI(次數/次數)
    - if all CPI is the smae
        - $Cpu\ Clock\ Cycle=Instruction\ Num\times CPI$
        - $Cpu\ Time= Instruction\ Num\times CPI\times Cpu\ Cycle\ Times$
        - ex:你所撰寫的程式在JAVA n上，執行時間需要約15秒。
                又今天JAVA官方發表最新的JAVA n+1，且已知你的程
                式由JAVA n+1 編譯出來的指令數只要JAVA n的0.6倍，
                但其CPI會提高到1.1倍，請問你的程式在新編譯器中
                的執行時間初估為幾秒呢?  
                Ans = 15⨯1.1⨯0.6=9.9(sec)
    - if not
        - $Cpu\ Clock\ Cycle= \varSigma (Instruction\ Num_n\times CPI_n)$
        - $average(CPI)= \varSigma (CPI_n \times\frac {Instruction\ Num_n} {sum\ of\ Instruction \ Num})=\frac {Cpu\ Clock\ Cycle}{sum\ of\ Instruction \ Num}$
        - 用權重平均的方式理解
        - 其實不用背啦
        - ex : if here has two program
        
        | instruction | a   | b   | c   |
        | ----------- |:--- |:--- | --- |
        | cpi         | 1   | 2   | 3   |
        
        | program | a   | b   | c   |
        | ------- |:--- |:--- | --- |
        | A       | 1   | 1   | 1   |
        | B       | 1   | 2   | 5   |
        
        | ans      | A           | B              |
        | -------- | ----------- | -------------- |
        | cycle    | 1+2+3=6     | 1⨯1+2⨯2+3⨯5=20 |
        | Avg(CPI) | 6/(1+1+1)=2 | 20/(1+2+5)=2.5 |
        
    - **Influencing Factors**
        - Instruction Count for a program(指令數)
            - 程式
            - ISA(指令庫)
                - 不同ISA其中與硬體溝通方式會不同(cycle會不同)
            - 編譯器
        - Average cycles per instruction(指令平均週期or 指令平均時脈數)
            - 硬體
            - 不同指令不同CPI
                - 因此Avg(CPI)會嚴重受使用的所有指令影響
4. 硬碟的I/O次數
    - 根據I/O的使用次數與使用方式會影響程式表現,[硬碟詳細內容介紹](/硬碟HDD.md)
        |儲存型態|link list |arr|
        |-|:-|:-|
        |優點| 可隨時變換長度及型態|根據硬碟型態 可以有較快的讀取速度 |
        |缺點| 根據硬碟型態 不會有較快的讀取速度|不可隨時變換長度及型態 |

5. 時間複雜度
    - algorthim
6. if 你是個資工系學生 ,how to improve cpu time
    
    |      東東\Cpu Time Factor      | 指令数 | CPI | 時脈速率 |
    |:------------------------------:|:------:|:--- |:--------:|
    |           alogorithm           |   ✔️   | ✔️  |    ✖️    |
    |            資料結構            |   ✔️   | ✔️  |    ✖️    |
    |         program design         |   ✔️   | ✔️  |    ✖️    |
    |            complier            |   ✔️   | ✔️  |    ✖️    |
    | [ISA](/ISA.md) |   ✔️   | ✔️  |    ✔️    |
    |              計組              |   ✖️   | ✔️  |    ✔️    |
    |          VLSI(純硬體)          |   ✖️   | ✖️  |    ✔️    |
    
#### exapand-[turbo mode](/turbo%20mode.md) 
渦輪模式 : 在 CPU 運算量高時讓 CPO 時脈短暫开高10 %,
直到 CPO 過熱為止
### The power wall (能耗牆)
- why 考慮耗能 ?
    - 時脈提升已到極限
    - 近期PMD(Personal Mobile Device)發展迅速，因此會需要減少能耗
    - 無法解決的散熱問題(液氮超频)
    - MOSFET 結構的能耗 
         
        ![](image/SyvpWBp-p.png)
        動態耗能: 
            由於電橋本身具有電阻，產生能耗\
        靜態能耗:
            由於mosfet本身結構(中間電橋),在靜止狀態下容易產生電中和，因此會產生能耗
        
    - for 動態耗能
        - $Power=\frac 12Capacitive\ load\times Voltage^2\times Frequency$
    - 目前靜態漏電佔總耗能40% →通過材料學解決


### Fallacies and pitfalls(謬誤與陷阱)
-  [Amdahl’s Law](/Amdahl’s%20Law.md)(經驗法則)

    - $P_{new}=\frac{P_{part\ of \ affect}}{times\ of\ improve}+P_{part\ of \ not\ affect}$ 
        - example : \
            程式在電腦上執行需要100秒，且乘法耗費其中的80秒，請問該如何改善乘法的速度讓他跑5倍快? \
            ans : $\frac {100}{5}=20 \neq \frac{80}{X} +20$ \
            其中X為改善倍率 ,因此X→$\infty$\
            ⇒不可能改善
    - so make the common case fast is better

- Computers at low utilization use little power
    - is it a joke?

- Using a subset of the performance equation as a performance metric MIPS as a Performance Metric?
    - MIPS: Millions of Instructions Per Second
        - Didn't consider  
            - ISAs between computers
            - Instruction program
            - complexity between instructions
        - $\large{MIPs \\= \frac {Instruction\ Count}{Excution\ 
            time_{(sec)}\times 10^6}
            \\= \frac {Instruction\ Count}{\frac{Instructio \ count\times CPI}{Clock Rate}\ \times\  10^6}
            \\=\frac{Clock \ Rate }{CPI\times 10^6}}$
