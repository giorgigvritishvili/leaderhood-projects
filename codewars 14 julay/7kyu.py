
def is_anagram(test, original):
    test =test.lower()
    original = original.lower()
    
    sorted_str1 = sorted(test)
    sorted_str2 = sorted(original)
    
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False