def word_after_string_sequence(input_string, target_sequence):
    words = input_string.split()
    target_words = target_sequence.split()
    
    for i, word in enumerate(words):
        if words[i:i+len(target_words)] == target_words and i + len(target_words) < len(words):
            return words[i + len(target_words)]
    
    return None