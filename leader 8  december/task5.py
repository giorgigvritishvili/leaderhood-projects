def anagrams(str1: str, str2:str) -> bool:
    if len(str1) != len(str2):
        return False
    
    return sorted(str1) == sorted(str2)

print(anagrams("listen", "silent"))
print(anagrams("hello", "world"))
print(anagrams("triangle", "integral"))
