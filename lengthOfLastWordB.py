from tkinter import N


def lengthOfLastWord(s):
    flag = False
    n = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] != " ":
            flag = True
            n += 1
        else:
            flag = False
        if flag == False and n > 0:
            return n
    return n


print(lengthOfLastWord("s"))
print(lengthOfLastWord("b a "))
print(lengthOfLastWord(" "))
print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("HelloWorld"))
print(lengthOfLastWord("Hello World  "))
print(lengthOfLastWord("  Hello x  "))
print(lengthOfLastWord("   "))
