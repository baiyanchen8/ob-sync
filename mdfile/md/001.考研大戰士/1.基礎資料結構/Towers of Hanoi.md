---
title: Towers of Hanoi
tags: [基礎資料結構, 練習題]

---

# Towers of Hanoi
有三根杆子A，B，C。A杆上有 N 個 (N>1) 穿孔圓盤，盤的尺寸由下到上依次變小。要求按下列規則將所有圓盤移至 C 杆
1. 每次只能移動一個圓盤
2. 大盤不能疊在小盤上面

Ｑ：試求完成的最少次數


```python=
count=0
def hanoi(n, source, target, auxiliary):
    global count
    
    if n > 0:
        count+=1
        # 将 n-1 个圆盘从源杆移动到辅助杆
        hanoi(n-1, source, auxiliary, target)
        
        # 将第 n 个圆盘从源杆移动到目标杆
        print(f"Move disk {n} from {source} to {target}")
        # 将 n-1 个圆盘从辅助杆移动到目标杆
        hanoi(n-1, auxiliary, target, source)
# 测试
n = 7 # 圆盘的数量
hanoi(n, 'A', 'C', 'B')
print(count)

```