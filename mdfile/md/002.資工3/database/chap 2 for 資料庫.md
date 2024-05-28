---
title: chap 2 for 資料庫
tags: [資料庫]

---

# Introduction of Relation Model

## Structure of Relational Databases
### relation schema 
R=($A_1,A_2,A_3....$) ⇒ relation schema
R ⇒ table
$A_1,A_2....$ 為 attribute 

## Database Schema
R($A_1,A_2$) ⇒ Database Schema

## Keys
### define
key 是由一個 table 中的部分或全部 attribute 組成
### super key
在 所有 key 的組合中能夠達到分辨每個tuple也就是在table中能符合  unique 條件的即為 super key(請注意這裡的 unique 並非指單個attribute 的唯一性）
### Candidate key
- 定義： 候選鍵是資料表中能夠唯一標識每一筆記錄的一組屬性或屬性的集合。
- 特性：
	- 可能有多個候選鍵存在於一個資料表中。
	- 候選鍵的選擇應基於該屬性或屬性的組合確實能夠標識唯一的記錄。

### Primary Key
- 定義： 主鍵是從候選鍵中選擇出來的一個鍵，用來唯一識別資料表中的每一筆記錄。
- 特性：
	- 資料表中只能有一個主鍵。
	- 主鍵的選擇通常基於簡單性、穩定性和易於管理。
### Candidate key vs Primary Key
1. 數量： 一個資料表可以有多個候選鍵，但只能有一個主鍵。
1. 用途： 候選鍵是可能成為主鍵的屬性集合，而主鍵是被選中作為唯一識別記錄的鍵。
1. 唯一性： 主鍵必須是唯一且不能包含空值，而候選鍵只需要確保其屬性組合是唯一的。
## Schema Diagrams
模式圖（Schema Diagrams）是用來視覺化資料庫結構的工具，它展示了資料庫中的資料表、屬性和它們之間的關係。以下是模式圖的一些重要元素：

1. 資料表（Table）： 以方框表示，每個方框內包含資料表的名稱，列出該表所包含的屬性。
1. 屬性（Attribute）： 在資料表方框中列出，代表該表的屬性或欄位。屬性的資料型態和限制條件也可以包含在內。
1. 關聯線（Relationship Lines）： 連接不同資料表之間的關聯，用來表示表之間的關係。箭頭通常指向參照的表，顯示參照的方向。
1. 主鍵（Primary Key）： 以底線或其他方式標示在資料表方框中，表示該屬性或屬性組合是該表的主鍵。

1. 外鍵（Foreign Key）： 以斜線或其他方式標示在資料表方框中，表示該屬性是參考其他表的主鍵，建立表之間的關聯。


## Relational Query Languages
### 程序式（Procedural）
程式式程式設計是一種傳統的程式設計範式，強調的是通過明確的步驟和指令來實現任務。以下是一些特點和相關的資訊：

- 特點：
	- 使用過程呼叫或函數呼叫的方式進行流程控制。
	- 程序是一系列的運算步驟，可以是常式、子程序、方法或函式。
	- 需要明確指定實現的步驟。
- 範例語言：
	- Fortran、ALGOL、COBOL、PL/I、BASIC、Pascal、C等。

### 非程序式或聲明式（Declarative）
宣告式程式設計則更著重於描述計算的邏輯和目標，而不是明確指定實現的步驟。以下是一些特點和相關的資訊：
- 定義:
	- 告訴電腦需要計算「什麼」而不是「如何」去計算的進階程式。
	- 明確的對應數理邏輯的程式語言。
- 特點：
	- 表達計算的邏輯而不描述控制流程。
	- 不需要明確指定每一步該怎麼做，而是告訴電腦需要計算「什麼」。
- 範例語言：
	- 資料庫查詢語言如SQL的查詢子集、XQuery。
	- 正規表示式。
	- 組態管理系統如Puppet管理組態語言。


總的來說，程序式程式設計強調執行的步驟，而宣告式程式設計強調實現的目標，並且通常對於控制流程的細節有較少的關注。

## The Relational Algebra
在關聯代數中，各種操作符號的表示如下：

- 選擇 (Select): 用符號 $σ$ 表示。
- 投影 (Project): 用符號 $\Pi$ 表示。
- 笛卡兒積 (Cartesian Product): 用符號 $×$ 表示。
- 連接 (Join): 用符號 $⋈$ 表示。
- 交集 (Intersection): 用符號 $∩$ 表示。
- 聯集 (Union): 用符號 $∪$ 表示。
- 集合差異 (Set Difference): 用符號 $-$ 表示。
- 賦值 (Assignment): 用符號 $←$ 表示。
- 重新命名 (Rename): 可以使用其他符號或者不使用特定符號，有時也用 $ρ$ 表示。

這些操作符號在關聯代數中被用來表示不同的操作，例如從資料表中選擇特定條件的行，將資料表的列專案化，計算笛卡兒積或連接兩個資料表，以及進行交集、聯集和集合差異等。

### Select Operation

- Query
	- $\sigma_{dept_name='Physics'}(instructor)$
- result

- We allow comparisons using
	- $=,\ne,\gt,\ge,\lt,\le$
- We can combine several predicates into a larger predicate by using the connectives:
	- ^ (and), v (or), - (not)
- example:尋找薪水超過$90,000的物理學教授。
	- $\sigma_{\text{dept\_name} = \text{"Physics"} \land \text{salary} > 90,000}(\text{instructor})$

### Project Operation
- define
	- $\Pi_{A_1,A_2,A_3...}(R)$
	- 這個 operation 的作用是選擇 attribute 輸出
- example
	- $\Pi _{name}(\sigma_{dept_name ="Physics"(instructor)})$

### Cartesian-Product Operation
- 就是對兩個table使用基本乘法
- instructor X teaches
- 假如有重複名稱的attribute不會合併 ⇒ $teaches.ID\;\&\; instructor.ID$

### Join Operation
- Inner Join
	- 代數表示法：$⋈$
	- 描述：內連接返回兩個表中共同擁有的元組，即它們在連接條件上匹配的元組。
- left outer join
	- 代數表示法：⟕
	- 描述：左外連接返回左表中的所有元組，以及與右表中匹配的元組。如果右表中沒有匹配的元組，對應的結果將為 NULL。
- right outer join 
	- 代數表示法：⟖
	- 描述：右外連接返回右表中的所有元組，以及與左表中匹配的元組。如果左表中沒有匹配的元組，對應的結果將為 NULL。
- full outer join
	- 代數表示法：⟗
	- 描述：全外連接返回兩個表中的所有元組，對於沒有匹配的元組，對應的結果將為 NULL。
- nature join 
	- 代數表示法：⋈
	- 描述：自然連接是一種特殊的連接，它自動基於相同名稱的欄位進行連接。
### Set-Union Operation
- Notation
	- $R \cup S$
### Set-Intersection Operation
- Notation
	- $R \cap S$

### Set-Difference Operation
- Notation
	- R - S
### The Assignment Operation
- Notation
	- y←x
	- 將右邊的結果給到左邊
### The Rename Operation
- Notation
	- $\rho_{B(A_1,A_2)}(R)$
