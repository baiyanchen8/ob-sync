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

# 1.2 Linear Combanation

> [!tip] define
> $$c_1u_1+c_2u_2+c_3u_3+c_4u_4+...c_ku_k$$
> 由 coefficient $c_i$ 和 vector $u_i$ 組合而成的向量就稱文為 $u_1$ ~ $u_k$ 的線性組合


## Standard vectors 

$$\left[ \begin{align} 1 \\ 0 \\ 0 \end{align} \right]$$ 只有一個 1 其他都是 0 的 vector 
## Marix Vector Product
$$A\mathbb{v}=v_1\mathbb a_1+v_2\mathbb a_2+v_3\mathbb a_3.....$$
$$A\mathbb{v}=[\mathbb a_1\ \mathbb a_2\ \mathbb a_3.......]\left[\begin{align}v_1\\v_2\\v_3\\v_4\end{align}\right]$$

![[Pasted image 20240705140422.png]]

# 1.3 System of Linear Equation

![[Pasted image 20240706190108.png]]
## Solution set
> [!tip] define
> 以集合方式表達解的方式稱為 solution set


- if a system of equation is **consistent**
	- 有解(一組或以上)
- **inconsistent**
	- 無解 (solution set is empty)
- if two system of equation is equivalent 
	- same solution set

## System linear equation in Matrix


> [!tip] define
> 我們將 function 定義為以下形式:
> $$Ax=b$$
> 其中:
> $$ A = \begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}, \quad \mathbf{x} = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix}, \quad \mathbf{b} = \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix} $$
> A 為 coefficient matrix，x 為 variable vector，b  is ????(i don't know)
> $[A|b]$ is augmented matrix(增廣矩陣)

## operation of elementary row (基本行變換)
#### 行交換
將矩陣 $A$ 的第 $i$ 行與第 $j$ 行交換可以表示為 $R_i \leftrightarrow R_j$。
$$\begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} 
\xRightarrow{R_1\leftrightarrow R_2}
\begin{pmatrix} a_{21} & a_{22} & a_{23} \\ a_{11} & a_{12} & a_{13} \\ a_{31} & a_{32} & a_{33} \end{pmatrix}$$
#### 行乘法
將矩陣 $A$ 的第 $i$ 行乘以一個非零常數 $k$ 可以表示為 $R_i \rightarrow k R_i$。
$$
\begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} 
\xRightarrow{R_1\rightarrow 2\times R_1}
\begin{pmatrix} 2\times a_{11} &2\times  a_{12} &2\times  a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} 
$$
#### 行加法
將矩陣 $A$ 的第 $i$ 行加上第 $j$ 行的 $k$ 倍可以表示為 $R_i \rightarrow R_i + k R_j$。
$$
\begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} 
\xRightarrow{R_1\rightarrow R_1+1\times R_2}
\begin{pmatrix} a_{11} +a_{21} &  a_{12}+a_{22} &  a_{13}+a_{23} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} 
$$

## (Reduced) Row Echelon Form 
### Row Echelon Form, REF

一個矩陣處於列階梯形時具有以下特性：

1. 所有的 非零 row 都在 零 row 的上方。
2. 每個 非零  row 的首個非零元素（稱為主元、leading entry）位於其**上方**的leading entry 右側。
4. 主元(leading entry)**下方**的元素全為零。

$$ A = \begin{pmatrix} 1 & 2 & 3 & 4 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 2 & 3 \\ 0 & 0 & 0 & 0 \end{pmatrix} $$
### Reduced Row Echelon Form, RREF

簡化行階梯形具有列階梯形的所有特性，並且還具有以下特性：

1. 每個leading entry都為 1。
2. 每個leading entry所在 col 的其他元素全為零。

$$A' = \begin{pmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 1 & 1.5 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$
### 意義
> [!tip] 當 augmented matrix in (Reduced) Row Echelon Form ，求解會變得很容易

# 1.4 Gaussian Elimination
 高斯消去法（Gaussian Elimination）是一種用來求解線性方程組、求矩陣的秩和求矩陣的逆的方法。這種方法通過一系列的行變換將矩陣轉換成行階梯形或簡化行階梯形，從而使得問題變得更加容易解決。

### 高斯消去法的步驟

高斯消去法主要包括以下步驟：

1. **前向消去（Forward Elimination）：** 將矩陣轉換成行階梯形（Row Echelon Form, REF）。
2. **回代（Back Substitution）：** 將行階梯形轉換成簡化行階梯形（Reduced Row Echelon Form, RREF）。

### 前向消去

通過一系列的基本行變換將矩陣的下三角部分變為零。

### 回代

通過從下至上的操作，將每一列的主元變為1，並且將主元所在列的其他元素變為零。

## Rank and Nullity (必需要在 RREF 下計算)

### Rank (basic variable)
num of Non-Zero row，可以代表 system 中有用的 equation 有幾個
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

# 1.6 Set theorem

- Union set
	- 聯集
- intersection set
	- 交集
- difference set
	- 差集

$$R^n=\{[x_1,x_2,x_3......]^T,x_1,x_2,x_3......\in R\}$$

 > [!question] $R^2$ is $R^3$ 的 subset ? 
 > NO!!!!!!!!
 
 
 
# 1.6 Span of a Set of Vectors

## Span of Set 
> [!tip] define
> **向量空間的生成集合**：一組向量的Span指的是所有這些向量的線性組合所構成的空間。例如，給定兩個向量 $v_1$​ 和 $v_2$​，它們的Span是所有形如 $av_1+bv_2$​ 的向量，其中 $a$ 和 $b$ 是任意實數。
> $$v\in\ Spna\{u_1,u_2,u_3\}$$
