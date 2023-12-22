#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Hello:
    pass


def hello_world():
    print('Hello world!')


def wrapper_function():
    def hello_world1():
        print('Hello world!')
    hello_world1()


def higher_order(func):
    print(f'Получена функция {func} в качестве аргумента')
    func()
    return func


if __name__ == '__main__':
    print('Пример №1')
    print(type(hello_world()))
    print(type(Hello))
    print(type(10))

    print('\nПример №2')
    wrapper_function()

    print('\nПример №3')
    higher_order(hello_world)
