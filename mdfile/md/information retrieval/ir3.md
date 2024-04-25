---
title: ir3
tags: [I.R.]

---


# Rank Retrieval

> 這章節要處理的問題是 『rank retrieval』
> 我們目前只能處理搜尋，但無法處理相關度的問題
> 本章節就是解決這個
## w 

$idf_t = log_{10}(N/df_t)$ , N : 文章總數 $df_t$ ：出現 term t 的文章總數
因為出現太多次（在不同文章中）的term 是沒有意義的
so ,需要idf 

$wtf= 1 + log_{10}(tf_{t,d})$ , $tf_{t,d}$：在文章 d 中term t 出現的次數
用於計算 term t 在文章 d 的重要性

$w= (wtf)(idf_t)$

## BM25 (OKapi)
>改用除法處理 term 的飽和度

捨棄log的方法，因為除法比較快，而且值會值會介於 0~1 之間
$\large{wtf=\frac{tf_{t,d}}{tf_{t,d}+k}}$ 
- k: a given parameter

> 在加上考慮文章長度

$\large{wtf=\frac{tf_{t,d}}{tf_{t,d}+k\times \frac{dl}{adl}}}$

$dl$ : document length
$adl$ : average document length 

> 將上考慮文章長度的重要性


$\large{wtf=\frac{tf_{t,d}}{tf_{t,d}+k\times(1 - b + b \times \frac{dl}{adl})}}$

$b$ : given parameter 
# Vector Sparse Model
> A collection of n documents can be represented in the vector space model by a term-document matrix.

| Document \ Term | T<sub>1</sub>  | T<sub>2</sub>  | T<sub>3</sub>  | ... | T<sub>t</sub>  |
| --------------- | -------------- | -------------- | -------------- | --- | -------------- |
| D<sub>1</sub>   | w<sub>11</sub> | w<sub>21</sub> | w<sub>31</sub> | ... | w<sub>t1</sub> |
| D<sub>2</sub>   | w<sub>12</sub> | w<sub>22</sub> | w<sub>32</sub> | ... | w<sub>t2</sub> |
## Similarity Measur
> 三種可能計算相似度的方法
> > 1. Euclidean Distance (歐肌理得距離) 
> > 2. Inner Product （內積）
> > 3. Cosine Similarity （角度）

1. Euclidean Distance (歐肌理得距離) (就是垃圾)
    - 距離近不代表相似
2. Inner Product （內積）
    - $\Sigma^n_{i=1}A_i\times B_i$（每項乘積和）
    - 假設是 binary index ，就只需要紀錄批配項和
    - 假設是 weighted index , 就需要將每項相乘取和
3. Cosine Similarity （角度）
    ![image](image/rJoeZCeWA.png)

> ***第61 頁不懂*** 做等解釋

## TAAT & DAAT

### TAAT (Term At A Time)
Scores for all docs computed concurrently, one query term at a time.

先看第一個 term，算出每個文件的 partial score，再看第二個 term 再慢慢加起來…

- 優點是能減少硬碟的讀取(不用讀取所有posting list)
- 缺點是很耗記憶體，因為要儲存所有候選文件的 partial score
### DAAT (Document At A Time)
Total score for each doc (include all query terms) computed, before proceeding to the next.

先看第一個文件所存在的 term

- 優點是能節省記憶體
- 缺點是必需把整個 inverse index 的 list 讀取出來



# Non-safe Ranking
> 因為只需要搜出差不多的東西，就可以了，使用者是感受不出來的。

## Bloom filter 稿不懂

