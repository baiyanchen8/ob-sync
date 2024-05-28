---
title: CHAP1  For OS
tags: [os]

---

# CHAP1 Introduction For Operation System
## Computer System Structure
---
* 現代計算機可以分為四個主要部分
    * hareware
    * os(operation system)
    * 系統與應用程式 (system and application programs)
    * user 
    ![Untitled (4)](H1vEDKcQ6.png)

## What is Operating System ?
---
### **define**
* [wiki](https://zh.wikipedia.org/zh-tw/%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F)

    作業系統（英語：Operating System，縮寫：OS）是一組<font color="ffff">主管並控制電腦操作、運用和執行硬體、軟體資源和提供公共服務來組織使用者互動的相互關聯的系統**軟體**程式</font>，同時也是電腦系統的核心與基石。作業系統需要處理如管理與組態記憶體、決定系統資源供需的優先次序、控制輸入與輸出裝置、操作網路與管理檔案系統等基本事務。作業系統也提供一個讓使用者與系統互動的操作介面。

* from 張軒彬
    - A **software** act between users/application and hardware
    - goal: 
        - manages computer hardware
        - provide an envirnment for applicationn  programs to run
- **another define**
    - Operating System is the one program running at all times on the computer
    - it is often to descript kernel

>Ｑ： 如果沒有作業系統，會怎樣?

>Ａ： 總之就是電腦不能動了

>Ｑ： 為什麼要學習作業系統?
>Ａ： 因為不管你為來是從業哪裡，只要是電腦相關產業都需要對運行著眾多程序的os有所了解
## Computer Structure

### 電腦硬體介紹
![image.png](S1c37Ov7T.png)
- [[cpu]]
    - 處理器
    - 現代電腦皆採[[馮紐曼]]
- bus (匯流排)
    - 可以簡單理解為數據線
- memory
    ![Untitled (5)](r1j0Oo9mp.png)
    - 分類1(性質分類)
        - Volatile Memory(揮發性記憶體)
            - 揮發性記憶體是一種計算機儲存設備，其特點是當電源關閉或設備關閉時，其中存儲的數據會丟失。
        - nonVolatile Memory(非揮發性記憶體)
            - 非揮發性記憶體是一種計算機儲存設備，其特點是數據在電源關閉或設備關閉時仍然保留。
    - 分類2(結構分類)
        - 機械式記憶體
            - HDD、磁帶...
        - 電子式記憶體
            - Flash(閃存)、SDD...
    
### i/o structure
作業系統大部分都是在處理i/o，因為這跟系統穩定性有很大關係
- [[DMA]]

## Computer System Architecture(電腦系統架構)
根據處理器的分配做分類
### 計算機系統組件定義

- cpu : 執行指令的硬體(genal propose)
- processor : 一個實體 chip 中包含多個cpu(至少1)(經常與cpu混用)
- core : cpu 的單位

### Single Processor System
就一顆Processor，很少見
### Multi Processor System
多處理器有兩種類別：

- **非對稱多元處理 ( asymmetric multiprocessing )**
    - 存在 master-slave 關係 ⇒ 角色不對稱
    - 一個主處理器控制系統，其他從處理器完成主處理器的指令
    - 容易因主處理器觸發bottleneck
- **對稱多元處理 ( symmetric multiprocessing / SMP )**
    - 所有處理器都同等，執行所有任務
    - 因為 CPU 之間是獨立的，所以要互相協調 process 和 resource 在處理器之間動態的共用 ⇒ 避免分配不均造成效能減低


### Multi Core System
一個chip中有多個cpu


### UMA vs NUMA(統一記憶體存取與非統一記憶體訪問)

- UMA(統一記憶體存取)
    - 指所有的物理記憶體被均勻共享，即處理器訪問它們的時間是一樣的。
    - 簡單來說就是共用全部的記憶體
    - 缺點:
        - 由於是共用全部，bus也會互相共用，但就會更容易引發i/o bottleneck
- NUMA(非統一記憶體訪問)
    - 使每個cpu有自己的較近的memory
    - 每個cpu自身的memory使用完之後，才會向其他cpu界記憶體
    - 缺點:
        - 由於memory分遠近，所以會造成額外的overhead(開銷)
### 刀鋒伺服器 (blade server)
### 叢集式系統 (clustered ststem)
透過網路(local/wide network)將多個節點(node)鏈接在一起的方式，使其共享資源，被認為是鬆散耦合(loosely coupled)。
推薦看[wiki](https://zh.wikipedia.org/zh-tw/%E8%AE%A1%E7%AE%97%E6%9C%BA%E9%9B%86%E7%BE%A4)其中有詳細描述
- 優點
    - high avaliablity service(高可用率) 
    - fault tolerant(容錯)
    - graceful degradation(優雅降級)
        - 指的是在部分主機 shut down 時，整個系統的效能並不會斷層式下降
        ![image](SyGEVns7T.png)

    
- 分類
    - 對稱性
        - 所有節點通過管理做相同的工作
    - 非對稱性
        - master-slave
- 舉例
    - p2p 
    - hadoop [參考網址](https://zh.wikipedia.org/wiki/Apache_Hadoop)
    - Mapreduce [參考網址](https://zh.wikipedia.org/zh-tw/MapReduce)
## Operation System Structure

### os 大前提--- Event driven

![image.png](S1c37Ov7T.png)
<!-- 不會看圖嘔??-->
 Event driven 
"Event driven"（事件驅動）是一種軟體架構或程式設計範式，它強調系統的反應和行為取決於發生的事件。在這種模式下，**程式執行的動作是對於事件的觸發而發生的**，而不是持續地進行某些操作。這種架構常見於許多應用程式和系統中，如用戶介面開發、即時資訊處理等領域。


>Ｑ：cpu 如何通知device
>Ａ：利用讀取每個device中的register

>Ｑ：device 如何通知 cpu
>Ａ：透過interrupt

### Trap(軟體中斷)
- system call
- Error
### Interrupt(硬體中斷)

1. 硬體可以隨時藉由發送訊號至cpu，通知cpu硬體的某項活動，而由於這個訊號會使cpu暫停目前工作處理，因此稱為中斷(interrupt)
2.  分類
    - maskable
        - 可屏蔽中斷是指可以被系統中斷控制器或中央處理器（CPU）屏蔽或禁用的中斷。
    - nonmaskable
        - 不可屏蔽中斷是指無法被屏蔽或禁用的中斷，它們通常具有較高的優先級，並不受中斷屏蔽設置的影響。
3. 存儲結構(中斷向量/interrupt vector)
    - 中斷向量（Interrupt vector）是中斷服務程式的入口位址，或中斷向量表（它是一個中斷處理程式位址的陣列）的表項。
    - 系統程式必須維護一份中斷向量表，<font color="ffff">每一個表項紀錄一個中斷處理程式(ISR)的位址</font>
    - interrupt vector table 
        - 0~31為nonmaskable (intel)
        - 32~255為maskable (intel)

     interrupt vector table(其實不用看)
     
| IVT Offset | INT #     | Description                       |
| ---------- | --------- | --------------------------------- |
| 0x0000     | 0x00      | Divide by 0                       |
| 0x0004     | 0x01      | Reserved                          |
| 0x0008     | 0x02      | NMI Interrupt                     |
| 0x000C     | 0x03      | Breakpoint (INT3)                 |
| 0x0010     | 0x04      | Overflow (INTO)                   |
| 0x0014     | 0x05      | Bounds range exceeded (BOUND)     |
| 0x0018     | 0x06      | Invalid opcode (UD2)              |
| 0x001C     | 0x07      | Device not available (WAIT/FWAIT) |
| 0x0020     | 0x08      | Double fault                      |
| 0x0024     | 0x09      | Coprocessor segment overrun       |
| 0x0028     | 0x0A      | Invalid TSS                       |
| 0x002C     | 0x0B      | Segment not present               |
| 0x0030     | 0x0C      | Stack-segment fault               |
| 0x0034     | 0x0D      | General protection fault          |
| 0x0038     | 0x0E      | Page fault                        |
| 0x003C     | 0x0F      | Reserved                          |
| 0x0040     | 0x10      | x87 FPU error                     |
| 0x0044     | 0x11      | Alignment check                   |
| 0x0048     | 0x12      | Machine check                     |
| 0x004C     | 0x13      | SIMD Floating-Point Exception     |
| 0x00xx     | 0x14-0x1F | Reserved                          |
|0x0xxx     | 0x20-0xFF | User definable
    


4. ISR (Interrupt Service/handler Routine )
    - ISR (Interrupt Service Routine) 是一個在計算機系統中用來處理中斷事件的特殊軟體程序。

5. 流程圖:
    ```mermaid
    %%{init: {'theme':'dark'}}%%
    graph LR;
    a[prcoess A]-->b[save A'regs]-->c[ISR]-->d[restore A'resg]-->e[process A]
    ```
    >Ｑ：為什麼在作ISR時，不用存取ISR的regs
    >Ａ：因為ISR每次都會執行完整的行程。
### multi tasking and multi programing
作業系統一個重要能力是能夠執行多元程式，因為通常一個程式沒有辦法最大化cpu性能，所以需要並行的技術。
- multi programing
    - 目的是藉由使cpu始終有process執行中，以讓cpu使用率提升
    - process 
        - 指正在執行的程式
- multi tasking(time sharing)
    - 為multi programing 的延伸
    - cpu通過在多個process多次之間切換，以提升響應速度(reponse time)
    - need cpu scheduling in [[chap 5 for os]]
    - 為了達到這一效果，很常會使用到一技術--[[虛擬記憶體]]
### Dual mode and Multi mode
由於作業系統要確保不會有錯誤(或惡意)程式，使其他程式無法執行，故需要用多種模式去限制能使用的物件(or 指令)。
![](image/dualmode.png?raw=true)
### Timer
- 通常由晶振體組成
- 使用inerrupt

## protection and security
- protection
    - 是一種行程控制或使用者存取電腦資源的一種限制
- security
    - 防止來自電腦內部或外部的攻擊


