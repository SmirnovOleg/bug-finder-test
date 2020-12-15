import collections
import copy
import types

'''
Can highlighted `isinstance`-checks in the first function be replaced with `callable()`?

Do not hesitate to experiment with this code and tell us, if something goes wrong!
'''


def stream_response_to_file(response, path=None):
    pre_opened = False
    fd = None
    if path:
        if isinstance(getattr(path, 'write', None), collections.Callable):
            pre_opened = True
            fd = path
        elif isinstance(getattr(path, 'write', None), types.FunctionType):
            pre_opened = True
            fd = path
        else:
            fd = open(path, 'wb')
    else:
        header = response.headers['content-disposition']
        i = header.find('filename=') + len('filename=')
        fd = open(header[i:], 'wb')
    for chunk in response.iter_content(chunk_size=512):
        fd.write(chunk)
    if not pre_opened:
        fd.close()


def _filter_patterns(storage):
    cleared_keys = set()
    keys = sorted(storage._size_to_patterns.keys())
    for size1 in keys:
        patterns = storage._size_to_patterns[size1]
        for pattern1 in copy.copy(patterns):
            for size2 in keys:
                if size1 > size2:
                    continue
                patterns2 = storage._size_to_patterns[size2]
                found = False
                for pattern2 in patterns2:
                    if pattern2 != pattern1 and pattern2.contains(pattern1):
                        patterns.remove(pattern1)
                        storage._patterns_cnt -= 1
                        if not patterns:
                            cleared_keys.add(size1)
                        found = True
                        break
                if found:
                    break
    for k in cleared_keys:
        storage._size_to_patterns.pop(k)
    for size in range(len(storage._size_to_patterns.keys())):
        print(size)
