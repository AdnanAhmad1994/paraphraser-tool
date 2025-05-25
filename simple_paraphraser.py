import random
import re

class SimpleParaphraser:
    """A simple rule-based paraphraser that uses predefined patterns and synonyms."""
    
    def __init__(self):
        # Word replacements (common words and their alternatives)
        self.word_replacements = {
            # Nouns
            'environment': ['ecosystem', 'setting', 'domain', 'context'],
            'resources': ['assets', 'components', 'elements', 'capabilities'],
            'infrastructure': ['framework', 'foundation', 'structure', 'architecture'],
            'efficiency': ['effectiveness', 'performance', 'productivity', 'efficacy'],
            'sustainability': ['durability', 'resilience', 'viability', 'eco-friendliness'],
            'energy': ['power', 'fuel', 'force'],
            'methods': ['approaches', 'techniques', 'procedures', 'strategies'],
            'machines': ['devices', 'equipment', 'systems', 'hardware'],
            'models': ['frameworks', 'structures', 'designs', 'patterns'],
            'tools': ['utilities', 'instruments', 'mechanisms', 'applications'],
            'decisions': ['choices', 'judgments', 'determinations', 'selections'],
            'techniques': ['methods', 'approaches', 'practices', 'procedures'],
            
            # Verbs
            'affect': ['influence', 'impact', 'modify', 'shape'],
            'organized': ['arranged', 'structured', 'ordered', 'classified'],
            'makes': ['creates', 'produces', 'generates', 'forms'],
            'failed': ['underperformed', 'fallen short', 'been inadequate', 'not succeeded'],
            'emerged': ['appeared', 'surfaced', 'arisen', 'come forth'],
            'optimizing': ['improving', 'enhancing', 'refining', 'maximizing'],
            
            # Adjectives
            'complex': ['complicated', 'intricate', 'sophisticated', 'multifaceted'],
            'dynamic': ['changing', 'fluid', 'evolving', 'adaptable'],
            'optimal': ['best', 'ideal', 'superior', 'prime'],
            'physical': ['tangible', 'material', 'concrete', 'actual'],
            'virtual': ['digital', 'simulated', 'online', 'computer-based'],
            'heterogeneous': ['diverse', 'varied', 'mixed', 'assorted'],
            'promising': ['potential', 'hopeful', 'encouraging', 'prospective'],
            
            # Phrases
            'there are': ['we find', 'one can observe', 'it contains', 'we see'],
            'significantly affect': ['greatly impact', 'considerably influence', 'substantially change', 'notably alter'],
            'recently': ['lately', 'in recent times', 'not long ago', 'in the near past'],
        }
        
        # Sentence structure variations
        self.sentence_structures = [
            lambda s: f"In fact, {s.lower()}",
            lambda s: f"{s} indeed.",
            lambda s: s.replace("There are", "We observe"),
            lambda s: s.replace("Recently,", "In recent developments,"),
            lambda s: s,  # sometimes keep original structure
        ]
        
    def paraphrase(self, text):
        """Paraphrase the given text using word replacements and structure changes."""
        # Split text into sentences
        sentences = re.split(r'(?<=[.!?])\s+', text)
        paraphrased_sentences = []
        
        for sentence in sentences:
            if not sentence.strip():
                continue
                
            # 1. Word replacements (30% chance for each eligible word)
            words = sentence.split()
            for i in range(len(words)):
                word_lower = words[i].lower().strip('.,;:!?()"\'')
                
                # Check if this word has replacements and we decide to replace it
                if word_lower in self.word_replacements and random.random() < 0.3:
                    # Choose a replacement
                    replacement = random.choice(self.word_replacements[word_lower])
                    
                    # Preserve capitalization
                    if words[i][0].isupper():
                        replacement = replacement.capitalize()
                    
                    # Preserve punctuation
                    for char in ',.:;!?()"\'-':
                        if words[i].endswith(char):
                            replacement += char
                            break
                    
                    words[i] = replacement
            
            # Reconstruct the sentence
            new_sentence = ' '.join(words)
            
            # 2. Apply sentence structure variation (50% chance)
            if random.random() < 0.5:
                new_sentence = random.choice(self.sentence_structures)(new_sentence)
            
            paraphrased_sentences.append(new_sentence)
        
        # Join sentences back together
        paraphrased_text = ' '.join(paraphrased_sentences)
        
        return paraphrased_text

def paraphrase_text(text):
    """Function to interface with the paraphraser class."""
    paraphraser = SimpleParaphraser()
    return paraphraser.paraphrase(text)

# Example usage
if __name__ == "__main__":
    original_text = "The quick brown fox jumps over the lazy dog."
    paraphrased = paraphrase_text(original_text)
    print(f"Original: {original_text}")
    print(f"Paraphrased: {paraphrased}")
