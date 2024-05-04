---
title: chap6 graph
tags: [基礎資料結構]

---



# 圖的抽象資料型態
## 定義
圖由兩種基本物組成: 邊(edge)、節點(vertex)
而邊則有兩種型態(有無方向)

## 表現方式
一張圖通常是使用點集合與邊集合的方式表示(手寫)，而在程式實作中通常只使用edge set(看情況)

| graph | vertex        | edge                                |
| ----- | ------------- |:----------------------------------- |
| a     | 0,1,2,3       | (0,1),(0,2),(0,3),(1,2),(1,3),(2,3) |
| b     | 0,1,2,3,4,5,6 | (0,1),(0,2),(1,3),(1,4),(2,5),(2,6) |
| c     | 0,1,2         | <0,1>,<1,0>,<1,2>                   |

*tips:* 在有向圖中，edge set 中的紀錄也會有方向(通常由前指向後<前,後>)

## Constraints (通常禁止以下的內容)
1. self edge 
	指那些由A指向A的邊，也稱 self loop
	EX : (A,A)、<C,C>
		![[20240302_191947.jpg]]
1. multigraph
	擁有**多重邊**的圖即稱為 mutigraph
		![[multigraph.jpg]]
## 圖的各種表示法
### 相鄰矩陣 (Adjacency Matrix) 
假設共有 N 個 Vertex，使用一個N$\times$N的矩陣，並用0表示不相鄰、1表示相鄰。
>  **舉例**
	**使用$G_3$舉例**

| x\y  | 0   | 1   | 2   |
| --- |:--- | --- | --- |
| 0   | 0   | 1   | 0   |
| 1   | 1   | 0   | 0   |
| 2   | 0   | 1   | 0   |

*tips:* 在這裡有方向性(y$\rightarrow$x)

#### 優點
對於尋找A,B任意兩點之間是否相鄰非常快，只需要$O(1)$
#### 缺點
空間複雜度為$O(N^2)$，且所有需要遍歷的算法都需要比較大的時間複雜度

### 相鄰串列 (adjacency list)

### 相鄰多元串列 (Adjacency Multilist)

### 索引表 (Index Table)

# 圖的各種基本名詞
1. 完全圖 full graph
    > 
    一個有*n*個邊的無向圖中，最多可能有$\frac{n(n-1)}{2}$個邊(*握手問題*)，而一個擁有最多可能邊的無向圖則稱為無向圖
