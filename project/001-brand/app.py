from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Function to load words from a file
def load_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()  # Read lines and remove trailing newlines
    return words

# Load adjectives and nouns from external files
adjectives = load_words('adjectives.txt')
nouns = load_words('nouns.txt')
# Function to generate a random band name
def generate_band_name():
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adj} {noun}"

# Route to serve the main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# API route to generate a band name
@app.route('/generate', methods=['GET'])
def get_band_name():
    band_name = generate_band_name()
    return jsonify({"band_name": band_name})

if __name__ == "__main__":
    app.run(debug=True)
