import math

import numpy as np

'''
`assertIs` can be replaced with `assertTrue` in that case, can't it?
And try some other examples with numpy methods calls.

Do not hesitate to experiment with this code and tell us, if something goes wrong! 
'''


def test_positive_calculation(self, obj):
    value = obj.calculate()
    # error message in case if test case got failed
    message = "First value and second value are not evaluated to same object!"
    self.assertIs(value, True, message)


def include_revision(revision_num, skip_factor=1.1):
    if skip_factor <= 1.0:
        return True
    return (int(np.log(1 + revision_num) / math.log(skip_factor)) != int(
        np.log(revision_num + 2.0) / math.log(skip_factor)))


def arrays_processing(n: int):
    data = np.array(range(n))
    print('All the data created.')
    return np.random.randint(0, len(data))
