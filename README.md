# Multimodal-Learning-Model-for-YouTube-Popularity
Machine Learning: Predicting Views from YouTube Video Titles Using Multimodal-Learning-Model

(Improved from the Bi-LSTM model, this was a homework assignment. I spent a week working on it, and have posted it here for those who might be interested to reference.)

## Expected Model Applications
It's well known that one of the most significant factors determining viewer traffic is the attractiveness of a video's thumbnail and title. This model aims to provide YouTubers with a way to test whether their video titles are catchy and competitive enough before the video's release. It prevents the disappointment of a video produced with great effort having low views due to an unattractive title or thumbnail. YouTubers can prepare several video titles in advance and use the model to predict which title will be the most eye-catching, thus expected to have the highest click rate. This ensures that their video titles are competitive enough!!!


## How to Use
### Collection of YouTube Video Data
```
# Use the Youtube_Crawler.py file to collect YouTube video data on your own
$ python Youtube_Crawler.py 
```

### Model Structure (Image-to-Image, Text-to-Text)
Using the concept of Multimodal-Learning-Model, an EfficientNetB0-based Visual model is used to process image data; a Bi-LSTM-based Social Model is used to process text data!
Finally, through the Merge Layer, the outputs of the Visual model and Social Model are fused to form the final Multimodal Model!
![image](https://user-images.githubusercontent.com/111637364/208354494-c602e24a-8fd5-4125-b103-08cfb1096822.png)

Concept of Multimodal-Learning-Model & Concept Diagram of YouTube Crawling
![image](https://user-images.githubusercontent.com/111637364/208354700-9e42a03f-a7d8-47f1-9603-96059a2254cb.png)

### Natural Language Processing (Segmentation + Word Vector)
```
# Use the _Word2Vec_visualization_3D.py file to process video titles as Word2Vec word vectors and visualize them
$ python _Word2Vec_visualization_3D.py
```
![word2Vec_gif](https://user-images.githubusercontent.com/111637364/186734029-2d3c3d5e-e059-4a75-82d3-3ac3eb5242c7.gif)

```
# Use the _Doc2Vec_visualization.py file to process video titles as Doc2Vec word vectors and visualize them
$ python _Doc2Vec_visualization.py 
```
![doc2Vec](https://user-images.githubusercontent.com/111637364/186747996-65ea93cc-5dc1-452b-8874-51aec3158ffe.jpg)


### Model Training
![image](https://user-images.githubusercontent.com/111637364/208354748-867413a9-9fcc-4d70-94a4-e39bbac6d023.png)


### Model Evaluation
Additionally, we collected video information from other channels to serve as our testing data!
![image](https://user-images.githubusercontent.com/111637364/208354955-6d6f5eed-c068-4b10-84a4-4c1d7bfe15db.png)
![image](https://user-images.githubusercontent.com/111637364/208355454-574b48e6-e176-40d5-8c2d-93fdc4d62c6a.png)
![image](https://user-images.githubusercontent.com/111637364/208355470-69b6782e-1125-4176-b280-6d290ec41f60.png)
![image](https://user-images.githubusercontent.com/111637364/208355480-b6748649-8299-4e76-be31-c9d68d6defb7.png)

### Model Prediction
```
# Use the Predict_Crawler.ipynb file, input a specific video ID to predict the click-through rate result
$ python Predict_Crawler.ipynb
```
![image](https://user-images.githubusercontent.com/111637364/187491916-8c2fb094-fa9c-4e23-99a9-6980a4db11b1.png)


