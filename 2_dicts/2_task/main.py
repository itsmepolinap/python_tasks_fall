import re


def top_10_most_common_words(text: str) -> dict[str, int]:
    """Функция возвращает топ 10 слов, встречающихся в тексте.

    Args:
        text: исходный текст

    Returns:
        словарь типа {слово: количество вхождений}
    """
    words_list = [word for word in re.findall(r'[а-я]*', text.lower()) if word and len(word)>=3]
    most_common = {}
    for word in words_list:
        if word in most_common:
            most_common[word]+=1
        else:
            most_common[word]=1
    spisok_par = list(most_common.items())
    spisok_par.sort(key = lambda para: (-para[1],para[0]))

    if len(spisok_par) > 10:
        spisok_par = spisok_par[:10]

    most_common = dict(spisok_par)
    return most_common
