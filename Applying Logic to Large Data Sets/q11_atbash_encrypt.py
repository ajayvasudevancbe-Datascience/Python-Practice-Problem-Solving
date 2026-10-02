""" Question 11: atbash_encrypt """
"""
Input: string
Output: string encoded using atbash encryption
"""
import string
def atbash_encrypt(message):
    result=""
    for ch in message:
     if ch.islower():
      alpha=string.ascii_lowercase
      result+=alpha[25-alpha.index(ch)]
     elif ch.isupper():
       alpha=string.ascii_uppercase
       result+=alpha[25-alpha.index(ch)]
     else:
       result+=ch
    return result
    

""" Test 11 """
def test_atbash_encrypt():
    print("Testing atbash_encrypt...", end='')
    assert(atbash_encrypt("Hello") == "Svool")
    assert(atbash_encrypt("night!") == "mrtsg!")
    assert(atbash_encrypt("Coding is fun :)") == "Xlwrmt rh ufm :)")
    assert(atbash_encrypt("") == "")
    print("... done!")

if __name__ == '__main__':
    test_atbash_encrypt()