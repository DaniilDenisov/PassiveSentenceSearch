import spacy
# Function to find passive sentences

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def find_passive_sentences(text):
    doc = nlp(text)
    passive_sentences = []
    
    for sent in doc.sents:
        for token in sent:
            if token.dep_ == "auxpass" or token.dep_ == "nsubjpass":
                passive_sentences.append(sent.text)
                break
    return passive_sentences