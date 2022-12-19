# Multimodal-Learning-Model-for-YouTube-Popularity
機器學習：利用Multimodal-Learning-Model訓練模型從YouTube影片封面及標題預測點閱數   
Machine Learning: Predicting Views from YouTube Video Titles Using Multimodal-Learning-Model

(由Bi-LSTM模型改良，某堂課的作業，丟上來供有興趣的先進們參考)
## 預期模型應用
眾所皆知，影片的封面圖以及標題是否吸睛即是決定能否吸引到觀眾流量的最大影響因素之一，此模型旨在提供給YouTuber在影片發佈之前事先測試自己的影片標題是否足夠吸睛、是否足夠具有競爭力，避免自己辛苦產出的影片卻因為封面和標題不夠吸引人而導致點閱數低下，YouTuber可預先準備數個影片標題，由模型來預測何項影片標題最為吸睛，預期點閱數最高，來確保自己的影片標題能夠具有足夠競爭力！


## 使用方式
### 模型架構（圖對圖、字對字）
運用Multimodal-Learning-Model概念，利用由EfficientNetB0構成的Visual model處理圖像資料；利用由Bi- LSTM構成的Social Model處理文字資料！
![image](https://user-images.githubusercontent.com/111637364/208354494-c602e24a-8fd5-4125-b103-08cfb1096822.png)



```
# 將爬取到的資料透過 model_F.py 檔案來作模型訓練
$ python model_F.py
```
![image](https://user-images.githubusercontent.com/111637364/187491703-e687ca21-2fa6-4679-8d1d-18260481f12c.png)
![image](https://user-images.githubusercontent.com/111637364/187491716-1692db3a-0110-4d51-892c-35445b7c1038.png)


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


### 模型預測
```
# 使用 github_predict.py 檔案，輸入特定影片ID作點閱率結果預測
$ python github_predict.py
```
![image](https://user-images.githubusercontent.com/111637364/187491916-8c2fb094-fa9c-4e23-99a9-6980a4db11b1.png)

