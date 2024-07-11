---
title: lec1
tags: [離散]

---
# 命題與真值表
> [!tip] define
> 凡是能判斷為 T or F 的敘述，稱為　proposition

| 符號                | 意義　　　　　　　　　　　　　　　　　　　　　　　　　　　　　.                  |
| ----------------- | ------------------------------------------------- |
| $\Leftrightarrow$ | 代表兩個敘述等價                                          |
| $\leftrightarrow$ | 條件命題(if($\rightarrow$) and only if($\leftarrow$)) |
| ～/-               | 否定                                                |
| $\land$           | and                                               |
| $\lor$            | or                                                |
| $\oplus$          | xor                                               |
## 命題基本定律表

| 定律名稱  | 表達式                                                          .    |
| ----- | ----------------------------------------------------------------- |
| 身分律   | $A \land \text{True} = A$                                         |
|       | $A \lor \text{False} = A$                                         |
| 零律    | $A \land \text{False} = \text{False}$                             |
|       | $A \lor \text{True} = \text{True}$                                |
| 交換律   | $A \land B = B \land A$                                           |
|       | $A \lor B = B \lor A$                                             |
| 結合律   | $(A \land B) \land C = A \land (B \land C)$                       |
|       | $(A \lor B) \lor C = A \lor (B \lor C)$                           |
| 分配律   | $A \land (B \lor C) = (A \land B) \lor (A \land C)$               |
|       | $A \lor (B \land C) = (A \lor B) \land (A \lor C)$                |
| 吸收律   | $A \land (A \lor B) = A$                                          |
|       | $A \lor (A \land B) = A$                                          |
| 德摩根定律 | $\neg(A \land B) = \neg A \lor \neg B$                            |
|       | $\neg(A \lor B) = \neg A \land \neg B$                            |
| 雙條件   | $A \leftrightarrow B = (A \rightarrow B) \land (B \rightarrow A)$ |
| 反演律   | $A \land \neg A = \text{False}$                                   |
|       | $A \lor \neg A = \text{True}$                                     |
|       |                                                                   |


# 量詞

| forall | `$\forall$` | $\forall$ |
| ------ | ----------- | --------- |
| exists | `\exists`   | $\exists$ |

| Statement        | When true?                               | When false?                               |
| ---------------- | ---------------------------------------- | ----------------------------------------- |
| $\forall x P(x)$ | When $P(x)$ is true for every $x$        | When $P(x)$ is false for at least one $x$ |
| $\exists x Q(x)$ | When $Q(x)$ is true for at least one $x$ | When $Q(x)$ is false for every $x$        |

# 命題推理
![[Pasted image 20240710040102.png]]
![[Pasted image 20240710040116.png]]

