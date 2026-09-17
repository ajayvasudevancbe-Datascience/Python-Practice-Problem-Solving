def find_root(a,b,c): 
    import math
    formula=(-b+ math.sqrt(b*b-4*a*c))/(2*a)
    return formula
print(find_root(1,-7,10),5)
print(find_root(1,0,-9))
print(find_root(10,-29,-21))
print(find_root(1,-2,1))
    


""" Test 3 """
def test_find_root():
    import math # we use math.isclose to compare floats
    print("Testing find_root...", end="")
    assert(math.isclose(find_root(1, -7, 10), 5))
    assert(math.isclose(find_root(1, 0, -9), 3))
    assert(math.isclose(find_root(10, -29, -21), 3.5))
    assert(math.isclose(find_root(1, -2, 1), 1))
    print("... done!")


if __name__ == '__main__':
    test_find_root()