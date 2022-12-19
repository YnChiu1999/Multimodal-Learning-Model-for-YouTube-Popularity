# Multimodal-Learning-Model-for-YouTube-Popularity
機器學習：利用Multimodal-Learning-Model訓練模型從YouTube影片封面及標題預測點閱數   
Machine Learning: Predicting Views from YouTube Video Titles Using Multimodal-Learning-Model

(由Bi-LSTM模型改良，某堂課的作業，丟上來供有興趣的先進們參考)
## 預期模型應用
眾所皆知，影片的封面圖以及標題是否吸睛即是決定能否吸引到觀眾流量的最大影響因素之一，此模型旨在提供給YouTuber在影片發佈之前事先測試自己的影片標題是否足夠吸睛、是否足夠具有競爭力，避免自己辛苦產出的影片卻因為封面和標題不夠吸引人而導致點閱數低下，YouTuber可預先準備數個影片標題，由模型來預測何項影片標題最為吸睛，預期點閱數最高，來確保自己的影片標題能夠具有足夠競爭力！


## 使用方式
### 模型架構（圖對圖、字對字）
運用Multimodal-Learning-Model概念，利用由EfficientNetB0構成的Visual model處理圖像資料；利用由Bi- LSTM構成的Social Model處理文字資料！
最後再透過Merge Layer融合Visual model, Social Model輸出，構成最終的Multimodal Model！
![image](https://user-images.githubusercontent.com/111637364/208354494-c602e24a-8fd5-4125-b103-08cfb1096822.png)

Multimodal-Learning-Model概念 & YouTube爬蟲概念圖
![image](https://user-images.githubusercontent.com/111637364/208354700-9e42a03f-a7d8-47f1-9603-96059a2254cb.png)

### 自然語言處理(斷詞+詞向量)
```
# 使用 _Word2Vec_visualization_3D.py 檔案，將影片標題作Word2Vec詞向量處理並作視覺化
$ python _Word2Vec_visualization_3D.py 
```
![word2Vec_gif](https://user-images.githubusercontent.com/111637364/186734029-2d3c3d5e-e059-4a75-82d3-3ac3eb5242c7.gif)

```
# 使用 _Doc2Vec_visualization.py 檔案，將影片標題作Doc2Vec詞向量處理並視覺化
$ python _Doc2Vec_visualization.py 
```
![doc2Vec](https://user-images.githubusercontent.com/111637364/186747996-65ea93cc-5dc1-452b-8874-51aec3158ffe.jpg)


### 訓練模型（Model Training）
![image](https://user-images.githubusercontent.com/111637364/208354748-867413a9-9fcc-4d70-94a4-e39bbac6d023.png)


### 評估分析（Model Evaluation）
另外蒐集其他頻道影片資訊，作為測試集(Testing data)！
![image](https://user-images.githubusercontent.com/111637364/208354955-6d6f5eed-c068-4b10-84a4-4c1d7bfe15db.png)

![image](https://user-images.githubusercontent.com/111637364/208354748-867413a9-9fcc-4d70-94a4-e39bbac6d023.png)


### 模型預測
```
# 使用 Predict_Crawler.ipynb 檔案，輸入特定影片ID作點閱率結果預測
$ python Predict_Crawler.ipynb
```
![image](https://user-images.githubusercontent.com/111637364/187491916-8c2fb094-fa9c-4e23-99a9-6980a4db11b1.png)

