---
tags:
  - 密碼學
---
## 6.2.1 Feistel 回合
![[Pasted image 20240501142911.png]]
> 下圖為DES core 

![[Pasted image 20240501143021.png]]

> Expansoin p box

![[Pasted image 20240501143330.png]]

32 -> 32/4 共有 8 組 每組有兩個擴充 ->  32 + 8\*2 = 48  

>漂白器（XOR） 
- 在擴展排列之後，DES 將擴展的右半部分與回合金鑰進行 XOR 運算 
- 注意右半部與金鑰長度均為 48 位元，而且回合金鑰僅使用在這 個運算上

> S box

![[Pasted image 20240501143646.png]]

![[Pasted image 20240501143737.png]]

## pseudocode for DES 
![[Pasted image 20240501144804.png]]

![[Pasted image 20240501144836.png]]

![[Pasted image 20240501144856.png]]

![[Pasted image 20240501144907.png]]
### round key Generator
原始金鑰有64位元，但其中有8為用於錯誤校正(奇偶校正，每組第八位)
![[Pasted image 20240501145606.png]]
