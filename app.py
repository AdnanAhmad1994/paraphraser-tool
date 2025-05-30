from flask import Flask, render_template, request, jsonify
import traceback

app = Flask(__name__)

# Configuration
PARAPHRASER_TYPE = "enhanced"  # "simple", "enhanced", or "ml"

def get_paraphraser():
    """
    Returns the appropriate paraphraser function based on configuration.
    """
    if PARAPHRASER_TYPE == "ml":
        try:
            # Try to import the ML-based paraphraser
            from paraphraser_example import paraphrase_text
            print("Using ML-based paraphraser")
            return paraphrase_text
        except ImportError as e:
            print(f"Warning: ML dependencies not found: {str(e)}. Falling back to enhanced paraphraser.")
            from enhanced_paraphraser import paraphrase_text
            return paraphrase_text
    elif PARAPHRASER_TYPE == "enhanced":
        # Use the enhanced rule-based paraphraser
        print("Using enhanced rule-based paraphraser")
        from enhanced_paraphraser import paraphrase_text
        return paraphrase_text
    else:
        # Use the simple rule-based paraphraser
        print("Using simple rule-based paraphraser")
        from simple_paraphraser import paraphrase_text
        return paraphrase_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/paraphrase', methods=['POST'])
def paraphrase():
    data = request.get_json()
    original_text = data.get('text', '')
    
    if not original_text:
        return jsonify({'error': 'No text provided'}), 400
    
    try:
        # Get the appropriate paraphraser
        paraphrase_text = get_paraphraser()
        
        # Print debug info
        print(f"Received text for paraphrasing: {original_text[:50]}...")
        
        # Get paraphrased text
        paraphrased_text = paraphrase_text(original_text)
        
        print(f"Paraphrased result: {paraphrased_text[:50]}...")
        
        return jsonify({
            'original': original_text, 
            'paraphrased': paraphrased_text
        })
    except Exception as e:
        error_info = traceback.format_exc()
        print(f"Error during paraphrasing: {str(e)}")
        print(error_info)
        return jsonify({
            'error': str(e),
            'details': error_info
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
