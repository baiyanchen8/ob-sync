# TCP Services
The services offered by TCP to the processes at the application layer.
## Process-to-Process Communication
- TCP provides process-to-process communication using port numbers
## Stream Delivery Service
- TCP delivers/receives data as a stream of bytes
- TCP提供給上層的服務目標: 資料好像經由一個虛擬的水管(bytes管)抵達接收端
  
  ![[Pasted image 20250612134108.png]]
  ![[Pasted image 20250612134211.png]]

## Connection-Oriented Service
- TCP is a connection-oriented protocol
- However, the connection is virtual, not a physical connection
- In fact, each TCP segment may use a different path to reach the destination
![[Pasted image 20250612134512.png]]
## Reliable Service
- TCP is a reliable protocol
- Question: How to provide reliable services? 
- Ans: by error control (shown later)
## Full-Duplex Service(!Skip)
## Multiplexing and Demultiplexing(!Skip)
## Encapsulation and De-capsulation(!Skip)
# TCP Features
- TCP has several features to provide the services mentioned in the previous section 

![[Pasted image 20250612135604.png]]
![[Pasted image 20250612135615.png]]
![[Pasted image 20250612135623.png]]![[Pasted image 20250612135642.png]]
## Flow Control
![[Pasted image 20250612140519.png]]

## Error Control
![[Pasted image 20250612140749.png]]
## Congestion Control(show later)
- Why congestion?
	- A router/switch has queues that store the incoming packets.
- Why congestion?
	- If packet arrival rate > packet processing rate, queue become overloaded and congestion occurs.

## Numbering System
- TCP implement a numbering (編號) system.
	- 對傳送的資料編號
- Although TCP use segments for transmission and reception
	- However, TCP does not have segment number 
- Instead, TCP **numbers all data bytes** that are transmitted in a connection
- Why use Byte num 而非 Segment Num
	- 因為這樣可以提供 byte level Service(更加彈性)
	- ex : if datagram 中第三個 byte 的內容發生錯誤，可以只將該 byte 重傳
	- Service
		- Byte-oriented flow control
		- Byte-oriented error control
		- Byte-oriented congestion control
![[Pasted image 20250612144424.png]]
### Acknowledgment Number 
- the number of the next byte that the party expects to receive
- Acknowledgment number is cumulative(累進，增加)
- For example, if a party uses 5,643 as an acknowledgment number
	- It has received all bytes from the beginning up to 5,642
	- Note that, this does not mean that the party has received 5642 bytes
	- The first byte number does not have to start from 0 
![[Pasted image 20250612151047.png]]
### Summary
![[Pasted image 20250612151359.png]]
# Flow Control
> [!question]- Question: ,如果Source送太快, Destination收很慢會發生什麼事呢? 
> Ans: Destination會來不及處理而掉封包

>[!question]- 如何解決
> 答：流量控制平衡來源建立資料的速率與目的地使用資料的速率。

> [!question]- Question: 那Source如何知道可以送多快並且Destination不會掉封包呢?
> Ans: Destination直接告知Source就好了

> [!question]- Question: 那Destination如何告知Source?
> Hint: 藉由某個封包的某個欄位
Ans: Destination回ACK封包的Receiver Window Size(**rwnd**)欄位 (rwnd如何決定以後會介紹)

- The destination controls(**由目的地決定**) how much data are to be sent by the sender
- The numbering system allow TCP to use a **byte-oriented flow control**

## Sender Buffer & Receiving Buffer 
- The sending and receiving speed may not be the same
	- TCP needs buffers for buffering
- Two buffers in TCP
	- Sending buffer and receiving buffer
	- Also used in flow- control and error-control mechanisms
![[Pasted image 20250612152530.png]]
### Send Buffer
- The sending circular buffer has three types of sections
	- 白色區域: empty location
		- Can be filled by the sending process
	- 淺藍色區域: hold bytes that have been sent but not yet acknowledged 
		- TCP keeps these bytes until it receives acknowledges	
		- why已經送過了還不清除
			- 因為還未收到 ack ,要確保 if 需要重傳
	- 粉紅色區域: bytes to be sent by the sending TCP
		- TCP may be able to send only part of this colored section
		- 針對粉紅色區域的資料, 為什麼只送一部分呢?
			-  flow control and congestion control
### Recv Buffer
- The receiving circular buffer is divided into two areas
	- White area: 
		- Empty locations to be filled 
	- Colored area: 
		- Contain received bytes that can be consumed by the receiving process

