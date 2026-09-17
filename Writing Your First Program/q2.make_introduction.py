def make_introduction(name,hobby):
    Introduction= f"My name is {name} and I like {hobby}"
    return Introduction
print(make_introduction("shriman", "cricket"))
""" Test 2 """
def test_make_introduction():
    print("Testing make_introduction...", end="")
    assert(make_introduction("shriman", "cricket") == "My name is shriman and I like cricket")
    assert(make_introduction("pranav", "cricket") == "My name is pranav and I like cricket")
    assert(make_introduction("Rei", "reading") == "My name is Rei and I like reading")
    assert(make_introduction("Govind", "dancing") == "My name is Govind and I like dancing")
    print("... done!")

if __name__ == '__main__':
    test_make_introduction()
    
    