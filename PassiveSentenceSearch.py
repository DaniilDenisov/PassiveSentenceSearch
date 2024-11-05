from flask import Flask, request, jsonify
from PassiveNLPFunctions import find_passive_sentences

# Initialize Flask app
app = Flask(__name__)


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
    app.run(debug=True, host='0.0.0.0')