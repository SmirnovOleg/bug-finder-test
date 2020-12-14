import collections
import os
from typing import List

import numpy as np


def test_log(x):
    return np.log(x + 1)


def test_callable(f):
    return isinstance(f, collections.Callable)


def test_arange(n):
    return np.array(range(n))


def test_assert(self, x):
    self.assertIs(x, True)


def test_dict_keys(vocab):
    for i in range(len(vocab.keys())):
        print(i)
    sorted_keys = sorted(vocab.keys())
    return sorted_keys


def test_os_path_exists(path):
    os.mkdir(path)
    return os.path.exists(path)


def iterate_and_print_even_items(data: List[int]):
    print('Start working...')
    for i in range(len(data)):
        print(f'Counter: {i}')
        current_item = data[i]
        if current_item % 2 == 0:
            print(f'Item: {current_item}')


def test_random_choice(data):
    return np.random.randint(0, len(data))


if __name__ == '__main__':
    iterate_and_print_even_items([1, 1, 1])
