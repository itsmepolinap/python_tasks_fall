import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '.\n'


def get_article(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_correct_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'correct_article.txt'))


def get_wrong_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'wrong_article.txt'))


def recover_article() -> str:
    wrong_article = get_wrong_article().split("\n")
 
    words = ""
    for sentence in wrong_article:
        art = []
        if not len(sentence):
            continue
        sentence = sentence.split()
        
        for word in sentence:
            exc = word.find("!")
            if exc != -1:
                word = word[:exc]
            word = word[::-1].lower()
            print(word)
            ind = word.find("woof-woof")
            if ind != -1:
                word = word[:ind] + "cat" + word[ind + len("woof-woof"):]
            art.insert(0, word)
        words += " ".join(art).capitalize() + ".\n"
        
    return words

print(recover_article())
