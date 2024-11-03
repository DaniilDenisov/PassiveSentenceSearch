from flask import Flask, request, jsonify
import spacy

# Initialize Flask app
app = Flask(__name__)

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to find passive sentences
def find_passive_sentences(text):
    doc = nlp(text)
    passive_sentences = []
    
    for sent in doc.sents:
        for token in sent:
            if token.dep_ == "auxpass" or token.dep_ == "nsubjpass":
                passive_sentences.append(sent.text)
                break
    return passive_sentences

# API route to get passive sentences
@app.route('/get_passive_sentences', methods=['POST'])
def get_passive_sentences():
    # Get JSON data from the request
    data = request.get_json()
    
    # Extract text from the request
    text = data.get('text', '')
    
    # Find passive sentences
    passive_sentences = find_passive_sentences(text)
    
    # Return the result as JSON
    return jsonify({"passive_sentences": passive_sentences})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
