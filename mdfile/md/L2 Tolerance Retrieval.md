---
title: L2 Tolerance Retrieval

---

# L2 Tolerance Retrieval

## 使用的 index 搜尋
在關鍵字進來時，要怎麼將關鍵字與其所在Dictionary位做相連
![image](image/r1cKq176p.png)

1. Hash
    - 缺點
        - 因為無法做相近字搜尋，所以 google 不太使用這種方法
2. Dictionary Tree (goolge choose)
    1. mon\*
        建立一顆順序的tree
    2. \*mon
        建立一顆反序的tree
    3. mon\*mon
        順序做一次&反序作一次，做交集
    4. \*mon\*
        解法 : K-Gram index

## K-gram index
1. 將text切割為 k-gram(連續k個字元)的字串ex: month,k=2 => \{\$m,mo,on,nt,th,h\$\}
2. 建立一個list table，用於保存所有包含k-gram的所有單字
    >  example
    ![image](image/BknHblXaT.png)
    
3. 從 table 中將符合的片段取出，並且對所有結果取聯集後確保所有結果都符合原本的條件
    > 
    ![image](image/B1QXel7TT.png)
    

## Spelling correction 

#### 目的

使用者打錯字，該幹啥?

### 錯誤情境

1. 打錯字 ex :  apole $\Rightarrow$ apple
2. 語意錯誤 ex : i *form* Canada  $\Rightarrow$ i *from* Canada

### fix 1 (打錯字)
***Similar 相近***
假設我有一個字典要怎麼搜尋相近的字
1. Edit Distance
    >  說明
    要替換的次數，like cat & dog 的距離為 3、abc & ac 為 1
    
    假設 $S_1$ 長度 m & $S_2$ 長度 n & 字典大小為 M，$S_2$為從字典取出與$S_1$比較的某個字
    單次時間複雜度: O(m$\times$n)
    總時間複雜度: O(m$\times$n$\times$ M)
    
    *BUT!!* 因為要跟字典中的所有字比較 $\Rightarrow$ 成本很高
    
2. K-gram method
    >  說明
    透過 k-gram method 把字拆分為多個字根，然後比較其中的字根比例來計算相似度
    
    Jaccard Coefficient:$\frac{A\cup B}{A\cap B}$
    假設 $S_1$ 長度 m & $S_2$ 長度 n & 字典大小為 M，$S_2$為從字典取出與$S_1$比較的某個字
    單次時間複雜度 : O(m+n) 
    總時間複雜度: O((m+n)$\times$M)
    
    

**BUT** 問題是 Dictionary 太大

so 解法就是先對搜尋字做 k-gram，將其中的字根抓出，再去 k-gram table 中把該字根的 List 取出，以那些List 做比較最為方便

![image](image/Sk8fAl7aT.png)

### fix 2 (語意錯誤)

***STEP***
1. 抓出錯誤語義的字
2. 抓出替換字(使用similar算法即可)

## Soundex Algorithm
- 透過將相近的字母轉換為符號，可以將單字做編碼
- 編碼方式
    - 抓開頭，去母音，轉編碼，補0
![image](image/S1K0sZmTp.png)

## Spelling correction -- Context Sensitive

> 問題 ：如何找語意出錯的 ＆ 如何找出正確該替換的字


> 暴力作法 ：通過尋找替代字，然後將所有 word 做反向索引，然後找最多的組合？
> 其實這裡我也不懂

## Growth about website

> 網站與單字量不斷上升，導致google 的儲存成本不斷上升

### heap's law 
> 一種經驗法則，用於描述文檔數量與詞彙數量的關係

- $M=kT^b$
    - M 為單字量
    - T 為文件數量
    - k & b 為常數 (30<k<100,0.4<b<0.6 通常) 

### 需要儲存的內容
1. 文檔本身的 index 
    ![image](image/BJzYCgeWR.png)
3. 建立invert index 的空間(posting list)
    ![image](image/HJUc0xeb0.png)

>  example
假設文檔有 600 billion (= 600,000,000,000)
文檔 id 就要有 $log_2(600,000,000,000)~=39.1~=40$ 個位元用於紀錄

假設每個 posting list 就有平均1000的長度
那每個 posting list 就會有 $40\times 1000=40000$ 的 bits 約 5 kbyte

set k =44 ,b = 0.49
單字量 M = $44 \times (600\ billion)^0.49~=34965568$

posting file 就有
34965568 * 5 kbyte =174827840 kbyte = 174 GB
> kbyte = KB
> 1000 * KB ~= MB
> 1000 * MB ~= GB

### Save Dictionary
> 如何存儲所有單字
> 1. 使用固定大小 (垃圾方法)
> 2. 使用一個超長字串紀錄，單字只需要紀錄他的長度以及所在位置即可

## Compreesion of Posting file

使用間隔的方式紀錄 posting list 

### example 

game $\rightarrow$ 1,45,59,90
$\Rightarrow$ game $\rightarrow$ 1,44,14,31

可以省下不少空間