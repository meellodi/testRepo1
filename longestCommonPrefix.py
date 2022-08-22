def longestCommonPrefix(strs):
    result = ""
    n = 0
    word = strs[0]
    while True:
        temp = word[0:n]
        for str in strs:
            if n == len(str)+1 or temp != str[0:n]:
                return result
        result = temp
        n += 1


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
print(longestCommonPrefix(["dog"]))
print(longestCommonPrefix([""]))
