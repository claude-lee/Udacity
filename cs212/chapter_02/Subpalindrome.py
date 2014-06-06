# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    text = text.upper()
    results = list(expand(text))
    return max(results, key=lambda (x,y):y-x)

def expand(text):
    if text == "":
        yield (0,0)
    l = len(text)
    for (i,j) in fs(text):
        while True:
            if (i <= 0 or j >= l - 1):
                yield (i,j+1)
                break
            elif (i-1 == -1 or j+1 == l or text[i-1] != text[j+1]):
                yield (i,j+1)
                break
            else:
                 i -= 1
                 j += 1
            
    
def fs(text):
    l = len(text)
    for i in range(l):
        for j in range(i+1,l):
            if text[i] == text[j] and abs(j-i) <= 2:
                print "booya", (i,j)
                yield (i,j)
                   
            
        
        
    
def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()