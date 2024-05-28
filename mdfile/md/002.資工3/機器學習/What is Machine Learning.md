---
title: What is Machine Learning
tags: [機器學習]

---

# What is Machine Learning
## 引言(名言佳句?)


>“Field of study that gives computers the ability to learn without being explicitly programmed"
>讓電腦無需明確程式設計即可學習的研究領域
>---Arthur Samuel(1959)

>“A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E.”
>“如果電腦程式在 T 中的任務中的表現（按 P 測量）隨著經驗 E 的提高而提高，則可以說它可以從關於某類任務 T 和性能測量 P 的經驗 E 中學習。”
---Tom Mitchell(1997)
### 範例
![](S1ppAPfzp.png)
從關於某類任務 T 和性能測量 P 的經驗 E 中學習
先通過E(training set)將 model 訓練好 → model 學習經驗
通過T(testing set)測驗 model 的P → 通過T得出效能P

### model training 流程圖
![](rkobbuff6.png)

## 四種mdeol類型

1. 監督學習 (Supervised Learning):
    - [[Classification]] [[Regression]]
        - 分類 (Classification):
                分類是一種監督學習任務，通常用於將數據點分為不同的類別或類別。它的目標是為每個輸入數據點分配一個預定義的類別標籤。常見的分類算法包括決策樹、支持向量機 (SVM)、K最近鄰 (K-Nearest Neighbors)、神經網絡等。
        - 回歸 (Regression):
            回歸也是一種監督學習任務，但與分類不同，它的目標是預測數值結果而不是類別標籤。通常，回歸用於建立一個模型，該模型可以預測連續性數值，例如價格、溫度、股票價格等。線性回歸和多項式回歸是常見的回歸技術，還有其他高級回歸方法。
    - 介紹: 
        在監督學習中，模型接受有標籤的訓練數據，其中每個數據點都有一個已知的正確答案（標  籤）。模型的目標是學習如何映射輸入數據到正確的輸出，以便在未見過的數據上進行預測。
    - 例子: 手寫數字識別，其中模型訓練於數字圖像和相對應的數字標籤。
    - 圖示 : 
         ![](SkvRu_zfp.png)
         ![](1Nf2tTTkALYq6RTMQmhjo1A.png)

    
    
2. 非監督學習 (Unsupervised Learning):
    - 介紹: 在非監督學習中，模型處理沒有標籤的數據，目標是發現數據中的結構、模式或群集。這種方法通常用於降維、集群分析和特徵提取。
    - 例子: K-均值聚類，該算法通過將數據點劃分為 K 個簇來識別模式。
    - 示意圖: ![](HkhpOdMGa.png)
        
3. 半監督學習 (Semi-Supervised Learning):

    - 介紹: 半監督學習結合了監督和非監督學習的元素。它使用少量有標籤的數據和大量無標籤的數據來進行訓練，以提高模型的性能。
    - 例子: 在文本分類中，您可能擁有一些文章有標籤，但大多數文章是無標籤的，半監督學習可用於提高分類性能。
    - 示意圖: (無標準示意圖，因為它是混合了監督和非監督學習的方法)
4. 強化學習 (Reinforcement Learning):

    - 介紹: 強化學習是一種學習方式，模型通過與環境互動，根據其行動而獲得的回饋信號來學習。目標是找到最佳策略，以最大化長期獎勵。
    - 例子: 機器人學習遊戲中的最佳策略，例如學習玩象棋或打電子遊戲。
    - 示意圖: Reinforcement Learning ![](500px-Reinforcement_learning_diagram.svg.png)
## The challenges of machine learning
- Challenges in data selection
    - 訓練資料不足
        - 通常需要數千條數據，有時甚至更多…
    - 訓練資料不具代表性
        - 選舉民調
    - 低品質
        - 異常值，缺乏特徵價值
    - 不相關的特徵
        - 要素過多
- Challenges in model selection
    - 過擬合 
        - model too complex
    - 未擬合
        - model too easy
![](SyXTh_Mfp.png)
