# 1.1 Matrices and Vectors
## Matrix
> [!tip] DEFINE
> A matrix is a rectangular array of scalars.
> 矩陣是標量的矩形陣列。 標量在線代中是指實數$\mathbb{R}$

### row & col
if the size of matrix A is $m\times n$

$$
A = \begin{pmatrix}
a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m,1} & a_{m,2} & \cdots & a_{m,n}
\end{pmatrix} = [a_{i,j}]
$$
if m\==n:
	that we say it is square

if A\==B:
$$
A = B \Leftrightarrow \forall_{i,j}\{a_{i,j}=b_{i,j}\}
$$
即大小相同且所有點的數值相同

> [!example]-
> ![[Pasted image 20240704213446.png]]
> **ANS**: 唯有 A=C

### Submatrix(子矩陣)
> [!tip] DEFINE
> 一個大矩陣中切割出的一部份即為 submatrix
> $$ A = \begin{pmatrix} a_{1,1} & a_{1,2} & a_{1,3} & a_{1,4} \\ a_{2,1} & a_{2,2} & a_{2,3} & a_{2,4} \\ a_{3,1} & a_{3,2} & a_{3,3} & a_{3,4} \\ a_{4,1} & a_{4,2} & a_{4,3} & a_{4,4} \end{pmatrix} $$
> $$ B = \begin{pmatrix} a_{2,2} & a_{2,3} \\ a_{3,2} & a_{3,3} \end{pmatrix} $$
> B 為 A 的 submatrix

### Matrix Addition 
> [!tip] define
> if and only if size of A is equal size of B ,A can add B.
> 只有當 A B 大小相等時才能相加，且為對應元素相加
> $$ A = \begin{pmatrix} a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\ a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m,1} & a_{m,2} & \cdots & a_{m,n} \end{pmatrix} $$ $$ B = \begin{pmatrix} b_{1,1} & b_{1,2} & \cdots & b_{1,n} \\ b_{2,1} & b_{2,2} & \cdots & b_{2,n} \\ \vdots & \vdots & \ddots & \vdots \\ b_{m,1} & b_{m,2} & \cdots & b_{m,n} \end{pmatrix} $$ $$ C = A + B = \begin{pmatrix} a_{1,1} + b_{1,1} & a_{1,2} + b_{1,2} & \cdots & a_{1,n} + b_{1,n} \\ a_{2,1} + b_{2,1} & a_{2,2} + b_{2,2} & \cdots & a_{2,n} + b_{2,n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m,1} + b_{m,1} & a_{m,2} + b_{m,2} & \cdots & a_{m,n} + b_{m,n} \end{pmatrix} $$


> [!example]-
> ![[Pasted image 20240704215032.png]]
> 由於一般加法存在交換性，而矩陣加法屬於一般加法的延伸，可以理解為繼承屬性，因此具有交換性

### Zero Matrix

> [!tip] define
>$$ A + O = A\ for\ all\ A $$
>$$ A \cdot O = O\ for\ all\ A $$

> [!example]-
> ![[Pasted image 20240704214827.png]]
> 不會一樣，因為 size 不同

### Transpose 轉置矩陣
> [!tip] define
> $$ A = \begin{pmatrix} 
> a_{1,1} & a_{1,2} & a_{1,3} \\ 
> a_{2,1} & a_{2,2} & a_{2,3} 
> \end{pmatrix} $$ 
> 則矩陣 $A$ 的轉置矩陣 $A^T$ 為： 
> $$ A^T = \begin{pmatrix} 
> a_{1,1} & a_{2,1} \\ 
> a_{1,2} & a_{2,2}  \\ 
> a_{1,3} & a_{2,3} 
> \end{pmatrix} $$

> [!tip] Tranpose 的運算規則
> 1. $(A+B)^T=A^T+B^T$
> 2. $(sA)^T=s\cdot A^T$
> 3. $(A^T)^T=A$
###  對稱矩陣
> [!tip] define
> if $A^T=A$ 稱為　Symmetric Matrix
> if $A^T=-A$ 稱為　skew-Symmetric Matrix
### identify Matrix
**Must be square**
$I_n = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$

### Stochastic Matrix
> [!tip] define
> 1. 方陣 
> 2. 所有 col 的元素合為 1 (unity、單位元素) 
> 3. all element must be non-negative 
>
>  identify Matrix 為 Stochastic Matrix 的一種特例
>  *example:*
>  ![[Pasted image 20240705142203.png]]

> [!example]-
> ![[Pasted image 20240705142331.png]]

### rotation Matrix
這是一個二維旋轉矩陣範例：$R(\theta) = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$。
> [!example]-
> ![[Pasted image 20240705142701.png]]

