import spacy
import nltk
from nltk import word_tokenize, sent_tokenize, pos_tag

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def find_passive_spacy(text):
    doc = nlp(text)
    passive_sentences = []
    
    for sent in doc.sents:
        # Flag to track passive detection in sentence
        passive = False
        
        # Check for common passive dependencies
        for token in sent:
            if token.dep_ == "auxpass" or token.dep_ == "nsubjpass":
                passive_sentences.append(sent.text)
                passive = True
                break
        
        # If no passive detected, look for "to be" + past participle or "being" + past participle
        if not passive:
            for token in sent:
                # Detect infinitive passive (e.g., "to be promoted")
                if token.text == "to" and token.head.lemma_ == "be" and token.head.dep_ == "xcomp":
                    if any(child.dep_ == "acl" or child.dep_ == "relcl" for child in token.head.children):
                        passive_sentences.append(sent.text)
                        break
                
                # Detect gerund passive (e.g., "being interviewed")
                if token.lemma_ == "be" and token.dep_ == "aux" and token.head.dep_ == "acl":
                    passive_sentences.append(sent.text)
                    break
                    
    return passive_sentences
    

def find_passive_nltk(text):
    # Split the input text into sentences
    sentences = sent_tokenize(text)
    passive_sentences = []
    
    for sentence in sentences:
        tokens = word_tokenize(sentence)
        pos_tags = pos_tag(tokens)
        
        # Flag for identifying passive sentences
        is_passive = False
        
        # Check for passive voice patterns
        for i in range(len(pos_tags) - 1):
            word, tag = pos_tags[i]
            next_word, next_tag = pos_tags[i + 1]
            
            # Simple passive (be + VBN)
            if tag.startswith('VB') and word.lower() in ["is", "was", "were", "are", "been", "being", "be"]:
                if next_tag == "VBN":
                    is_passive = True
                    break
            
            # Infinitive passive (to be + VBN)
            if word.lower() == "to" and next_word.lower() == "be" and i + 2 < len(pos_tags) and pos_tags[i + 2][1] == "VBN":
                is_passive = True
                break
            
            # Gerund passive (being + VBN)
            if word.lower() == "being" and next_tag == "VBN":
                is_passive = True
                break
        
        # Check for agent (by + noun) in passive sentences
        if is_passive:
            for i in range(len(pos_tags) - 1):
                word, tag = pos_tags[i]
                next_word, next_tag = pos_tags[i + 1]
                
                # If we find "by" and a noun (agent), it's likely passive
                if word.lower() == "by" and next_tag in ["NN", "NNS", "NNP", "NNPS"]:
                    passive_sentences.append(sentence)
                    break
            else:
                # If no "by" phrase found, still consider it passive
                passive_sentences.append(sentence)
    
    return passive_sentences

