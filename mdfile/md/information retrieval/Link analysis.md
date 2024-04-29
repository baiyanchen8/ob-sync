---
titles: 
tags:
  - IR
data: https://www.dropbox.com/scl/fi/romddsr2fe7jiwmbtg8db/Information-Retreival-Lecture-5-Link-Analysis.pptx?dl=0&e=1&rlkey=zxbawckbtxeg27eo3kzq2wr14
---
# Link analysis
## why we need link analysis
是因為有人會惡意利用 database 使他們想要呈現 upper rank 的內容被看見，為此 google 使用許多方法，為了不容易被竄改網頁排名所以需要 (Search Engine Optimization) 
![500](Pasted%20image%2020240429143015.png)

## Page Rank : Defined 
Main Function :$$PageRank=\frac qN +(1-q)\Sigma_{p_i\in L(pi)} PageRank(pi)$$
> N : page 數量
>  q: 指向當前page的數量(以yahoo 舉例: yahoo Amazon 為2) 
![[Pasted image 20240429144827.png|500]]

 > 需要遞迴，因為有可能指向自己所以會有遞迴計算的結構，所以需要反覆計算直至收斂

![[Pasted image 20240429145631.png|500]] 
## Random Walk interpretation
透過隨機移動（通過超連結），模仿使用者使用網路的行為，並計算出現在某個節點的機率，最終以此作為排名
### spider trap(死結)
以下圖解釋，假設現在 random walk 到 microsoft ，就不會出去了，會使評分系統出錯
![[Pasted image 20240429154347.png|500]]

### Random teleport
通過對每個page加上可以到任意page的路徑，避免死結，並且還能更好的模仿使用行為，畢竟使用者不一定只會使用超連結，也有可能直接使用網址
### Dead end
當 $Page_i$ 沒有指向任何 Page，就會導致經遞迴的結果最終將收斂至0
![[Pasted image 20240429154707.png|500]]

### Dealing with dead end
![[Pasted image 20240429155153.png|500]]

## PageRank 越準，就會越來越不準？
我想應該指的是因為不重要或者**新出的page沒有人重視**
也有使用者行為的變化，例如: 使用者**不再使用**超連結

## HITS
