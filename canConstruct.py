def canConstruct(ransomNote, magazine):
    magazineDict = {}
    for char in magazine:
        if char in magazineDict:
            magazineDict[char] += 1
        else:
            magazineDict[char] = 1
    for char in ransomNote:
        if char not in magazineDict or magazineDict[char] == 0:
            return False
        else:
            magazineDict[char] -= 1
    return True


print(canConstruct("abcdefhafss", "x"))
print(canConstruct("a", "a"))
print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))
