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
def hanoi(n, a, b, c):
	if n == 1:
		print(a, '-->', c)
	else:
		hanoi(n - 1, a, c, b)
		hanoi(1    , a, b, c)
		hanoi(n - 1, b, a, c)
# 调用
if __name__ == '__main__':
	hanoi(5, 'A', 'B', 'C')
```

總即動次數:
$$
T(n)=T(n-1)+T(1)+T(n-1),T(1)=1
$$
$$T(n)=2^n-1$$
