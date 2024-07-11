---
title: SaaS
tags: ['#計組']

---


# SAAS Simple Maturity Model
- L1： customized 
- L2： configured
- L3： configurable,muti-Tenant-Efficient
- L4：configurable, muti-Tenant-Efficient,Scale

### L1
- 把不同單租戶軟體放到同一個托管平台(only 提供硬體)上執行
- 不同電腦，不同軟體

![](B1nT5GpWp.png)


### L2
- 把相同的單租戶軟體的多個實例分別執行服務不同的使用者， 大型機的多租戶服務屬於這一類。
- 相同軟體，不同電腦

 ![](ByqAqfa-6.png)

 ### L3 
- 多租戶軟體，一個執行實例，服務多個使用者，郵件系統屬 於這一類
- 相同電腦，相同軟體

![](SkmkoMaZa.png)

### L4
- 一個多租戶軟體，可伸縮的多個執行實 例，服務大批量使用者。
- 相同電腦，相同軟體，但是有loader可以平衡流量
 ![](H1lljMTZ6.png)

 