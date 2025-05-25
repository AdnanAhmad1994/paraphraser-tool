from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Load a pre-trained model that's specifically fine-tuned for paraphrasing
# "Vamsi/T5_Paraphrase" is a community model fine-tuned for paraphrasing
tokenizer = AutoTokenizer.from_pretrained("Vamsi/T5_Paraphrase")
model = AutoModelForSeq2SeqLM.from_pretrained("Vamsi/T5_Paraphrase")

def paraphrase_text(text_to_paraphrase):
    """
    Paraphrases the input text using a pre-trained model fine-tuned for paraphrasing.
    """
    # This model expects a specific prefix for paraphrasing task
    input_text = "paraphrase: " + text_to_paraphrase + " </s>"

    # Encode the input text
    encoding = tokenizer.encode_plus(
        input_text,
        padding='max_length',
        max_length=256,
        truncation=True,
        return_tensors="pt"
    )
    input_ids = encoding["input_ids"]
    attention_mask = encoding["attention_mask"]

    # Generate paraphrased text with improved parameters
    with torch.no_grad():
        outputs = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_length=256,
            num_beams=5,
            num_return_sequences=1,
            temperature=1.0,
            top_k=50,
            top_p=0.95,
            early_stopping=True,
            no_repeat_ngram_size=2
        )
    
    # Decode the generated output
    paraphrased_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Return the paraphrased text, handling any empty results
    if not paraphrased_text.strip():
        return "Unable to generate paraphrase. Please try a different text or check model settings."
    return paraphrased_text

# Example usage:
if __name__ == "__main__":
    original_text = "The quick brown fox jumps over the lazy dog."
    paraphrased_version = paraphrase_text(original_text)
    print(f"Original: {original_text}")
    print(f"Paraphrased: {paraphrased_version}")
