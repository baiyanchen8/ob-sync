---
title: lec 2 note
tags: [密碼學]

---


# 整數算術
## 整除性
![image](S1axFNvxC.png)
![image](HJs-KNwlR.png)
![image](ry8HFEwgR.png)
![image](r1ccYEPgR.png)

### 歐幾里德演算法(輾轉相除法)(用於尋找最大公因數)
![image](By-ttVDlR.png)

```python=
def gcd(a,b):
    while (b>0):
        q= int(a/b)
        r= a%b # also equal a-b*q
        a=b
        b=r
    return a
```
### 歐幾里德延伸演算法
![image](SJg7sVvl0.png)
![image](rJpHhEDeC.png)

## 線性 Diophantine 方程式
![image](ryxd2qDgR.png)
![image](BJf939PlC.png)

# 模數運算

![image](SkX-RcvxR.png)

## 餘數集合
$Z_n$ 意謂在 mod n 的情況下，所有可能出現的餘數的集合

## 同餘 $\equiv$ 

$a\ mod\ d \equiv \ b \ mod \ d$

## 剩於類

$[a]_n$
即為所有 mod n 之後為 a 的數

## 反元素
### 乘法反元素
$a+b \equiv 0(mod \ n)$
#### 求解
![image](HJzzSjDl0.png)
![image](rJTvrjPgA.png)

### 加法反元素
$a\times b \equiv 0(mod \ n)$

![image](By7nrovlC.png)
![image](BJ32HjweA.png)

# 矩陣

![image](B1338oPg0.png)
![image](ByufwowlC.png)

## 行列式
$det(A)=\Sigma _{j=1...m}(-1)^{i+j} \times a_{ij}\times det(A_{ij})$ 
![image](r1y4_sDg0.png)
也可以用高中常用的對角線法

## 反矩陣

$AA^{-1}=I$

## 餘數矩陣
- 在密碼學上我們使用餘數矩陣：所有元素皆定義在 ���� 中的矩陣。
- 若 gcd(det(A), b) = 1，則該餘數矩陣具有乘法反矩陣。

![image](rksZknvxC.png)
