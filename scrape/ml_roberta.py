"""Pipeline performs all pre-processing and post-processing steps on your input text data. 
it performs some pre-processing steps like converting text into numerical values and post-processing 
steps like generating sentiment of a text and these steps may vary depending upon the task of a pre-trained model.
"""

from transformers import pipeline
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
"""
To solve error :token indices sequence length is longer than the specified maximum sequence length, we use truncation
"""


"""Truncation=True for specfied length"""
sentiment_analysis = pipeline("sentiment-analysis",model="siebert/sentiment-roberta-large-english",truncation=True)
#print(sentiment_analysis("I love this!"))





def getSentiment_ml():
    with open("/home/ayush/myproj/vaahan/scrape/scrapeListFile.txt","r") as f:
        content = f.read()

        words = [word for word in content.split() if word.lower() not in ENGLISH_STOP_WORDS]
        new_text = " ".join(words)
        #print(new_text)
        print("Old length: ", len(content))
        print("New length: ", len(new_text))
        #print (sentiment_analysis(content))
        
        sentiList = sentiment_analysis(new_text)
        for d in sentiList:
            label = d['label']
        for d in sentiList:
            score = d['score']
        return label, round(score* 10,2)
        #print (label)
        #print (round(score* 100,2))
        


getSentiment_ml()
