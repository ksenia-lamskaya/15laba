#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def benchmark(func):
    import time
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))

    return wrapper


@benchmark
def fetch_webpage():
    import requests
    webpage = requests.get('https://google.com')


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
