---
title: oslab15
tags:
  - os
---

# oslab15

>  mysort.c
```clike=
// 修改 mysort 函數，接受陣列和陣列大小作為參數，不再返回陣列
int* mysort(int arr[], int n) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;
        // 將比 key 大的元素向右移
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
    return arr;
}
```


>  lab1.c
```clike=
#include <stdio.h>
extern int* mysort();
int main() {
    int numbers[] = {5, 2, 9, 1, 5, 6};
    int n = sizeof(numbers) / sizeof(numbers[0]);
		int *re;
    // 使用 mysort 函數進行排序
    re=mysort(numbers, n);
    // 輸出排序後的結果
    printf("排序後的數字：");
    for (int i = 0; i < n; i++) {
        printf("%d ", re[i]);
    }
    return 0;
}
```

