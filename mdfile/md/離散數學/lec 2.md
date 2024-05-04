---
tags:
  - 離散
---
# Set
## Define ---Set
### In English 
A set is an **unordered** collection of objects, called elements or members of the set .
We denote that a set-A contain element-a as $a \in A$
We denote that a set-A doesn't contain element-a as $a \notin A$
### In Chinese
集合是物件的**無序**元素組成。
我們將集合 A 包含元素 a 表示為 $a \in A$
我們將集合 A 不包含元素 a 表示為 $a \notin A$

### Example
#### example 1
the set-O of odd positive intergers less than 10 can be express by ?
1. O={1,3,5,7,9}
2. O= {x|x is an odd positive interger less than 10}
3. O={x$\in Z^+$|x is odd and x < 10}
> 三種表示都是合理的作法
> 第一種使用全列出
> 第二種使用文字描述
> 第三種使用集合建構法

#### 多種常見集合符號
1. $\mathbf N${0,1,2,3......},a set of natrual number
	- 自然數的定義可能有是否包含零的歧義，所以通常會使用上下形避免
	- $\mathbf N^0\ or\ \mathbf N_0$ 代表{0,1,2,3,4....}
	- $\mathbf N^*=\mathbf N^+=\mathbf N_{>0}=\mathbf N_1={1,2,3,4,5,6,7}$ 
2. $\mathbf Z$ ={....-2,-1,0,1,2.........} 所有整數 
3. $\mathbf Z^+$ ={0,1,2.........} 所有正整數
4. $\mathbf Q$ = {p/q|p$\in\mathbf Z$,q$\in\mathbf Z$ and q $\ne$ 0 }所有有理數
5. $\mathbf R$ ,real number
6. $\mathbf R^+$,positive real number
7. $\mathbf C$,the complex number (複數)
###  大於等於的符號(等於用`[`,不等於用`(`)
\[a,b\]={x|$a\le x\le b$}
\[a,b\)={x|$a\le x\lt b$}

## Define---Equal of Set

Set-A and Set-B are equal if and only if $\forall x(x\in A \leftrightarrow x\in B)$ .
簡單來說就是A裡有的B有，B裡有的A也有。（饒口令呢！！）

### Example
#### take 1
![[tempFileForShare_20240502-224653.jpg]]

> all same 
> 由於 Set 是不會有順序&重複的問的，so 都一樣
Which set of problem are same ?
## Define---subsets
when $\forall x(x \in A \rightarrow x \in B)$ that we say A is a subset of B ($A \subseteq B$)

### 注意 $\subset \not= \subseteq$

| mark        | 說明                           |
| ----------- | ---------------------------- |
| $\subset$   | 指的是真子集，$A\subset B$ A 不能等於 B |
| $\subseteq$ | $A\subseteq B$ A 可以等於 B      |

####  tips $\subset$
$\forall x(x\in A \rightarrow x \in B)\land \exists x(x\in B \land x \not\in A)$

### how to prove
#### for $A \subseteq B$ 
證明 A 裡的所有元素都在 B 中出現過
#### for A $\not\subseteq$ B
證明在 A 中有出現至少一個元素不在 B 中
#### example
![[SmartSelect_20240503_013548_Samsung Notes.jpg|600]]

> 第一題中說，A={x|$x^2\lt 100$ and$x\in Z$} ,B ={x|$x\in Z^+$}
> **but** $-1\in A$ but $-1 \not\in B$

>在你們學校學習[[離散數學]]的人,並不是你們學校所有資工專業的人的子集。
>yes , 沒什麼好解釋的，就是有外系

### Theorem 1 
For every Set 
1. $\emptyset \subseteq S$
2. $S \subseteq S$
## Define---the size of set (取絕對值)
指的是集合中元素的數量(不取重複)
S = {1,2,3,4,5,67,$\emptyset$}
|S| = 7
## Define---Power Sets(冪集合)
指的是一個集合可能有的所有子集合的集合

### Example
![[tempFileForShare_20240503-132003.jpg|600]]

> Tips 
> 	計算 $|P(S)|$ 就是計算 $|S|^2$

![[tempFileForShare_20240503-132329.jpg|600]]

> 其實也就是那樣，就記得好好算

## Define---Orderd n-tuples(有序n項)
### Compare

| 物件   | 特性           | 用處                  |
| ---- | ------------ | ------------------- |
| 集合   | 無順序之分，不存在重複項 | 用於不會重複的資料集，ex: 類別   |
| 有序n項 | 有順序之分，存在重複項  | 可能重複的資料，通常會用編碼分辨，學號 |

## Define---Cartesain Products(笛卡兒積)
[[chap 2 for 資料庫]]有介紹
$A\times B=\{(a,b)|a\in A \land b \in B\}$

![[tempFileForShare_20240503-133901.jpg|left|600]]

