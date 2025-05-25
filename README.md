# Text Paraphraser

A simple web application that paraphrases text using both rule-based and ML-based approaches.

## Features

- User-friendly web interface
- Real-time paraphrasing
- Two paraphrasing approaches:
  - Rule-based paraphrasing (fast and lightweight)
  - ML-based paraphrasing using Hugging Face Transformers (more advanced)

## Project Structure

- `app.py`: Flask web application
- `paraphraser_example.py`: ML-based paraphraser using Transformers
- `simple_paraphraser.py`: Rule-based paraphraser using synonym substitution
- `templates/index.html`: Web interface

## Installation

1. Clone this repository
2. Create a virtual environment (optional):
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install flask transformers torch
   ```

## Usage

1. Start the Flask application:
   ```
   python app.py
   ```
2. Open your browser and navigate to `http://127.0.0.1:5000`
3. Enter text in the input field and click "Paraphrase"

## Customization

You can modify the rule-based paraphraser by adding more synonyms to the `word_replacements` dictionary in `simple_paraphraser.py`.

For the ML-based approach, you can experiment with different models by changing the model name in `paraphraser_example.py`.

## License

MIT
