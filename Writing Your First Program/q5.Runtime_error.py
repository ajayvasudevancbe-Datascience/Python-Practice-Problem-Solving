def compute_total(total, tax):
    final = total + total * tax
    return final


print(compute_total(12, 0.05), 12.6)
print(compute_total(15, 0.07), 16.05)
print(compute_total(5.75, 0), 5.75)


""" Test 5 """
def test_compute_total():
    import math
    print("Testing compute_total...", end="")
    assert(math.isclose(compute_total(12, 0.05), 12.6))
    assert(math.isclose(compute_total(15, 0.07), 16.05))
    assert(math.isclose(compute_total(5.75, 0), 5.75))
    print("... done!")


if __name__ == '__main__':
    test_compute_total()