### 通常 AxB≠BxA,除非...
1. A=$\emptyset$ or B =$\emptyset$ (that AxB=$\emptyset$)
2. A=B
## Define---Cartesain Products more than 2 Sets
![[tempFileForShare_20240503-135644.jpg|600]]
### Annotation of Catesain Product
####  Power of itself $A^n$
$\{(a_1,a_2,a_3,...a_n)|a_i \in A for i=1,2,3...n\}$
#### order of pair
when we denote  AxB ,that means  pair $(a_i,b_j)$ where $a_i \in A$ and $b_j\in B$
#### other operation
1. $A\times\emptyset=\emptyset\times A=\emptyset$
2. $A\times B \ne B\times A$
3. $(A\times B)\times C \ne A\times (B\times C)$
4. $A\times(B\cup C)=(A\times B)\cup (A\times C)$ (聯集分配律)
5. $A\times(B\cap C)=(A\times B)\cap (A\times C)$(交集分配律)（聯集與交集相當於加法，而Catesain相當於乘法）
### Example
What are thr ordered pairs in less than or equal to relation , which contains (a,b) if a$\le$b,on set {0,1,2,3}?
> {(0,0),(0,1),(0,2),(0,3),(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)}

## Define---Using Set with Quantifiers
有時我們會使用集合去限制[[lec1|陳述]]的範圍
![[SmartSelect_20240503_153735_Samsung Notes.jpg]]

## Define---Truth Sets and Quantefiers
### In English
Given a Pridicate P and a domain D,we define that the truth set of P to be the set of element x in domain D for which P(x) is true.
The truth set of P(x) is denoted by {x$\in$ D|P(x)} or {x$\in$ D|P(x) is True}.
### In Chinese
給定一個謂詞 P 和一個領域 D，我們定義 P 的真值集合為領域 D 中使得 P(x) 為真的元素 x 的集合。
P(x) 的真值集合通常表示為 {x∈D | P(x)} 或 {x∈D | P(x) 為真}。
### Example
![[tempFileForShare_20240503-154949.jpg]]

> P-> {x$\in$Z| "|x|=1"}
> Q-> {x$\in$Z| "$x^2$=2"}
> R-> {x$\in$Z| "|x|=x"}

# Set operation
## Define---Union（聯集） $\cup$
$A\cup B = \{x|x\in A \lor x \in B\}$
![[Pasted image 20240503194641.png|300]]

## Define---Intersection (交集) $\cap$
$A\cap B = \{x|x\in A \land x \in B\}$
![[Pasted image 20240503194506.png]]

## Define--disjoint (互斥) $\dot\cup$
$A\cap B = \{x|x\in A \land x \in B\}=\emptyset$

![[Pasted image 20240503194923.png]]
## Difine---Difference (差集) (A-B)
$A-B = \{x|x\in A \land x \not\in B\}$
$B-A = \{x|x\not\in A \land x \in B\}$
![[Pasted image 20240503195145.png|300]]
## Define---Complement （補集）$\bar A$
$\bar A$指的是整個空間中除了A 以外的所有空間
$\bar A=\{x\in U|x\notin A\}$
![[SmartSelect_20240503_203532_Samsung Notes.jpg]]
## Define---Size operation (可以用圖解釋)
$|A\cup B|=|A|+|B|-|A\cap B|$
$|A-B|=|A|-|A\cap B|$
## Set identities (運算規則)

| Name                     | identities                                        |
| ------------------------ | ------------------------------------------------- |
| identity laws 同一律        | $A \cap U=A$                                      |
| ^                        | $A\cup \emptyset=A$                               |
| Domination laws 支配律      | $A \cup U=U$                                      |
| ^                        | $A\cap \emptyset=\emptyset$                       |
| Idempotent laws 冪等律      | $A\cap A=A$                                       |
| ^                        | $A\cup A=A$                                       |
| Complementation laws 補集律 | $\overline{ \bar A}=A$                            |
| Commutative laws 交換律     | $A\cap B=B\cap A$                                 |
| ^                        | $A\cup B=B\cup A$                                 |
| Associative laws 結合律     | $(A\cap B)\cap C=A\cap(B\cap C)$                  |
| Distribution laws 分配律    | $A\cup(B\cap C)=(A\cup B)\cap(A\cup C)$           |
| De Morgan's laws         | $\overline{A\cap B}=\overline A \cup \overline B$ |
| Absortion laes 吸收律       | $A\cup(A\cap B)=A$                                |
| ^                        | $A\cap(A\cup B)=A$                                |
| Complement laws 補律       | $A\cup\bar A=U$                                   |
| ^                        | $A\cap\bar A=\emptyset$                           |

### how to prove 2 sets are equal ?
1. show that each is a subset of other
2. use set builder notation and logical equivalence
3. use memberships table
4. Use Set identities

### Example
 > Prove that $\overline{A\cap B}=\overline A\cup \overline B$ (use 1)

