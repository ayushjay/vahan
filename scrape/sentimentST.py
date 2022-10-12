#does sentiment analysis using spacyTextblob, producing same results as Textblob
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

""" 
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')
text = 'I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy.'
doc = nlp(text)
doc._.blob.polarity                            # Polarity: -0.125
doc._.blob.subjectivity                        # Subjectivity: 0.9
doc._.blob.sentiment_assessments.assessments   # Assessments: [(['really', 'horrible'], -1.0, 1.0, None), (['worst', '!'], -1.0, 1.0, None), (['really', 'good'], 0.7, 0.6000000000000001, None), (['happy'], 0.8, 1.0, None)]
doc._.blob.ngrams()   
 """

def getSentiment2():
    nlp = spacy.load('en_core_web_sm')
    nlp.add_pipe('spacytextblob')   
    with open("/home/ayush/myproj/vaahan/scrape/scrapeListFile.txt","r") as f:
        content = f.read()
        senAnalysis = nlp(content)
        polarity = round(senAnalysis._.blob.polarity * 5 + 5,2)
        subjectivity = senAnalysis._.blob.subjectivity
        if subjectivity <= 0.25:
            subjectivity = 'is not opinion-based'
        elif subjectivity <= 0.5:
            subjectivity = 'is somewhat opnion-based'
        elif subjectivity <= 0.75:
            subjectivity = 'is opinion-based'
        elif subjectivity <= 1:
            subjectivity = 'is highly opnion-based'   

        return polarity, subjectivity

print(getSentiment2())