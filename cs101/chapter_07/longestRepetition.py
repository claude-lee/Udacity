# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(things):
    length = len(things)
    if not length:
        return None
    max_element = things[0]
    current_element = things[0]
    i = 1
    max_count = 1
    current_count = 1
    while i < length:
        if things[i] == current_element:
            current_count += 1
        elif current_count > max_count:
            max_count = current_count
            current_count = 1
            max_element = current_element
            current_element = things[i]
        current_element = things[i]
        i+=1
    return max_element if max_count >= current_count else current_element



#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([2, 2, 3, 3, 3])
# 3

print longest_repetition([2, 2, 2, 3, 3, 3])
