
# 3.1 因數與質數

> [!tip] define
> $a、b$ 為二整數，$b\not =0$ 若存在1整數 $c$ 使$a=bc$，則 a 是 b 的倍數，b 是 a 的因數，$b|a$ 

## Theorem 1 
> [!tip] define
> $a、b、c、x、y\in \mathbb{Z}$,if $a|b \land a|c$ so $a|bx+cy$

> [!error]- proof
> $$
> a|b\Rightarrow b=am、a|c\Rightarrow c=an
> $$
> $$
> bx+cy=a(mx+ny) \Rightarrow a|bx+cy
> $$

## define---質數

> [!tip] define
> 任意一個 > 1 的整數 p，無法被 1 < x < p 整除，則稱為 prime ，不符合的稱為 composite


## Theorem 2 質數有無限個
> [!tip] define
> 如題

> [!error]- proof
> 所有質數都能表示為 $p_i=p_1p_2p_3.....p_n+1$，且所有p都為質數
> 假設 $p_k$ 為最大的質數，但根據以上定義還有一個 $p_{i}$ > $p_k$，因此假設不成立
> $\Rightarrow$ 永遠會有更大的質數

## Theorem 3 貝祖定理（Bézout's identity）
> [!tip] define
> $x、y\in \mathbb{Z}^+$，則存在 2 整數 $m、n$ 使$xm+ny=gcd(x,y)$
> 若$gcd(x,y)=1$，則$x、y$互質
> 可用擴展歐肌理德算法算出$m、n$


## Theorem 4 $gcd(a,b)\times lcm(a,b)=ab$
> [!tip] define 如題

> [!error]- proof
> 設 $d =gcd(a,b)\Rightarrow a=d\cdot a_1,b=d\cdot b_1$
> that $lcm(a,b)=d\times a_1\times b_1$
> so $gcd(a,b)\times lcm(a,b)=d\times d\times a_1\times b_1=ab$ ,得證
> 

## Theorem 5 
> [!tip] define
> $a,b,c\in \mathbb{Z}^+$,$c|ab$,if $c|a$ and $c|b$

## 3.2 同餘

