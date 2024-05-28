---
title: chap 8 Deadlock
tags: [os]

---

# System Model
- Resources type : $R_1,R_2...$
	- CPU、Memory space、I/O、mute、semaphores...
	- 每個 Resources 有 $W_i$ 個實例
- $P_i$ Thread or Process
	- request edge : 請求資源
	- assignment edge : 分配資源

![image](S1MqaZaw6.png)

# Deadlock Characterization
- 4 大必要條件
	- mutual exclusive
	- hold and wait
	- No preemption
	- Circular wait
		- there exists a set {P0, P1, …, Pn} of waiting threads such that 
		- $P_0→P_1→P_2→P_3→P_0$

## Circlar Wait

![](S1MqaZaw6.png)
P2->R3->P3->R2->P2
P1->R1->P2->R3->P3->R2->P1
- fun fact
	- if circle
		- 不一定 deadlock
	- if deadlock
		- 一定 circle



# Deadlock Prevention
- Deadlock prevention
	- 確保4大條件個中至少一個不成立
## Mutual Exclusion 
- 無法透過拒絕此條件來防止 deadlock
	- 有些資源本身就是 Mutual Exclusion，例如印表機

## Hold and Wait 
- solution
	- 方法1（Hold and no wait）：每個執行緒請求並在執行前分配其所有資源
	- 方法2（Wait and no hold）：只有當執行緒沒有資源時，該執行緒才能請求資源。
		-	Method 1 (Hold and no wait): each thread request and be allocated all its resources before execution 
		- Method 2 (Wait and no hold): A thread can request resources only when the thread has none.
	
- Disadvantages
	- Low resource utilization 
	- Starvation possible
## No Preemption 
- Solution
	- make it preemption
- condition
	- 只有當資源可以方便儲存與復原時才可使用
	- 不能使用在 mutex and semaphores .etc

## Circular Wait 
- idea
	- 對所有資源做編號
- Solution 1
	- 每個 process 只能遞增的請求資源
	- if get $R_2$,請求 $R_1$
		- reject
-  Solution 2
	- 每個 process 只能遞增的請求資源
	- 如果請求比現有資源小的資源，擇要釋放比請求資源大的資源
		- 假如已經 $R_1、R_3$,請求 $R_1$
		- 釋放 $R_3$