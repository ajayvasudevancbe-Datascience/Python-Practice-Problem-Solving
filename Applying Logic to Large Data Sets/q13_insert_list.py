""" Question 13: insert_list """
"""
Inputs: two lists, L and K, and index i
Output: K destructively inserted into L at index i
"""
def insert_list(L, i, K):
    for x in K:
     L.append(0)
    for j in range(len(L)-1, i+len(K)-1, -1):
      L[j] = L[j-len(K)]
    for j in range(len(K)):
       L[i+j] = K[j]
""" Test 13 """
def test_insert_list():
    print("Testing insert_list...", end='')
    L = [1, 5, 6]
    K = [2, 3, 4]
    assert(insert_list(L, 1, K) == None)
    assert(L == [1, 2, 3, 4, 5, 6])
    L1 = [2, 4]
    K1 = [5, 1, 8]
    assert(insert_list(L1, 2, K1) == None)
    assert(L1 == [2, 4, 5, 1, 8])
    print("... done!")

if __name__ == '__main__':
    test_insert_list()