> [!question]- Question: 如上圖, Destination回ACK時, rwnd可以填多少?
> 白色部分(=15)Rwnd的值就是這麼決定的!!! 
> ![[chap15 Transmission Control Protocol (TCP) 2025-06-12 15.32.38.excalidraw|>700]]

![[Pasted image 20250612153634.png]]![[Pasted image 20250612154019.png]]


## Sliding Window Protocol
🪟 什麼是 TCP 的「Sliding Window」？
TCP 使用 **滑動視窗（Sliding Window）協定** 來做 **Flow Control（流量控制）**，目的是：
> 控制傳送方不要傳太快，以免接收方來不及處理，造成資料遺失或塞車。

✅ 基本觀念：
- **視窗（Window）** 是一個「範圍」，代表：
    > 傳送方在「未收到接收方 ACK 前」，**最多可以送出多少資料（byte）**
- TCP 的視窗是根據：
    - **接收方的 buffer 容量**
    - **當前的 ACK 狀態**
    - → 動態變化的！
## Window Shutdown
在某些情況下，接收方暫時不想接收發送方的任何資料。
接收方會暫時關閉視窗。
發送一個 rwnd = 0 的 ACK 封包段。
發送方會停止發送，直到收到新的廣播。
## Summary
- Flow control regulates the amount of data a source can send before receiving an acknowledgment from the destination. 
- TCP uses sliding window protocol
	- The sender window size is controlled by the receiver window value (rwnd)
# Error Control
> [!question]- Question: 有哪些錯誤呢?
> corrupt, lost, duplicated, and out-of-order
'
## checksum 
TCP uses 16-bit checksum to detect **corrupt** segments
## Acknowledgment
- Acknowledgment in TCP
	- Accumulative Acknowledgment (ACK)
	- If ACK number = 1000, **代表999(含)之前全部都收到**
- Selective Acknowledgment (SACK)
	- Newly added feature
	- Shown later
- Sol. 1: 每收到一個data segment就回ACK封包
	- ACK封包太頻繁
	- 尤其ACK封包是overhead
- Sol. 2: Delayed ACK, 當收到一個data segment時等一下
	- 看有沒有要回送data segment?如果有, piggyback ACK封包
	- 看有沒有又收到data segment?如果有, 回ACK(一個ACK回兩個data segments) (shown later)	
![[Pasted image 20250612213617.png]]

1. When one end sends a data segment 
	- It must piggyback an acknowledgment (see the next slide)
	- 它必須搭載一個確認（請參閱下一張投影片） 
	- Decrease the number of ACK segments
	- 減少 ACK 段的數量
2. The receiver delays sending an ACK 
	- When the following three conditions hold
		- 沒有要送的資料,recveiver has no data to send
		- 收到的是「順序正確」的資料
		- 前一段資料已經 ACK 過了
			- if recv id=4 ,id=3 已經 send ack 可以直接送 4
	- The receiver delays sending an ACK
		- Until another segment arrives or
		- Until a period of time (normally 500 ms) has passed
	- Thus, if only one outstanding in-order segment
		- Delaying sending an ACK
	- Prevent ACK segments from creating extra traffic
3. The receiver immediately sends an ACK(立即傳送 ack)
	1. When the following two conditions hold
		- An in-order segment arrives
		- The previous in-order segment has not been acknowledged
	2. Thus, there should not be more than two in-order unacknowledged segment at any time
		- 任何時候都不應該有 2 個之上未 ack 的 segment
	3. Prevent unnecessary retransmission
4. When an out-of-order segment with higher sequence number is received, the receiver immediately sends an ACK
	- Enable fast retransmission of any missing segment
	- if 上一個 ack= 12(即我收到 sequence num=11) 但我收到 sequence number = 14 我要立即啟用 ack=12 送給sender
5.  When a missing segment arrives, the receiver sends an ACK
	- Inform the sender that segments reported missing have been received
	- 當丟失封包重新收到 發送 ack
6. The receiver immediately sends an ACK if a duplicate segment arrives
	- Solve some problems when an ACK segment itself is lost

## Re-transmission
- Sender TCP starts a retransmission time-out (RTO) timer for each segment sent
- If timer matures
	- Retransmit the segment
  
