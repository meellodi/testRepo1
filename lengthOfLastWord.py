def lengthOfLastWord(s):
    if len(s) == 1:
        if s != " ":
            return 1
        else:
            return 0
    n = 0
    for i in range(len(s)-1, 0, -1):
        if s[i] != " " and s[i-1] == " ":
            return n+1
        elif s[i] != " " and s[i-1] != " ":
            n += 1
    if s[i-1] != " ":
        return n+1
    else:
        return n


print(lengthOfLastWord("s"))
print(lengthOfLastWord("s "))
print(lengthOfLastWord(" "))
print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("HelloWorld"))
print(lengthOfLastWord("Hello World  "))
print(lengthOfLastWord("   "))
