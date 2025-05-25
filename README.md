# Paraphraser Tool

A simple web application that allows you to paraphrase text using rule-based techniques.

## Features

- Easy-to-use web interface
- Fast text paraphrasing without requiring large models
- Synonym replacement and sentence restructuring
- Lightweight Flask backend

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/AdnanAhmad1994/paraphraser-tool.git
   cd paraphraser-tool
   ```

2. Set up a virtual environment (optional but recommended):
   ```
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. Install the required dependencies:
   ```
   pip install flask
   ```

## Usage

1. Start the Flask server:
   ```
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`

3. Enter the text you want to paraphrase in the "Original Text" field

4. Click the "Paraphrase" button to generate the paraphrased version

## How It Works

The paraphraser uses a rule-based approach:

1. Word replacement: Replaces words with synonyms (30% chance for each eligible word)
2. Sentence restructuring: Occasionally changes sentence structures
3. Preserves meaning: Maintains the original meaning while creating variations

This approach is lightweight and doesn't require downloading large machine learning models.

## Advanced Version

The repository also includes an ML-based paraphraser that uses the Hugging Face Transformers library. To use it:

1. Install additional dependencies:
   ```
   pip install transformers torch
   ```

2. Modify the `app.py` file to use `paraphraser_example.py` instead of `simple_paraphraser.py`

## License

MIT

## Author

Adnan Ahmad
