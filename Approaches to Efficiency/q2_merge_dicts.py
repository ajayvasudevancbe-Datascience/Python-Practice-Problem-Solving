""" Question 2: merge_dicts """
"""
Input: list of dictionaries
Output: merged dictionaries where non-unique keys are mapped to sets of their
        corresponding values
"""
def merge_dicts(L):
    result = dict()
    for d in L:
        for key, value in d.items():
            if key not in result:
                result[key] = value
            elif result[key] != value:
                if isinstance(result[key], set):
                    result[key].add(value)
                else:
                    result[key] = {result[key], value}
    return result






""" Test 2 """
def test_merge_dicts():
    print("Testing merge_dicts...", end='')
    L = [{"a": 1, "b": 2, "c": 3}, {"a": 4, "b": 2, "c": 3}]
    assert(merge_dicts(L) == {"a": {1, 4}, "b": 2, "c": 3})
    assert(L == [{"a": 1, "b": 2, "c": 3}, {"a": 4, "b": 2, "c": 3}])
    L1 = [{"a": 5}, {"a": 7}, {"a": 0}]
    assert(merge_dicts(L1) == {"a": {5, 7, 0}})
    L2 = [{"d": 1, "e": 5, "f": 3, "g": 9}]
    assert(merge_dicts(L2) == {"d": 1, "e": 5, "f": 3, "g": 9})
    print("... done!")

if __name__ == '__main__':
    test_merge_dicts()