### Matrix trace
> [!tip] define
> - 當Matrix 為方陣時，他的對角線（左上右下）總和
> - $\Sigma a_{ii}$

### 共軛(Conjugate)矩陣與轉置共軛(Conjugate Transpose)矩陣
#### 共軛(Conjugate)矩陣
$$
A = \begin{pmatrix} 1 + i & 2 - 3i \\ 4 + 2i & 3 \end{pmatrix}
$$

$$
\overline{A} = \begin{pmatrix} 1 - i & 2 + 3i \\ 4 - 2i & 3 \end{pmatrix}
$$
#### 轉置共軛(Conjugate Transpose)矩陣
$$
A = \begin{pmatrix} 1 + i & 2 - 3i \\ 4 + 2i & 3 \end{pmatrix}
$$

首先，我們求轉置矩陣 $A^T$：
$$
A^T = \begin{pmatrix} 1 + i & 4 + 2i \\ 2 - 3i & 3 \end{pmatrix}
$$

然後，我們取轉置矩陣的共軛，得到轉置共軛矩陣 $A^H$：
$$
A^H = \begin{pmatrix} 1 - i & 4 - 2i \\ 2 + 3i & 3 \end{pmatrix}
$$
### Hermitian matrix
> [!tip] define
> if $A^H=A$ ，稱為　Hermitian matrix
> if $A^H=-A$，稱為　skew-Hermitian matrix
## Vector 
- row vector
	- $[1\ 2\ 3\ 4]$
- colum vector
	- $\left[ \begin{align} x \\ y \\ z \end{align} \right]$
	- $[x\ y\ z]^T$
	- The term of **vector** always refers to **col vector**
	- $R^n=M_{n\times 1}$ 有 n 個 element 的 col vector
	- $v_i$  第 i 個 element of vector $\textbf{v}$


# 1.2 反矩陣
## define
> [!tip] define
> - 左(右)反矩陣
> 	- $A_{m\times n}B_{n\times m}=I_{m\times m}$
> 	- 對於 A 而言，B 是右反矩陣（right inverse matrix）
> 	- 對於 B 而言，A 是左反矩陣（left inverse matrix）
> - 反矩陣
> 	- 當　$m==n$
> 	- 左反=右反
> 	- 當 A 存在反矩陣時，A 為 inversible matrix or nonsingular matrix

## Theorem 1-6
> [!tip] define 
> 方陣(可逆矩陣)的反矩陣存在唯一性

> [!error]- proof
> **反證法**：
> 假設不存在唯一性，則可逆矩陣 A 存在 2 反矩陣 B、C 
> $AB=I$ and $AC=I$
> that $B=A^{-1}$ and $C=A^{-1}$
> so $B=A^{-1}=C$ ， $B=C$ 得證反矩陣存在唯一性

## Theorem 1-7
> [!tip] define
> if A 為可逆矩陣，$A^{-1}$ 也是可逆矩陣，且$(A^{-1})^{-1}=A$

>[!error]- proof
> 根據定義：$AA^{-1}=I$
> so $A$ 的反矩陣為 $A^{-1}$，$A^{-1}$ 的反矩陣也為 $A$

## Theorem 1-8

> [!tip] define
> $A、B\in F_{n\times n}$，if $A、B、AB$ 可逆，that $(AB)^{-1}=B^{-1}A^{-1}$

> [!error]- proof
> if $AB$ 的反矩陣為 $B^{-1}A^{-1}$
> that $AB\cdot B^{-1}A^{-1}=B^{-1}A^{-1}\cdot AB=I$
> because $AB\cdot B^{-1}A^{-1}=B^{-1}A^{-1}\cdot AB=I$ is right 
> so $AB$ 的反矩陣為 $B^{-1}A^{-1}$

>[!example]- 
![[線代chap 1.1]]

## Theorem 1-9
> [!tip] define
> if $A$ 為可逆方陣
> 1. $A^T$ 為可逆且　$(A^{-1})^T=(A^T)^{-1}$
> 2. $A^H$ 也可逆且　$(A^{-1})^H=(A^H)^{-1}$

## Define 方陣多項式
> [!tip] define
> $$
> p(A) = a_0 I + a_1 A + a_2 A^2 + \cdots + a_m A^m
> $$

## Theorem 1-10
> [!tip] define
> 1. $f(A)g(A)=g(A)f(A)$
> 2. if $g(A)$ 可逆則 $f(A)g(A)^{-1}=g(A)^{-1}f(A)$

# 1.3 基本列運算
## Theorem 1-14
> [!tip] define
> if $A$ 列等價於 $B$ 則，存在 可逆矩陣$P$ 使 $B=PA$
> $P$ 為多個 $I$ 的乘積（P 為初等矩陣即為　$I$  進行 row operation 之後的結果）
# 1.4 線性方程組
## define 線性系統

