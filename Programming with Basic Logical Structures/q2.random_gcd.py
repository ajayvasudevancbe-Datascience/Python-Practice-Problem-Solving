""" Question 2: random_gcd() """
"""
Inputs: None
Output: randomly generates two integers in range [1, 100] and returns gcd
"""
import random 
import math
def random_gcd():
  A=random.randint(1,100)
  B=random.randint(1,100)
  print("Number",A,B)
  result=math.gcd(A,B)
  return result
""" Test 2 """
def test_random_gcd():
    print("Testing random_gcd...")
    # Check whether the result is actually the GCD of the two printed numbers
    result = random_gcd() # should print x and y
    print("gcd:", result) # prints the result
    print("... done!")

if __name__ == '__main__':
    test_random_gcd()