#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def cyrillic_to_latin(word):
    symb = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
         'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
         'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
         'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
         'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    word = word.lower()
    result = ''

    for char in word:
        result += symb.get(char, char) 
    return result

def replace_chars(chars): #декоратор
    def decorator(func):
        def wrapper(word):
            for char in chars:
                word = word.replace(char, '-')
            word = '-'.join(filter(None, word.split('-')))
            return func(word)
        return wrapper
    return decorator

# Применяем декоратор со значениями chars="?!:;,. "
@replace_chars("?!:;,. ")
def decorated_cyrillic_to_latin(word):
    return cyrillic_to_latin(word)

result = decorated_cyrillic_to_latin(input('Введите фразу: '))
print(result)