![[Pasted image 20240706190108.png]]
### Solution set
> [!tip] define
> 以集合方式表達解的方式稱為 solution set


- if a system of equation is **consistent**
	- 有解(一組或以上)
- **inconsistent**
	- 無解 (solution set is empty)
- if two system of equation is equivalent 
	- same solution set

### System linear equation in Matrix


> [!tip] define
> 我們將 function 定義為以下形式:
> $$Ax=b$$
> 其中:
> $$ A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}, \quad \mathbf{x} = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix}, \quad \mathbf{b} = \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix} $$
> A 為 coefficient matrix，x 為 variable vector，b  is ????(i don't know)
> $[A|b]$ is augmented matrix(增廣矩陣)

- if b =0 
	- 稱$Ax=0$ 為齊次線性系統(homogeneous linear system)
- if b$\not =$ 0
	- 稱$Ax=b$ 為非齊次線性系統(nonhomogeneous linear system)
## 注意事項　1-14
> [!note]
> 在齊次線性系統中，$Ax=0$ 因為 $A\cdot 0=0$ 必成立，所以$Ax=0$必有解，稱為顯然解（trivial solution）
> 

## Theorem 1-15
> [!tip] define
> 假設 $A\in F_{m\times n}$，其中$F=\mathbb R\ or\ \mathbb C$ 為一個無限體,則 $Ax=0$具非零解 $\Leftrightarrow$ $Ax=0$ 具有無限多解

> [!error]- proof
> 1. $Ax=0$具非零解 $\Leftarrow$ $Ax=0$ 具有無限多解
> 顯而易見
> 2.  $Ax=0$具非零解 $\Rightarrow$ $Ax=0$ 具有無限多解 	
> 假設 $Ax = 0$ 具有非零解。這意味著 $A$ 的零空間（null space）有非零向量，即 $\text{Null}(A)$ 至少有一個非零向量 $v$。 
>  我們來考慮這個非零向量 $v$，以及所有 $v$ 的標量倍數 $cv$，其中 $c \in F$ 且 $c \neq 0$。這些向量 $cv$ 也必定是 $A$ 的解，因為：  $$  A(cv) = cA(v) = c \cdot 0 = 0$$  
>  由於 $F$ 是無限體，因此 $c$ 可以取無限多個不同的值，從而 $cv$ 可以形成無限多個不同的解。  
>  因此，零空間 $\text{Null}(A)$ 包含無限多個不同的解。這證明了當 $Ax = 0$ 具有非零解時，它必然具有無限多解。  
>  綜上所述，我們得到了完整的證明：$Ax = 0$ 具有非零解 $\Leftrightarrow$ $Ax = 0$ 具有無限多解。

## define (Reduced) Row Echelon Form 
### Row Echelon Form, REF

一個矩陣處於列階梯形時具有以下特性：

1. 所有的 非零 row 都在 零 row 的上方。
2. 每個 非零  row 的首個非零元素（稱為主元、leading entry）位於其**上方**的leading entry 右側。
3. 主元(leading entry)**下方**的元素全為零。

$$ A = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 2 & 3 \\ 0 & 0 & 0 & 0 \end{pmatrix} $$
### Reduced Row Echelon Form, RREF

簡化行階梯形具有列階梯形的所有特性，並且還具有以下特性：

1. 每個leading entry都為 1。
2. 每個leading entry所在 col 的其他元素全為零。

$$A' = \begin{pmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 1 & 1.5 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$
### 意義
> [!tip] 當 augmented matrix in (Reduced) Row Echelon Form ，求解會變得很容易

## define Gaussion 消去法、Gauss-Jodan消去法
1. 將矩陣運算到 row echelon form ，就是 Gaussion 消去法
2. 將矩陣運算到 reduced row echelon form，就是 Gauss-Jodan消去法
## Theorem 1-16
> [!tip] define
> 當 $[A|a]=[B|b]$（列等價） 時，$Ax=a$ 與 $Bx=b$ 有相同的解集合

## Theorem 1-17
> [!tip] define
> 當 $A=B$（列等價） 時，$Ax=0$ 與 $Bx=0$ 有相同的解集合

## Theorem 1-18
> [!tip] define
> 假設$x_0$為$Ax=b$的其中一個解，解集合為$\{x_0+u|u\in U\}$，其中 $U=\{u|Au=0\}$

> [!error] proof
> 1. 假設 $x_0$ 是  $Ax = b$ 的解，即 $Ax_0 = b$。
> 2. 令 $u = x - x_0$。我們要證明 $u \in U$，即 $A u = 0$。
> 3. 由於 $A x = b$ 且 $A x_0 = b$，我們有：$$A u = A (x - x_0) = A x - A x_0 = b - b = 0$$
> 4. 因此，任何 $x$ 可以表示為 $x = x_0 + u$，其中 $u \in U$。
> 
> 這表明，方程 $Ax = b$ 的解集合可以表示為 $\{x_0 + u \mid u \in U\}$，其中 $U = \{u \mid Au = 0\}$ 是齊次方程 $Au = 0$ 的解空間。

## define---Rank and Nullity (必需要在 RREF 下計算)
### Rank (basic variable)
**num of Non-Zero row**，可以代表 system 中有用的 equation 有幾個
> [!tip] define
> if in consistent(有解) system of equation
> 	- rank(A) = basic variable 的個數 = rank(\[A|B\])
> if not consistent 
> 	- rank(A) +1 = rank(\[A|B\])
### Nullity(free variable)
colum - Rank 
### Rank-Nullity Theorem
$$Rank(A)+Nullity(A)=n$$
### Test of consistency
 > [!tip] theorem
 > reduced row echelon form of augmented matrix 中沒有 \[0 0 0 0 0...d\] 則有解，rank(A)=rank(\[A|B\])

## Theorem 1-19 Ax=b 有解？
> [!tip] define
> 1. $rank(A)\not =rank([A|b])\Leftrightarrow Ax=b$ 無解$$範例：A=\left[\begin{matrix}1&0&0\\ 0&1&0\\ 0&0&0\end{matrix}\right]，[A|b]=\left[\begin{array}{ccc|c}1&0&0&1\\ 0&1&0&1\\ 0&0&0&1\end{array}\right]$$
> 2. $rank(A) =rank([A|b])=row\ 數\Leftrightarrow Ax=b$ 有唯一解 $$範例：A=\left[\begin{matrix}1&0&0\\ 0&1&0\\ 0&0&1\end{matrix}\right]，[A|b]=\left[\begin{array}{ccc|c}1&0&0&1\\ 0&1&0&1\\ 0&0&1&1\end{array}\right]$$
> 3.  $rank(A) =rank([A|b])<row\ 數\Leftrightarrow Ax=b$ 無限組解$$範例：A=\left[\begin{matrix}1&0&0\\ 0&1&0\\ 0&0&0\end{matrix}\right]，[A|b]=\left[\begin{array}{ccc|c}1&0&0&1\\ 0&1&0&1\\ 0&0&0&0\end{array}\right]$$


# 1.5可逆矩陣
## 引理
> [!tip] define 
> 假設$A\in F_{m\times n}$，則 $Ax=0$只有 0 解 $\Leftrightarrow$ A列等價於 $I_n$


> [!error] proof - 沒必要

## Theorem 1-20
> [!tip] define
> $A\in F_{n\times n}$,即 A 為方陣時下列敘述等價
> 1. $A$ 為可逆矩陣
> 2. $Ax=0$ 只有 0 解
> 3. $A$ 列等價 $I$
> 4. $A$ 為若干個基本矩陣（$I$）乘積

## Theore 1-21
> [!tip] define 
> 假設 $A、B \in F_{m\times n }$,則 A 列等價於 B $\Leftrightarrow$存在一可逆矩陣 P  使 $PB=A$

>[!error] proof
> ($\Leftarrow$) 
> 左成一次列基本（初始）矩陣相當做一次列運算，而一個可逆矩陣就是一個初始矩陣

## Theorem 1-22
> [!tip] define
> if $A \in F_{m \times m}$
> 1. A 有右反矩陣 B ，則 $A^{-1}=B$,且 A 可逆
> 2. A 有左反矩陣 C ，則 $A^{-1}=C$,且 A 可逆
> => 但是方陣的左反不是等於右反矩陣？
## Theorem 1-23
> [!tip] define
> if $A\in F_{n\times n}$,下列敘述等價
> 1. $A$ 為可逆矩陣
> 2. $\forall b\in F_{n\times1}$,$Ax=b$ 具有唯一解
> 4. $\forall b\in F_{n\times1}$,$Ax=b$ 有解


> [!error] proof
> 3 $\Rightarrow$  1 
> 因為 "for all b" $Ax=b$ 有解
> 則可假定 $e_i=第i位為1且其他位為0的colum\ vector$
> 且$A\times x_i=e_i$,令$E=[x_1....x_n]$
> $AE=[Ax_1 Ax_2......Ax_n]=[e_1 e_2 ....e_n]=I_n$
> 則可以看出 $E$ 為 $A$ 的右反矩陣，又因為 $A$ 為方陣，所以可說 $E$ 為 $A^{-1}$
> $\Rightarrow$  由此看出 $A$ 為可逆矩陣

# 1-6 LU 分解

## Define--- LU 分解
> [!tip] define
> 