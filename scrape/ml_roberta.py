from transformers import pipeline
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

sentiment_analysis = pipeline("sentiment-analysis",model="siebert/sentiment-roberta-large-english")
print(sentiment_analysis("I love this!"))


def getSentiment_ml():
    with open("/home/ayush/myproj/vaahan/scrape/scrapeListFile.txt","r") as f:
        content = f.read()

        words = [word for word in content.split() if word.lower() not in ENGLISH_STOP_WORDS]
        new_text = " ".join(words)
        print(new_text)
        print("Old length: ", len(content))
        print("New length: ", len(new_text))