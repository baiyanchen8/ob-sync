好的，以下是題目的 LaTeX 語法嵌入：

---

考慮兩個 $2 \times 2$ 的矩陣 $A$ 和 $B$。已知
$$
B^{-1} = \begin{bmatrix} 1 & 2 \\ 3 & 5 \end{bmatrix} 
$$
和
$$
 (AB)^{-1} = \begin{bmatrix} 1 & 3 \\ 2 & 5 \end{bmatrix} 
$$
求矩陣 $A$。

---

## 求解

$$(AB)^{-1}=B^{-1}A^{-1}=\begin{bmatrix} 1 & 2 \\ 3 & 5 \end{bmatrix}A^{-1}=\begin{bmatrix} 1 & 3 \\ 2 & 5 \end{bmatrix}$$

$$
A=(\begin{bmatrix} 1 & 2 \\ 3 & 5 \end{bmatrix}^{-1}\begin{bmatrix} 1 & 3 \\ 2 & 5 \end{bmatrix})^{-1}
=\begin{bmatrix} 1 & 3 \\ 2 & 5 \end{bmatrix}^{-1}\begin{bmatrix} 1 & 2 \\ 3 & 5 \end{bmatrix}
$$


$$
\left[\begin{array}{cc|cc}
1 & 3 & 1 & 0 \\
2 & 5 & 0 & 1 \\
\end{array}\right]
\xRightarrow{r_2\rightarrow r_2-2r_1} 
\left[\begin{array}{cc|cc}
1 & 3 & 1 & 0 \\
0 & -1 & -2 & 1 \\
\end{array}\right]
\xRightarrow{r_2\rightarrow -r_2} 
\left[\begin{array}{cc|cc}
1 & 3 & 1 & 0 \\
0 & 1 & 2 & -1 \\
\end{array}\right]
\xRightarrow{r_1\rightarrow r_1-3r_2} 
\left[\begin{array}{cc|cc}
1 & 0 & -5 & 3 \\
0 & 1 & 2 & -1 \\
\end{array}\right]
$$
$$
A=\begin{bmatrix} -5 & 3 \\ 2 & -1 \end{bmatrix}\begin{bmatrix} 1 & 2 \\ 3 & 5 \end{bmatrix}
=\begin{bmatrix} 4 & 5\\ -1 & -1 \end{bmatrix}
$$