1. ✅ Sender 傳出一個 segment（假設 seq = 1000）
2. ⏲ 啟動 RTO 計時器（例如預設是 1 秒）
3. 📬 若在 RTO 到期前收到 ACK → ✅ 計時器關掉
4. ❌ 若 **沒有收到 ACK** → ⏱ 計時器到期 → 🔁 重傳該 segment
### Fast re-transmission
|條件|說明|
|---|---|
|❗ 收到 **3 個以上相同的 ACK**|例如連續收到 ACK = 1040 三次|
|✅ 沒有啟動 RTO timeout|不必等時間到，提早反應|
## 範例演示
###  Normal operation

![[Pasted image 20250612235522.png]]

## Lost or corrupt(損失) segment
- 遺失或損壞的段將以相同的方式處理（都是被封包丟棄）。
	- 遺失的段：在網路中的某個位置被丟棄。
	- 損壞的段：被接收方自己丟棄。
- 在以下圖中，段 3 遺失。
	- 接收方收到一個亂序的段（ex:段 4）。
		- 將其暫時存儲。
		- 立即發送 ACK（ACK 編號 = 701）。
- 發送方在 RTO 計時器到期時重新傳送段 3。
 ![[Pasted image 20250613001725.png]]
## Out-of-order segment
- Previous slide also shows out-of-order segments
- TCP store out-of-order segments temporarily
	- Until the missing segment arrives
- Note
	- The out-of-order segment are not delivered to the process
	- TCP guarantees in-order delivery
## Fast retransmission
![[Pasted image 20250613004240.png]]
## Automatically corrected lost ACK
- A lost acknowledgment is automatically replaced by the next
	- Since ACK is accumulative
![[Pasted image 20250613004306.png]]
## Lost acknowledgment corrected by resending a segment
![[Pasted image 20250613004339.png]]
## Duplicate segment
在上例中，伺服器偵測到重複的段，由於它們具有相同的序號（501~600），丟棄後面的段

# Congestion Control
> [!question]- What is congestion?
> The load on the network is greater than the capacity of the network
---
>[!question]- Where is the congestion?
> The connecting devices(router switcher....)
---
> [!question]- What is congestion control?
> The mechanism and techniques to keep the load below the capacity

## Congestion window
![[Pasted image 20250613005100.png]]
## Congestion policy
>[!question]- 方法一:是否可以類似rwnd, 由connecting devices告知傳送端TCP?
> ans : 不行 , why ? 因為你不知道是哪個點雍堵
---
> [!question]- 那怎麼辦呢?
> Ans: 猜

### Slow start: exponential increase
一開始先從很小的值測試看看…
- At the beginning, 
	- Congestion window size = maximum segment size (MSS)
- Each time an ACK arrives
	- Increase the congestion window size by one MSS
	- Until it reaches a threshold, called ssthresh (slow start threshold)
		- Usually, ssthresh = 65535 bytes
- However, it is not actually “slow start”
	- The congestion window size increases exponentially
	- Start			=> cwnd = 1 = 2\^0
	- After 1 RTT		=> cwnd = 2 = 2\^1
	- After 2 RTT		=> cwnd = 4 = 2\^2
	- After 3 RTT		=> cwnd = 8 = 2\^3
	  
![[Pasted image 20250613013158.png]]

然而，在延遲確認的情況下，慢啟動速度會更慢。 記住，對於每個 ACK，cwnd 都會增加 1 個 MSS。 因此，如果兩段被累計確認，cwnd 只會增加 1。

### Congestion avoidance: additive increase(線性增加 cwnd)
>[!n] 可是不能一直指數增長, 所以當cwnd達到一定的大小之後, 就必須**慢慢增長**

擁塞視窗大小達到 ssthresh 閾值後開始
當整個視窗的分段被確認後
擁塞視窗大小增加一個
注意，在擁塞避免階段，整個視窗大小通常大於一個 MSS

### Congestion detection: multiplicative decrease
- 在兩種情況下，閾值 (ssthresh) 都是目前壅塞視窗大小的一半 (ssthresh = cwnd/2)。
	- 乘性遞減
- 但是，採取的操作不同
- 如果發生逾時：極有可能發生壅塞
	- ssthresh = cwnd/2
	- 擁塞視窗大小再次從 1 開始，即 cwnd = 1
	- 發送方返回慢啟動階段
- 如果收到三個重複的 ACK：擁塞可能性較小
	- 呼叫快速重傳
	- 呼叫快速恢復
	- ssthresh = cwnd/2
	- 擁塞視窗大小 = 閾值，即 cwnd = ssthresh
	- 發送方啟動擁塞避免階段
### TCP Congestion Policy Summary Summary
![[Pasted image 20250613020535.png]]
# TCP Segment

# A TCP Connection

# Options