2. 子圖 sub-graph
    >  說明
    通過將原本的圖拆分，所獲得的圖即為 sub-graph
    ![](https://th.bing.com/th/id/R.143f05e877a98a5defd774e29b388cae?rik=z55otwB3FZ2Hbw&riu=http%3a%2f%2f3.bp.blogspot.com%2f-L7KQbEpYe6o%2fUs2MELwhrnI%2fAAAAAAAAB6M%2furqBoTOR7To%2fs1600%2fSubgraph.JPG&ehk=7mTflNxR9h9uNIZ813%2fLOfhRNT07RDwrwqi8i2lG8BE%3d&risl=&pid=ImgRaw&r=0)
3. 迴圈 circle
    >  說明
    由一段頭尾相同的路徑組成
    
4. 連通 connect
    >  說明
    指一張圖中，若u&v之間存在至少一條路徑，即為連通
    
5. 連通元件 connect components
    >  說明
    連通元件是指在一個圖形或網路中，能夠互相連接的元素或節點集合，這些元素之間可以透過路徑相互到達。
    
6. 強連通圖 strongly connected components
    >  說明
    強連通圖是指在*有向圖*中，任意兩個節點之間都存在互相到達的路徑，也就是說，圖中的任意兩個節點都是彼此可達的。
    
7. 弱連通圖 weak connected components
    >  說明
    如果將一個*有像圖*所有有向邊替換為無向邊之後的無向圖是連通的，則稱為弱連通圖。
    
8. 分支度
    >  說明
    1. 無向圖
>        所有相連邊的數量
    2. 有向圖
        有向圖的分支度分為入分支度 & 出分支度，就是將指向節點的邊&指出節點的邊分開計算。 
    


# 圖的基本運算

## Deepth First Search (深度優先算法)

從字面意義上可知，是優先探索深度的算法

```clike=
int visited[num_vertex]; // 假設 non visited 為 0 , visited 為1 
int edge [num_vertex][2];//假設未使用的edge內容為(-1,-1)
void dfs(int now){
    visited[now]=1;
    printf("%d ",now);
    int i;
    for (i=0;i<num_vertex;i++){
        if (edge[i][0]==-1 || edge[i][1]==-1)
            continue;
        if (edge[i][0]==now && visited[edge[i][1]]==0)
            dfs(edge[i][1]);
        if (edge[i][1]==now && visited[edge[i][0]]==0)
            dfs(edge[i][0]);
    }
}

```
## Breadth First Search

```clike=
int visited[num_vertex]; // 假設 non visited 為 0 , visited 為1 
int edge [num_vertex][2];//假設未使用的edge內容為(-1,-1)void bfs(int now){
void bfs(int now){
    addqueue(now);
    int tmp;
    while (queue){
        tmp = dequeue();
        if (tmp ==-1){
            break;
        }
        visited[tmp] = 1;
        printf ("%d ", tmp);
        int i;
        for (i = 0; i < num_vertex; i++){
            if (edge[i][0] == -1 || edge[i][1] == -1)
                continue;
            if (edge[i][0] == tmp && visited[edge[i][1]] == 0)
                addqueue(edge[i][1]);
            if (edge[i][1] == tmp && visited[edge[i][0]] == 0)
                addqueue(edge[i][0]);
        }
    }
}
```
## 連通元件
通過 dfs or bfs 尋找就可以了。
```clike=
void connected(){
    bfs();
}
```
##  生成樹
當選擇圖中一個頂點，然後使用某種算法遍歷所有頂點，把所有其中經歷的路徑記錄下來便是生成樹


## 雙連通元件(bi-connected components)
articulation point : 將*連通圖G*中某一*節點v*刪除會出現多個(>1)連通圖，該節點極為連接點(articulation point)

### low 公式
low(n)=min{dfn(n)
			,min{low(w)\|當w為n的child on dfs tree}
			,min{dfn(w)\|當(w,n)為back edge}}
### 如何決定 ariculation point
1. for root
	當有兩個分支時
2. for not root
	當tree 的下邊的low大於當前節點的dfn時

### code
```c=
#include <stdio.h>
#include <stdlib.h>
#define maxnode 100

int** edge;
int edgesize;
int node[maxnode];
int vist[maxnode];
int low_[maxnode];
int dfn = 0;
int v2[maxnode];

void addedge(int a, int b);
int checknode(int a, int b);
int dfs(int node);
int find_articulation(int node);
int main(int argc, char const *argv[]) {

	for (int i = 0; i < 10; i++) 
		node[i] = i + 1;
	
	addedge(1, 2);
	addedge(2, 3);
	addedge(1, 3);
	addedge(2, 4);
	addedge(2, 5);
	addedge(4, 5);
	addedge(3, 6);
	printf("Edges:\n");

	for (int i = 0; i < edgesize; i++) 
		if (edge[i] != NULL) 
			printf("%d %d\n", edge[i][0], edge[i][1]);
	
	dfs(1);
	printf("\nNodes:\n");
	for (int i = 0; i < maxnode && node[i] != 0; i++) 
		printf("%d ", node[i]);

	printf("\nLow values:\n");
	for (int i = 0; i < maxnode && node[i] != 0; i++) 
	printf("%d ", low_[i]);

	printf("\ndfn:\n");
	for (int i = 0; i < maxnode && node[i] != 0; i++) 
		printf("%d ", vist[i]);

	printf("\nfind all articulation point\n");
	find_articulation(1);
	printf("\n");

// Free allocated memory
	for (int i = 0; i < edgesize; i++) 
		free(edge[i]);
	free(edge);
	return 0;
}

int find_articulation(int node){
	v2[node]=1;
	for (int i = 0; i < edgesize; i++) 
	{
		if (edge[i] == NULL) break;

		if ((edge[i][0] == node && v2[edge[i][1]] == 0)) 
		{
			int below = find_articulation(edge[i][1]);
			
			if (below >= vist[node] &&vist[node]!=1) 
			{	// 當下方的low大於等於當前的dfn時即為 articulation point 
				printf("%d ",node);
				return low_[node];
			}
		} else if ((edge[i][1] == node && v2[edge[i][0]] == 0)) 
		{	// 當下方的low大於等於當前的dfn時即為 articulation point 
			int below = find_articulation(edge[i][0]);

			if (below >= vist[node] &&vist[node]!=1) 
			{
				printf("%d ",node);
				return low_[node];
			}
		}

	}
	// 回傳low
	return low_[node];
}

int dfs(int node) {
	printf("%d ", node);
	vist[node] = ++dfn;
	int nowdfn=dfn;
	int small = dfn;
	for (int i = 0; i < edgesize; i++) 
	{
		if (edge[i] == NULL) break;

		if ((edge[i][0] == node && vist[edge[i][1]] == 0)) 
		{
			int below = dfs(edge[i][1]);
			if (small > below) small = below;

		} else if ((edge[i][1] == node && vist[edge[i][0]] == 0)) 
		{

			int below = dfs(edge[i][0]);
			if (small > below) small = below;

		} else if (edge[i][1] == node || edge[i][0] == node) 
		{ //處理backedge

			int below = (edge[i][0] == node) ? vist[edge[i][1]] : vist[edge[i][0]];
			if (small > below&&below!=(nowdfn-1)) small = below;
		}

	}

	low_[node] = small;
	return low_[node];
}

int checknode(int a, int b) {
	if (a == 0 || b == 0) return 0;
	for (int i = 0; i < maxnode; i++) {
		if (node[i] == 0) node[i] = (a == 0) ? b : a;
		if (node[i] == a) a = 0;
		if (node[i] == b) b = 0;
	}
	return (a == 0 && b == 0) ? 1 : 0;
}
void addedge(int a, int b) {
	if (!checknode(a, b)) {
		printf("Warning there is an invalid pair! %d %d \n", a, b);
		return;
	}
	if (edge == NULL || edgesize == 0) {
		edgesize = 10;
		edge = (int**)malloc(edgesize * sizeof(int*));
		for (int i = 0; i < edgesize; i++) {
			edge[i] = NULL;
		}
	}
	for (int i = 0; i < edgesize; i++) {
		if (edge[i] == NULL) {
			edge[i] = (int*)malloc(2 * sizeof(int));
			edge[i][0] = a;
			edge[i][1] = b;
			return;
		}
		if ((edge[i][0] == a && edge[i][1] == b) || (edge[i][0] == b && edge[i][1] == a)) {
			return;
		}
	}
	edgesize *= 2;
	edge = (int**)realloc(edge, edgesize * sizeof(int*));
	for (int i = edgesize / 2; i < edgesize; i++) {
		edge[i] = NULL;
	}
	addedge(a, b);
}
```
# 最小花費生成樹(Minimum cost spanning tree)
## greedy method（貪婪）
簡單而言，就是**每次**選擇最短的的路徑，直到所有點都被連通為止。
### 缺點
不夠好，不夠精確，有可能造成 Cycle
## kruskal's algorithm
1. 將所有 edge 按照由小到大排序
2. 然後要將所有edge 一個一個選出(要避免cycle)


# 最短路徑與遞移封閉


# 活動網路

