
def vowels(word):
    new = []
    vowel= ['a','e','i','o','u']
    for i in word:
        if i.lower() not in vowel:
            new.append(i)
    return ', '.join(new)
print(vowels('HELLO'))

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
"l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,"r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,"x": 8, "z": 10}
def sum_score(word):
    sum = 0
    word = word.lower()
    for i in word:
        sum = sum + score[i]
        return sum
response.geturl()
response.info()


def median(s):
    n = len(s)
    if n == 1:
        return s [0]
    elif n%2 == 1:
        m = sorted(s)
        mid = m[(n-1)//2]
        return mid
    else:
        m = sorted(s)
        mid = float(m[n//2-1]+m[n//2])/2
        return mid
def median(s):
    n = len(s)
    m = sorted(s)
    if n == 1:
        return s[0]
    elif n%2 == 1:
        mid = [(n-1)/2]
        return mid
    else:
        mid = float(m[(n-1)/2]+m[n/2])/2
        return mid
