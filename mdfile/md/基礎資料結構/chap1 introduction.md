---
title: chap1 introduction
tags: [基礎資料結構]

---

# chap1 introduction
## 1.1系統的生命週期


- 系統生命週期
    - 系統從發想到寫成程式為系統生命週期
```mermaid
%%{init: {'theme':'dark'}}%%
graph LR;
需求-->分析-->設計-->coding-->驗證
```

## 1.2 指標和動態記憶體配置

### 1.2.1 指標

- `&`
    - 取地址
    ```c=1
    int main(){
        int a=0;
        printf("%d",&a);//會出現a在記憶體中的地址
    }
    ```
- `*`
    - 取值
    ```c=1
    int main(){
        int a=0;
        int *addr_a=&a;//在命名位址變數時必須在前面加*
        printf("%d",*addr_a);
    }
    ```

### 1.2.2 動態記憶體分配
#### malloc (分配記憶體)
`addr=(type *) malloc(length*siezof(type))`
#### realloc (重新分配記憶體，用於增加記憶體長度)
`new_addr=(type *) realloc(old_addr,new_length*siezof(type))`
#### 範例
```c=1
int main(int k,char *argv[]) {
	int *arr_addr;
	arr_addr= (int *)malloc(10*sizeof(int));
    // (type *) malloc(length*siezof(type))
    
	int i=0;
	for (i=0;i<10;i++){
		*(arr_addr+i)=i; 
        //在程式語言中，不需要去特別計算type長度，complier會幫你做好
        // ex: a[10] = 0 ， *(a+10) =0
	}
	for (i=0;i<10;i++){
		printf("%d : %d \n",i,*(arr_addr+i));
	}
	free(arr_addr);
    //程式結束前記得一定要free掉記憶體
    //雖然complier會幫你作，但這樣比較保險
    //在程式中最好將沒用到的記憶體free掉，以避免overflow
	return 0;
}
```
### 1.2.3 指標的潛在危險
假如指標指到<font color =dddd>NULL</font>就有可能出大事
## 1.3 演算法描述

### 1.3.1 簡介
- define
	-  演算法為一種固定的指令的集合，用於達成特定的效果。
- 條件
	- 輸入
	- 輸出
	- 明確性
	- 有限性
	- 有效性
### example
- [[排序演算法]]
- [[binsearch]] 
### 1.3.2 遞迴演算法
我懶得做了
## Exercise
1. [[Towers of Hanoi]]

## 1.4資料抽象化
除了char、int、float、double，還有array&structure
### define
抽象化資料型態(abstyract data type,ADT)是一種組織過的資料型態，組織過的資料型態，組織方式使我們得以將物件及其運算規格分開計算。


## 1.5 效能分析

### 1.5.1 空間複雜度
我懶得做了x2

### 1.5.2 時間複雜度
我懶得做了x3
### 1.5.3 漸進符號
我懶得做了x4
#### big o
$t=\mathcal{O}(g(n))$