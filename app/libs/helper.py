
def is_isbn_or_key(word):
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in short_word and short_word.isdigit() and len(short_word) == 10:
        isbn_or_key = 'isbn'
    return isbn_or_key
