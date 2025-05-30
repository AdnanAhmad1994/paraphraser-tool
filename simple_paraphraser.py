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
            'cloud': ['remote', 'distributed', 'networked', 'web-based'],
            'computing': ['processing', 'calculation', 'data processing', 'information technology'],
            'intelligence': ['intellect', 'reasoning', 'insight', 'cognitive ability'],
            'heuristics': ['guidelines', 'rules of thumb', 'practical methods', 'strategies'],
            'workloads': ['tasks', 'operations', 'processes', 'jobs'],
            
            # Verbs
            'affect': ['influence', 'impact', 'modify', 'shape'],
            'organized': ['arranged', 'structured', 'ordered', 'classified'],
            'makes': ['creates', 'produces', 'generates', 'forms'],
            'failed': ['underperformed', 'fallen short', 'been inadequate', 'not succeeded'],
            'emerged': ['appeared', 'surfaced', 'arisen', 'come forth'],
            'optimizing': ['improving', 'enhancing', 'refining', 'maximizing'],
            'allocate': ['assign', 'distribute', 'designate', 'apportion'],
            'manage': ['handle', 'control', 'administer', 'oversee'],
            
            # Adjectives
            'complex': ['complicated', 'intricate', 'sophisticated', 'multifaceted'],
            'dynamic': ['changing', 'fluid', 'evolving', 'adaptable'],
            'optimal': ['best', 'ideal', 'superior', 'prime'],
            'physical': ['tangible', 'material', 'concrete', 'actual'],
            'virtual': ['digital', 'simulated', 'online', 'computer-based'],
            'heterogeneous': ['diverse', 'varied', 'mixed', 'assorted'],
            'promising': ['potential', 'hopeful', 'encouraging', 'prospective'],
            'artificial': ['synthetic', 'manufactured', 'man-made', 'simulated'],
            
            # Phrases
            'there are': ['we find', 'one can observe', 'it contains', 'we see'],
            'significantly affect': ['greatly impact', 'considerably influence', 'substantially change', 'notably alter'],
            'recently': ['lately', 'in recent times', 'not long ago', 'in the near past'],
            'based on': ['founded on', 'derived from', 'grounded in', 'rooted in'],
        }
        
        # Sentence structure variations
        self.sentence_structures = [
            lambda s: f"In fact, {s.lower()}",
            lambda s: f"{s} indeed.",
            lambda s: s.replace("There are", "We observe"),
            lambda s: s.replace("Recently,", "In recent developments,"),
            lambda s: s.replace("that is", "which is"),
            lambda s: s.replace("and", "as well as"),
            lambda s: s,  # sometimes keep original structure
        ]
        
        # Phrase reorderings
        self.reorderings = [
            # "X and Y" -> "Y and X"
            (r'(\w+) and (\w+)', r'\2 and \1'),
            # "X, Y, and Z" -> "Z, X, and Y" 
            (r'(\w+), (\w+), and (\w+)', r'\3, \1, and \2'),
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
            
            # 2. Apply sentence structure variation (40% chance)
            if random.random() < 0.4:
                new_sentence = random.choice(self.sentence_structures)(new_sentence)
            
            # 3. Apply phrase reordering (20% chance)
            if random.random() < 0.2:
                reordering = random.choice(self.reorderings)
                new_sentence = re.sub(reordering[0], reordering[1], new_sentence)
            
            paraphrased_sentences.append(new_sentence)
        
        # Join sentences back together
        paraphrased_text = ' '.join(paraphrased_sentences)
        
        # Optional: Add/remove transition words (10% chance)
        transition_words = ['however', 'furthermore', 'additionally', 'moreover', 'consequently']
        if len(paraphrased_sentences) > 1 and random.random() < 0.1:
            sentence_index = random.randint(1, len(paraphrased_sentences) - 1)
            transition = random.choice(transition_words)
            paraphrased_sentences[sentence_index] = f"{transition.capitalize()}, {paraphrased_sentences[sentence_index].lower()}"
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
