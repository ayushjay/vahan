"""
Flair is a pre-trained embedding-based model.
This means that each word is represented inside a vector space. 
Words with vector representations most similar to another word are often used in the same context. 
This allows us, to, therefore, determine the sentiment of any given vector, and therefore, any given sentence. 
The embeddings are based on this paper if you are curious about the more technical aspects.
Flair tends to be much slower than its rule-based counterparts but comes at the advantage of being a trained NLP model instead of a rule-based model, which, if done well comes with added performance. 
"""
from flair.models import TextClassifier
from flair.data import Sentence
sia = TextClassifier.load('en-sentiment')
"""
def flair_prediction(x):
    sentence = Sentence(x)
    sia.predict(sentence)
    score = sentence.labels[0]
    if "POSITIVE" in str(score):
        return "pos"
    elif "NEGATIVE" in str(score):
        return "neg"
    else:
        return "neu"
#df["sentiment"] = df["reviews.text"].apply(flair_prediction)
"""

def getSentiment3():
    with open("/home/ayush/myproj/vaahan/scrape/scrapeListFile.txt","r") as f:
        content = f.read()  
        flair_analysis = Sentence(content)
        sia.predict(flair_analysis)
        score = flair_analysis.labels[0]

        return score

print(getSentiment3())
