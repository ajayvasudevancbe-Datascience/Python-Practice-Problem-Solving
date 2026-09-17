def box_volume(h,w,l):
    volume=h*w*l
    return volume
print(box_volume(3,4,2))
print(box_volume(2,2,2))
print(box_volume(5,2,0))

""" Test 1 """
def test_box_volume():
    print("Testing box_volume...", end="")
    assert(box_volume(3, 4, 2) == 24)
    assert(box_volume(2, 2, 2) == 8)
    assert(box_volume(5, 2, 0) == 0)
    print("... done!")

if __name__ == '__main__':
    test_box_volume()