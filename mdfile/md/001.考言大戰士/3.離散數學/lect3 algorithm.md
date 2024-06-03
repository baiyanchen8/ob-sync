# Algorithms VS Information Sciences
## What is Algorithm ?
> [!TIp] defination
>  在有限步驟中解決數學問題的程序

- 簡單來說要有精確的輸入與輸出
 
## 演算法的重要性
- 執行程式的演算法
- 一個好的演算法會在有限的空間與時間內有效率的執行
	- 通常空間與時間是**互相拮抗**

# What is algorithm ?

> [!TIp] defination
>  在有限步驟中解決數學問題的程序

## 演算法的說明
- 文字描述
	- 缺點：沒有效率、容易出錯
- pseudo code （虛擬碼）
	- 一種介於文字描述與程式碼之間的敘述方式，會使用良好的定義與輸入輸出並且適合轉換為任何程式語言 
- 流程圖
>[!tips]- 演算法中重要的特性 
> **輸入（input）：**
> - 演算法有指定的一組輸入值。
> - 這些輸入值是演算法所需處理的初始數據。
> **輸出：**
> - 每組輸入值經由演算法處理後，會產生來自指定集合的輸出值。
> - 這些輸出值是問題的解答 
> **正確性：**
> - 演算法應該對每組輸入值產生正確的輸出值。
> - 這意味著，演算法的結果必須符合問題的期望解答。
> **有限性：**
> - 演算法的步驟必須明確定義。
> - 每一步操作都應該是確定且可執行的，並且演算法必須在有限的步驟內完成。
> **有效性：**
> - 演算法的每一步操作必須是可以精確執行且在有限的時間內完成的。
> - 這保證了演算法在實際操作中的可行性
> **普遍性：**
> - 演算法應該適用於所有所需解決形式的問題，而不僅僅是某一特定輸入值的集合。
> - 這確保演算法的廣泛應用性和通用性。

## Example of Algorithm
### Searching Problem
>[!question] searching problem
> 找出 element A 是否在 list 中

> [!check]- linear search
> **優點：** 易於實做、在未經排序的序列中為最優解
> **缺點：** 在有排序的資料中並非最快
> **時間複雜度：** $O(n)$
>```python
>def linear_search(list,target):
>	for i in range(len(list)):
>		if list(i) == target :
>				return i
>	return 0
>```

> [!check]- binary search
> **優點：** 易於實做、在經排序的序列中為最優解
> **缺點：** 要先對數據做排序
> **時間複雜度：** $O(log_2(n))$
> ```python
>def bin_search(lst, target):
>   # 假設list 小->大
>    left, right = 0, len(lst) - 1
>    
>    while left < right:
>        middle = (left + right) // 2
>        if lst[middle] == target:
>            return middle
>        elif lst[middle] < target:
>            left = middle + 1
>        else:
>            right = middle
>    
>   return -1  # 如果沒有找到目標值，返回 -1
>```
>   

### Optimization Problem
>[!question] Optimization problem
> 優化問題是指尋找滿足特定條件的最佳解決方案的問題。在這種問題中，通常存在一個目標函數，該函數需要最大化或最小化。
>**例如：** 最短路徑演算法

#### Greedy method貪婪演算法
> [!faq] Greedy
> 在每個步驟中選擇當下最好的解。
> **缺點：**  *不一定*會得到最優解，但可以得到j還不錯的解
> 

# Complexity of Algorithm （複雜度）
- 相近值
	- Big $O$ ：上限（程式最多跑多久）
	- $\Omega$ ：下限
	- $\theta$ ：夾擠

> [!note] Big $O$
> 目標函式　$f(x)$ 在 x 超過　k 後，皆會小於　$C\times g(x)$ 
> => $f(x)$  是 $O(g(x))$　

![[Drawing 2024-06-03 14.33.40.excalidraw]]

  