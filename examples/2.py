#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def benchmark(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return return_value

    return wrapper


@benchmark
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')

    return wrapper


@decorator_function
def hello_world():
    print('Hello world!')


if __name__ == '__main__':
    print('Пример №4')
    hello_world()

    print('\nПример №5')
    print('Done!')
    # fetch_webpage()

    print('\nПример №6')
    print(fetch_webpage('https://google.com'))
