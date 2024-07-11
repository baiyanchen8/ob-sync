---
title: DMA
tags: [os]

---

# DMA

- **直接記憶體存取 ( Direct Memory Access / DMA )**
    
    對於少量的資料來說，Interrupt 很有用，但如果是大量的資料移動 ( EX：NVS I/O )，一直要 CPU 親自處理，負擔就很重
    
    DMA 可以解決這個問題，資料在移動過程不需要觸發 Interrupt，也不需要經過 CPU，而是由 **DMA controller** 將整個資料區段從 locol buffer 直接傳給記憶體，每一個區段 Interrupt 一次就好
    
    這樣的好處就是，CPU 可以去完成其他程序，不會一直被中斷，並且提高資料傳輸速度