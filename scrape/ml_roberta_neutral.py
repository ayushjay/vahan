from transformers import pipeline
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
classifier = pipeline("text-classification", model="j-hartmann/sentiment-roberta-large-english-3-classes", return_all_scores=True,truncation=True)




def getSentiment_ml2():
    with open("/home/ayush/myproj/vaahan/scrape/scrapeListFile.txt","r") as f:
        content = f.read()

        words = [word for word in content.split() if word.lower() not in ENGLISH_STOP_WORDS]
        new_text = " ".join(words)
        #print(new_text)
        print("Old length: ", len(content))
        print("New length: ", len(new_text))
        print (classifier(content))
        
        sentiList = classifier(new_text)
        for d in sentiList:
            label = d['label']
        for d in sentiList:
            score = d['score']
        print (label)
        print (round(score* 100,2))
        
        


getSentiment_ml2()