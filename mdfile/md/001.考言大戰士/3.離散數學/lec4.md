# 同餘方程 （Divisibility and Modular Arithmetic）
$$\huge{a\ mod\ b = c \ mod\  b} $$
## Define---Division
if "a" can be divised by "b" , that means exist  a "c" that $a=b\times c$.
$A|C$ is True means  C 可以被 A 整除

> [!Note]- Example
> $3|7$ is False
> $3|12$ is True

## Therom---Properties of Divisibility
1. if $\ a|b\ \& \ a|c \Rightarrow a|(b+c)$
2. if $a|b$ => $a|bc$  for all c in interger
3. if $a|b$ and $b|c$ => $a|c$

> [!note]- Example
> Proof that if $a|b$ and $b|c$ that $a|c$
> >$a|b$ => $ap =b$,p is interger
> > $b|c$ => $bx=c$,x is interger
> > $apx=c$ => $a|c$  

## Define---Division Algorithm
a=dq+r
q= a **div** d , r = a **mod** d
d is called the divisor.
a is called the dividend.
q is called the quotient.
r is called the remainder. (餘數一定要是正數)

> [!note]- exmaple-1
> what are the quotient and remainder when -11 is divided by 3
> -11 = 3 \*(-4)+1
> ans => -4 & 1

## Define---Congurence Relation（同餘）
$a\equiv b(mod\ m)$ => m|(a-b) => $\frac{a-b}{m}=int$
## Theorm---同餘???定理
Let m be a positive integer. The integers a and b are congruent modulo such that Let m be a positive integer. The integers a and b are congruent modulo m if and only if there is an integer k such that a = b + km.


> [!question] if $a\equiv b\ (mod\ m)$ and $c\equiv d\ (mod\ m)$ that$ac\equiv bd\ (mod\ m)$ and $(a+c)\equiv (b+d)\ (mod\ m)$
>  > [!note] proof
>  >  a=im+b ,c =jm+d
>  >  a+c=m(i+j)+b+d => $(a+c)\equiv (b+d)\ (mod\ m)$
>  >  $ac=ijm^2+imd+jmb+db=(ijm+id+jb)\times m+db$
>  >  =>$ac\equiv bd\ (mod\ m)$

![[Pasted image 20240612220758.png]]

12 mod 19

| q   | a   | b   | r   | s1  | s2  | s   | t1  | t2  | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 12  | 19  | 12  | 1   | 0   | 1   | 0   | 1   | 0   |
| 1   | 19  | 12  | 7   | 0   | 1   | -1  | 1   | 0   | 1   |
| 1   | 12  | 7   | 5   | 1   | -1  | 2   | 0   | 1   | -1  |
| 1   | 7   | 5   | 2   | -1  | 2   | -3  | 1   | -1  | 2   |
| 2   | 5   | 2   | 1   | 2   | -3  | 8   | -1  | 2   | -5  |
| 2   | 2   | 1   | 0   | -3  | 8   |     | 2   | -5  |     |
|     | 1   | 0   |     | 8   |     |     | -5  |     |     |
