# 同餘方程 （Divisibility and Modular Arithmetic）
$$\huge{a\ mod\ b = c \ mod\  b} $$
## Define---Division
if "a" can be divised by "b" , that means exist  a "c" that $a=b\times c$.
$A|C$ is True means  C 可以被 A 整除

> [!Note]- Example
> $3|7$ is False
> $3|12$ is True

## Therom---Properties of Divisibility
1. if $\ a|b\ \& \ a|c \Rightarrow a|(b+c)$
2. if $a|b$ => $a|bc$  for all c in interger
3. if $a|b$ and $b|c$ => $a|c$

> [!note]- Example
> Proof that if $a|b$ and $b|c$ that $a|c$
> >$a|b$ => $ap =b$,p is interger
> > $b|c$ => $bx=c$,x is interger
> > $apx=c$ => $a|c$  

## Define---Division Algorithm
a=dq+r
q= a **div** d , r = a **mod** d
d is called the divisor.
a is called the dividend.
q is called the quotient.
r is called the remainder. (餘數一定要是正數)

> [!note]- exmaple-1
> what are the quotient and remainder when -11 is divided by 3
> -11 = 3 \*(-4)+1
> ans => -4 & 1

## Define---Congurence Relation（同餘）
$a\equiv b(mod\ m)$ => m|(a-b)
## Theorm---同餘???定理

# other 
## RSA
RSA是一種非對稱加密算法，由Ron Rivest、Adi Shamir和Leonard Adleman在1977年提出。RSA算法基於數學中的兩個重要問題：大數因式分解和模指數運算。

RSA算法的運作過程如下：

1. **金鑰生成**：
   - 選擇兩個大質數$p$和$q$，計算它們的乘積$n = p \times q$。
   - 計算$n$的歐拉函數$\phi(n) = (p - 1) \times (q - 1)$。(這屬於歐拉函數特殊解)
   - 選擇一個整數\(e\)，使得$1 < e < \phi(n)$，且$e$與$\phi(n)$互質。
   - 計算$d$，使得$d \times e \equiv 1 \pmod{\phi(n)}$。
   - 公鑰為$(n, e)$，私鑰為$(n, d)$。

2. **加密**：
   - 將明文消息轉換為整數$m$，滿足$0 \leq m < n$。
   - 使用公鑰中的指數$e$，計算密文$c \equiv m^e \pmod{n}$。

3. **解密**：
   - 使用私鑰中的指數$d$，計算密文$c$的解密結果$m \equiv c^d \pmod{n}$。

