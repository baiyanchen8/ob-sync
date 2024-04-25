---
title: ir5
tags: [I.R.]

---



1. Sparse Retrival
    在 rank retrival 中，各個 vector 分佈可能非常分散(Sparse Retrival)，所以我們可能通過降為將維度下降，以穫得更好的結果--Desnse Retrival
2. Language Modelling
    - 所謂language Modelling 就是透過前字猜後字的遊戲
    - 簡單的作法就是統計,like 使用長度為3的 chunk ，透過滑動的方式紀錄所有 doc 中所有chunk 的後一個字，就能紀錄所有
    - problem : 但是沒有辦法預測沒有出現過的組合 , so 通過詞向量的找相近解
3. 詞向量
    - 原本透過統計的方式只能知道 A 後面有沒有出現 B 
        - if A 後有 B , $P(A\rightarrow B)=1$
        - if not , $P(A\rightarrow B)=0$
        - 但沒法預測沒出現過的
    - so , 轉為預測機率(softmax)
        - 假設我們空間中只有(A,B,C,D)四個向量
        - $\large{P(B|A;\theta)=\frac{e^{\vec{A}\cdot\vec{B}}}{e^{\vec{A}\cdot\vec{B}}+e^{\vec{A}\cdot\vec{C}}+e^{\vec{A}\cdot\vec{D}}}}$
        - [[圖片]]
