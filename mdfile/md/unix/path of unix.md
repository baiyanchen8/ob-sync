---
title: path of unix
tags: [unix]

---

# path of unix

## intro
this page is going to explain <font color="ffff">unix path contrustion</font>

## First
---
我先介紹一個好用的command幫助你了解unix目錄層級(根據系統或版本不同會有些差異，這裡只介紹個大概)

> 
- **command:** tree
- **intro:** 需要透過apt安裝
	- sudo apt install tree
	
![image.png](r1TCLX9mT.png)

| direction | usual meaning                                                    |
| --------- | ---------------------------------------------------------------- |
| /         | root 根目錄                                                      |
| /bin      | 通常適用於存放系統指令                                           |
| /boot     | 通常存放驅動                                                     |
| /dev      | 必要裝置, 例如：/dev/null.                                       |
| /media    | 可移除媒體(如CD-ROM)的掛載點 (在FHS-2.3中出現)。                 |
| /home     | 使用者的家目錄，包含儲存的檔案、個人設定等，一般為單獨的分割區。 |
| /tmp      | 臨時檔案(參見 /var/tmp)，在系統重新啟動時目錄中檔案不會被保留。  |


