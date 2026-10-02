
""" Question 7: generate_inputs """
"""
Input: integer n
Output: 2D list containing all combinations of n 0s and 1s
"""
def generate_inputs(n):
    if n==0:
        return [[]]
    else:
        result=[]
        partial_result=generate_inputs(n-1)
        for lst in partial_result:
            result.append(lst+[0])
            result.append(lst+[1])
    return result

""" Test 7 """
def test_generate_inputs():
    print("Testing generate_inputs...", end="")
    assert(sorted(generate_inputs(3)) == [ [0,0,0], [0,0,1], [0,1,0], [0,1,1],
                                           [1,0,0], [1,0,1], [1,1,0], [1,1,1] ])
    assert(sorted(generate_inputs(1)) == [ [0], [1] ])
    assert(sorted(generate_inputs(5)) == [ [0,0,0,0,0], [0,0,0,0,1], [0,0,0,1,0], [0,0,0,1,1],
                                           [0,0,1,0,0], [0,0,1,0,1], [0,0,1,1,0], [0,0,1,1,1],
                                           [0,1,0,0,0], [0,1,0,0,1], [0,1,0,1,0], [0,1,0,1,1],
                                           [0,1,1,0,0], [0,1,1,0,1], [0,1,1,1,0], [0,1,1,1,1],
                                           [1,0,0,0,0], [1,0,0,0,1], [1,0,0,1,0], [1,0,0,1,1],
                                           [1,0,1,0,0], [1,0,1,0,1], [1,0,1,1,0], [1,0,1,1,1],
                                           [1,1,0,0,0], [1,1,0,0,1], [1,1,0,1,0], [1,1,0,1,1],
                                           [1,1,1,0,0], [1,1,1,0,1], [1,1,1,1,0], [1,1,1,1,1] ])
    print("... done!")



if __name__ == '__main__':
    test_generate_inputs()
