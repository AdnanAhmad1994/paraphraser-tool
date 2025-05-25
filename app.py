from flask import Flask, render_template, request, jsonify
import traceback

app = Flask(__name__)

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
        # Use the simple paraphraser instead of the ML model
        from simple_paraphraser import paraphrase_text
        
        # Get paraphrased text
        paraphrased_text = paraphrase_text(original_text)
        
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
