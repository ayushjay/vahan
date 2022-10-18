from transformers import pipeline
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
"""
To solve error :token indices sequence length is longer than the specified maximum sequence length, we use truncation
"""



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
        return label, round(score* 100,2)
        #print (label)
        #print (round(score* 100,2))
        


getSentiment_ml()
