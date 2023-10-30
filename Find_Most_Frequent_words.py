from collections import Counter
import re

def find_most_frequent_words(paragraph, num_words):
    # Remove punctuation and convert to lowercase
    cleaned_paragraph = re.sub(r'[^\w\s]', '', paragraph.lower())
    
    # Split the paragraph into words
    words = cleaned_paragraph.split()
    
    # Count the occurrences of each word
    word_counts = Counter(words)
    
    # Get the most common words
    most_common_words = word_counts.most_common(num_words)
    
    return most_common_words

# Example usage
paragraph = "This is a test. This is only a test. Python is the best programming language."
num_words = 3
most_common_words = find_most_frequent_words(paragraph, num_words)

# Display the most frequent words and their counts
for word, count in most_common_words:
    print(f"{word}: {count}")
