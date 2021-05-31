import collections
import os

import numpy as np


def test_log(x):
    return np.log(1 + np.abs(x))


def test_callable(self):
    func_attr = getattr(self, 'func')
    print(func_attr)
    return isinstance(func_attr, collections.Callable)


def test_dict_keys(self):
    sorted_keys = sorted(self.vocab.keys())
    return sorted_keys


def test_arange(n):
    return np.array(range(n))


def test_assert(self, x):
    self.assertIs(x, True)


def test_os_path_exists(path):
    return os.path.exists(path)


def iterate_and_print_even_items():
    data = [1, 2, 3]
    print('Start working...')
    for i in range(len(data)):
        print(f'Counter: {i}')
        current_item = data[i]
        if current_item % 2 == 0:
            print(f'Item: {current_item}')


if __name__ == '__main__':
    iterate_and_print_even_items()
