def halvesAreAlike(s):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    l = len(s)//2
    sum = 0
    for i in range(l):
        if s[i] in vowel:
            sum += 1
        if s[l*2-1-i] in vowel:
            sum -= 1
    return True if sum == 0 else False


print(halvesAreAlike("ab"))
print(halvesAreAlike("book"))
