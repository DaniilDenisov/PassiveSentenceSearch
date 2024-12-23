from flask import Flask, request, jsonify
from PassiveNLPFunctions import find_passive_nltk, find_passive_spacy

# Initialize Flask app
app = Flask(__name__)


# API route to get passive sentences
@app.route('/get_passive_nltk', methods=['POST'])
def get_passive_nltk():
    # Get JSON data from the request
    data = request.get_json()
    
    # Extract text from the request
    text = data.get('text', '')
    
    # Find passive sentences
    passive_sentences = find_passive_nltk(text)
    
    # Return the result as JSON
    return jsonify({"passive_sentences": passive_sentences})
    
@app.route('/get_passive_spacy', methods=['POST'])
def get_passive_spacy():
    # Get JSON data from the request
    data = request.get_json()
    
    # Extract text from the request
    text = data.get('text', '')
    
    # Find passive sentences
    passive_sentences = find_passive_spacy(text)
    
    # Return the result as JSON
    return jsonify({"passive_sentences": passive_sentences})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')