我們可以使用集合的定義來證明這個等式。首先，我們來證明 $\overline{A\cap B}\subseteq \overline A\cup \overline B$。

假設 $x\in \overline{A\cap B}$，這表示 $x$ 不在 $A\cap B$ 中。根據集合的補集定義，這意味著 $x$ 要麼不在 $A$ 中，要麼不在 $B$ 中，或者同時不在 $A$ 和 $B$ 中。換句話說，$x\in \overline A$ 或者 $x\in \overline B$，所以 $x\in \overline A\cup \overline B$。因此，我們證明了 $\overline{A\cap B}\subseteq \overline A\cup \overline B$。

接下來，我們證明 $\overline A\cup \overline B \subseteq \overline{A\cap B}$。

假設 $x\in \overline A\cup \overline B$，這表示 $x$ 要麼不在 $A$ 中，要麼不在 $B$ 中，或者同時不在 $A$ 和 $B$ 中。根據集合的補集定義，這意味著 $x$ 要麼在 $A$ 的補集中，要麼在 $B$ 的補集中，或者同時在 $A$ 和 $B$ 的補集中。換句話說，$x$ 不在 $A\cap B$ 中。因此，我們證明了 $\overline A\cup \overline B \subseteq \overline{A\cap B}$。

綜合以上兩個部分，我們可以得出 $\overline{A\cap B}=\overline A\cup \overline B$。
>  Prove that $\overline{A\cap B}=\overline A\cup \overline B$ (use 2)

$\overline{A\cap B}=\{x|x\notin A\cap B\}$
	$=\{x|-(x\in A \cap B)\}$
	$=\{x|-((x\in A)\cap(x\in B))\}$
	$=\{x|-(x\in A )\cup-(x\in B)\}$
	$=\{x|(x\notin A)\cup (x\notin B)\}$
	$=\{x|(x\in\overline A)\cup(x\in\overline B)\}$
	$=\{x|x\in\overline A\cup \overline B\}$
	$=\overline A\cup \overline B$
> Use membership table prove $A\cup(B\cap C)=(A\cup B)\cap(A\cup C)$

| A   | B   | C   | $B\cap C$ | $A\cup B$ | $A\cup C$ | $A\cup(B\cap C)$ | $(A\cup B)\cap(A\cup C)$ |
| --- | --- | --- | --------- | --------- | --------- | ---------------- | ------------------------ |
| 1   | 1   | 1   | 1         | 1         | 1         | 1                | 1                        |
| 1   | 1   | 0   | 0         | 1         | 1         | 1                | 1                        |
| 1   | 0   | 1   | 0         | 1         | 1         | 1                | 1                        |
| 0   | 1   | 1   | 1         | 1         | 1         | 1                | 1                        |
| 0   | 0   | 1   | 0         | 0         | 1         | 0                | 0                        |
| 0   | 1   | 0   | 0         | 1         | 0         | 0                | 0                        |
| 1   | 0   | 0   | 0         | 1         | 1         | 1                | 1                        |
| 0   | 0   | 0   | 0         | 0         | 0         | 0                | 0                        |
因為最後兩條一樣，so proved

> show that $\overline{A\cup(B\cap C)}=(\overline C \cup \overline B )\cap\overline A$

| equation                                       | indentity         |
| ---------------------------------------------- | ----------------- |
| $\overline A \cap\overline{(B\cap C)}$         | De Morgan's law   |
| $\overline A \cap(\overline B\cup\overline C)$ | De Morgan's law   |
| $(\overline B\cup\overline C) \cap\overline A$ | Communtative Laws |
| $(\overline C\cup\overline B) \cap\overline A$ | Communtative Laws |

## Define---Generalized Union
$$\large{A_1\cup A_2\cup A_3\cup A_4\cup ...A_n=\cup^n_{i=1}A_i}$$
## Define---Generalized Intersection
$$\large{A_1\cap A_2\cap A_3\cap A_4\cap ...A_n=\cap^n_{i=1}A_i}$$
## Computer Representation of Sets
> 如何在電腦上表示 Sets

1. store elements with unordered fashion.
	- 但是如果使用不排序的方式存儲，在執行各種集合操作時會很消耗時間（element searching）
2. 使用特定（隨意）的順序存儲所有element
	- 可以使用一個binary string 代表整個 U 空間中的所有 element
	- 假設有一個set-A，其中$element_i$在 A 中，在 string 中第 i 位就記 1 ，反之為 0
### Example
![[SmartSelect_Pin.jpg]]

| num     | $a_{1}$ | $a_{2}$ | $a_{3}$ | $a_{4}$ | $a_{5}$ | $a_{6}$ | $a_{7}$ | $a_{8}$ | $a_{9}$ | $a_{10}$ |
| ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | -------- |
| content | 1       | 2       | 3       | 4       | 5       | 6       | 7       | 8       | 9       | 10       |
subset of all odd integer of U=>101010101010

![[SmartSelect_Pin 1.jpg]]
# Function
n 