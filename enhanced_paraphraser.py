import random
import re

class EnhancedParaphraser:
    """An enhanced rule-based paraphraser that produces more significant changes."""
    
    def __init__(self):
        # Word replacements (common words and their alternatives)
        self.word_replacements = {
            # Nouns
            'environment': ['ecosystem', 'setting', 'landscape', 'context'],
            'resources': ['assets', 'components', 'elements', 'capabilities'],
            'infrastructure': ['framework', 'foundation', 'structure', 'architecture'],
            'efficiency': ['effectiveness', 'performance', 'productivity', 'efficacy'],
            'sustainability': ['durability', 'resilience', 'viability', 'eco-friendliness'],
            'energy': ['power', 'fuel', 'electricity', 'resource'],
            'methods': ['approaches', 'techniques', 'procedures', 'strategies'],
            'machines': ['devices', 'equipment', 'systems', 'hardware'],
            'models': ['frameworks', 'architectures', 'designs', 'paradigms'],
            'tools': ['utilities', 'instruments', 'applications', 'solutions'],
            'decisions': ['choices', 'judgments', 'determinations', 'selections'],
            'techniques': ['methods', 'approaches', 'practices', 'procedures'],
            'cloud': ['remote', 'distributed', 'networked', 'virtualized'],
            'computing': ['processing', 'calculation', 'IT infrastructure', 'information processing'],
            'intelligence': ['intellect', 'reasoning', 'cognitive systems', 'smart technology'],
            'heuristics': ['guidelines', 'rules of thumb', 'practical methods', 'strategies'],
            'workloads': ['tasks', 'operations', 'processes', 'jobs'],
            'data': ['information', 'content', 'records', 'metrics'],
            'centers': ['facilities', 'installations', 'hubs', 'complexes'],
            'research': ['investigation', 'study', 'analysis', 'exploration'],
            'framework': ['structure', 'system', 'methodology', 'approach'],
            'aim': ['goal', 'objective', 'purpose', 'target'],
            'challenges': ['problems', 'difficulties', 'obstacles', 'hurdles'],
            'allocation': ['distribution', 'assignment', 'provisioning', 'apportionment'],
            'concerns': ['issues', 'considerations', 'worries', 'apprehensions'],
            'requirement': ['need', 'necessity', 'prerequisite', 'demand'],
            'consumption': ['usage', 'utilization', 'expenditure', 'depletion'],
            
            # Verbs
            'affect': ['influence', 'impact', 'modify', 'shape'],
            'organized': ['arranged', 'structured', 'ordered', 'classified'],
            'makes': ['creates', 'produces', 'generates', 'forms'],
            'failed': ['underperformed', 'fallen short', 'been inadequate', 'not succeeded'],
            'emerged': ['appeared', 'surfaced', 'arisen', 'come forth'],
            'optimizing': ['improving', 'enhancing', 'refining', 'maximizing'],
            'allocate': ['assign', 'distribute', 'designate', 'apportion'],
            'manage': ['handle', 'control', 'administer', 'oversee'],
            'address': ['tackle', 'resolve', 'handle', 'deal with'],
            'leads': ['results in', 'causes', 'drives', 'brings about'],
            'increase': ['growth', 'rise', 'escalation', 'surge'],
            'doubled': ['increased twofold', 'multiplied by two', 'grown by 100%', 'expanded dramatically'],
            'needs': ['requires', 'necessitates', 'demands', 'calls for'],
            'using': ['utilizing', 'employing', 'leveraging', 'applying'],
            'proposing': ['suggesting', 'recommending', 'presenting', 'putting forward'],
            
            # Adjectives
            'complex': ['complicated', 'intricate', 'sophisticated', 'multifaceted'],
            'dynamic': ['changing', 'fluid', 'evolving', 'adaptable'],
            'optimal': ['best', 'ideal', 'superior', 'prime'],
            'physical': ['tangible', 'material', 'concrete', 'actual'],
            'virtual': ['digital', 'simulated', 'online', 'cloud-based'],
            'heterogeneous': ['diverse', 'varied', 'mixed', 'assorted'],
            'promising': ['potential', 'hopeful', 'encouraging', 'prospective'],
            'artificial': ['synthetic', 'manufactured', 'simulated', 'machine-based'],
            'intelligent': ['smart', 'cognitive', 'AI-driven', 'automated'],
            'sustainable': ['eco-friendly', 'green', 'renewable', 'environmentally sound'],
            'large': ['substantial', 'significant', 'considerable', 'extensive'],
            'rising': ['increasing', 'growing', 'escalating', 'mounting'],
            'environmental': ['ecological', 'green', 'nature-related', 'planet-friendly'],
            'hybrid': ['combined', 'mixed', 'blended', 'dual'],
            
            # Phrases
            'there are': ['we find', 'one can observe', 'it contains', 'we see'],
            'significantly affect': ['greatly impact', 'considerably influence', 'substantially change', 'notably alter'],
            'recently': ['lately', 'in recent times', 'not long ago', 'in the near past'],
            'based on': ['founded on', 'derived from', 'grounded in', 'rooted in'],
            'that leads to': ['which results in', 'causing', 'leading to', 'triggering'],
            'by proposing': ['through the introduction of', 'by presenting', 'with the development of', 'via the creation of'],
            'will be': ['is projected to be', 'is expected to be', 'is anticipated to be', 'is forecasted to become'],
            'needs for': ['requires', 'necessitates', 'demands', 'calls for'],
            'the aim of': ['the objective of', 'the goal of', 'the purpose of', 'the intention behind'],
        }
        
        # Sentence transformations
        self.sentence_transformations = [
            # Passive to active voice
            (r'is ([\w]+ed) by', r'actively \1'),
            # Active to passive voice
            (r'([\w]+) ([\w]+s) the', r'the is \2ed by \1'),
            # Change sentence structure
            (r'(.*?) is to (.*?) by (.*?)', r'\3 enables \1 to \2'),
            # Invert sentence parts around conjunctions
            (r'(.*?) and (.*?)', r'\2 and \1'),
        ]
        
        # Sentence starters to completely restructure sentences
        self.sentence_starters = [
            "In the context of {topic}, {rest}",
            "With respect to {topic}, {rest}",
            "Regarding {topic}, {rest}",
            "As observed in {topic}, {rest}",
            "Considering {topic}, {rest}",
            "Studies show that in {topic}, {rest}",
            "Research indicates that {rest} in the domain of {topic}",
            "When analyzing {topic}, one finds that {rest}",
            "From the perspective of {topic}, {rest}",
            "It is notable that in {topic}, {rest}",
        ]
        
    def extract_topic(self, sentence):
        """Extract the likely topic of a sentence."""
        words = sentence.lower().split()
        for word in ['cloud', 'data', 'resource', 'energy', 'computing', 'sustainability']:
            if word in words:
                return word.capitalize()
        return "This context"
    
    def get_segments(self, text):
        """Break text into logical segments for major restructuring."""
        # Split by periods, question marks, and exclamation points
        segments = re.split(r'(?<=[.!?])\s+', text)
        return [s for s in segments if s.strip()]
        
    def paraphrase_segment(self, segment):
        """Apply transformations to a single segment (sentence or clause)."""
        # Skip empty segments
        if not segment.strip():
            return segment
            
        # 1. Word replacements (50% chance for each eligible word)
        words = segment.split()
        for i in range(len(words)):
            word_lower = words[i].lower().strip('.,;:!?()"\'')
            
            # Check if this word has replacements and we decide to replace it
            if word_lower in self.word_replacements and random.random() < 0.5:
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
        
        # Reconstruct the segment with word replacements
        new_segment = ' '.join(words)
        
        # 2. Apply sentence transformations (30% chance)
        if random.random() < 0.3:
            # Pick a random transformation
            transformation = random.choice(self.sentence_transformations)
            try:
                new_segment = re.sub(transformation[0], transformation[1], new_segment)
            except:
                # If transformation fails, keep the original
                pass
                
        # 3. Major restructuring (20% chance)
        if random.random() < 0.2:
            topic = self.extract_topic(new_segment)
            starter = random.choice(self.sentence_starters)
            # Remove the period if it exists at the end
            rest = new_segment.rstrip('.!?')
            # Make first letter lowercase for the "rest" part
            if rest:
                rest = rest[0].lower() + rest[1:]
            try:
                new_segment = starter.format(topic=topic, rest=rest) + "."
            except:
                # If formatting fails, keep the original
                pass
        
        return new_segment
        
    def paraphrase(self, text):
        """Thoroughly paraphrase the given text."""
        # Get segments (sentences)
        segments = self.get_segments(text)
        
        # Process each segment
        paraphrased_segments = [self.paraphrase_segment(segment) for segment in segments]
        
        # 4. Potentially reorder some segments (10% chance)
        if len(segments) > 1 and random.random() < 0.1:
            # Find segments that could be swapped without losing coherence
            idx1 = random.randint(0, len(paraphrased_segments) - 1)
            idx2 = random.randint(0, len(paraphrased_segments) - 1)
            if idx1 != idx2:
                paraphrased_segments[idx1], paraphrased_segments[idx2] = paraphrased_segments[idx2], paraphrased_segments[idx1]
        
        # 5. Add transition words between segments (40% chance if multiple segments)
        if len(segments) > 1:
            transition_words = ['Furthermore', 'Additionally', 'Moreover', 'In addition', 'Besides', 
                               'Similarly', 'Likewise', 'Consequently', 'As a result', 'Therefore',
                               'However', 'Nevertheless', 'On the other hand', 'In contrast', 'Conversely']
            
            for i in range(1, len(paraphrased_segments)):
                if random.random() < 0.4:
                    transition = random.choice(transition_words)
                    # Remove period from previous segment if it exists
                    if paraphrased_segments[i-1].endswith('.'):
                        paraphrased_segments[i-1] = paraphrased_segments[i-1][:-1] + ','
                    # Add transition to the beginning of this segment
                    paraphrased_segments[i] = f"{transition.lower()} {paraphrased_segments[i]}"
        
        # Join segments back together
        paraphrased_text = ' '.join(paraphrased_segments)
        
        return paraphrased_text

def paraphrase_text(text):
    """Function to interface with the enhanced paraphraser class."""
    paraphraser = EnhancedParaphraser()
    return paraphraser.paraphrase(text)

# Example usage
if __name__ == "__main__":
    original_text = "The quick brown fox jumps over the lazy dog."
    paraphrased = paraphrase_text(original_text)
    print(f"Original: {original_text}")
    print(f"Paraphrased: {paraphrased}")
