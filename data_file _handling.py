
import json
import re
from collections import Counter

# Count lines and words in text files
def count_lines_and_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        num_lines = len(lines)
        words = [word for line in lines for word in line.split()]
        num_words = len(words)
    return num_lines, num_words

# Find the most spoken languages
def most_spoken_languages(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    languages = [lang for country in data for lang in country.get('languages', [])]
    language_count = Counter(languages)
    return language_count.most_common(top_n)

# Find the most populated countries
def most_populated_countries(filename, top_n):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    countries = [{'country': country['name'], 'population': country['population']} for country in data]
    countries_sorted = sorted(countries, key=lambda x: x['population'], reverse=True)
    return countries_sorted[:top_n]

# Extract email addresses from a text file
def extract_emails(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    return emails

# Find the most common words
def find_most_common_words(text_or_file, top_n):
    if isinstance(text_or_file, str) and text_or_file.endswith('.txt'):
        with open(text_or_file, 'r', encoding='utf-8') as file:
            text = file.read()
    else:
        text = text_or_file
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = Counter(words)
    return word_count.most_common(top_n)

# Calculate similarity between texts
def clean_text(text):
    return re.sub(r'[^A-Za-z0-9\s]', '', text.lower())

def remove_support_words(text, stop_words_file):
    with open(stop_words_file, 'r', encoding='utf-8') as file:
        stop_words = set(file.read().split())
    words = text.split()
    return ' '.join(word for word in words if word not in stop_words)

def check_text_similarity(text1, text2, stop_words_file):
    text1_clean = clean_text(text1)
    text2_clean = clean_text(text2)
    text1_clean = remove_support_words(text1_clean, stop_words_file)
    text2_clean = remove_support_words(text2_clean, stop_words_file)
    text1_words = set(text1_clean.split())
    text2_words = set(text2_clean.split())
    common_words = text1_words.intersection(text2_words)
    total_words = text1_words.union(text2_words)
    similarity = len(common_words) / len(total_words)
    return similarity

# Count lines with specific terms in the Hacker News CSV
def count_lines_with_terms(file_path, terms):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    counts = {term: sum(1 for line in lines if re.search(term, line, re.IGNORECASE)) for term in terms}
    return counts

# Example usage for Exercises
# 1. Count lines and words in speeches
files = ['obama_speech.txt', 'michelle_obama_speech.txt', 'donald_speech.txt', 'melina_trump_speech.txt']
for file in files:
    lines, words = count_lines_and_words(f'./data/{file}')
    print(f'{file}: {lines} lines, {words} words')

# 2. Most spoken languages
print(most_spoken_languages(filename='./data/countries_data.json', top_n=10))

# 3. Most populated countries
print(most_populated_countries(filename='./data/countries_data.json', top_n=10))

# 4. Extract emails
emails = extract_emails('./data/email_exchange_big.txt')
print(f'Extracted Emails: {emails}')

# 5. Most common words
print(find_most_common_words('./data/romeo_and_juliet.txt', top_n=10))

# 6. Text similarity
with open('./data/michelle_obama_speech.txt', 'r', encoding='utf-8') as michelle_file, \
     open('./data/melina_trump_speech.txt', 'r', encoding='utf-8') as melina_file:
    michelle_text = michelle_file.read()
    melina_text = melina_file.read()
similarity = check_text_similarity(michelle_text, melina_text, './data/stop_words.txt')
print(f'Text Similarity: {similarity:.2%}')

# 7. Hacker News term counting
term_counts = count_lines_with_terms('./data/hacker_news.csv', ['python', 'javascript', 'java(?!script)'])
print(term_counts)
