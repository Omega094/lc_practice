class check(s, word):
    from collections import Counter
    wordCounter = Counter(word)
    wordType = len(wordCounter)
    wordLength = len(word)
    need = wordLength 
    currentCounter = Counter()
    for i ,c in enumerate(s):
        if i < wordLength:
            if c in wordCounter: 
                currentCounter[c] += 1
                if currentCounter[c] == wordCounter[c] :
                    wordType -= 1
        else:
            if wordType == 0:
                return True
            if c in currentCounter:
                currentCounter[c] += 1
                if currentCounter[c] == wordCounter[c]:
                    wordType -= 1
            if s[i-wordLength] in currentCounter:
                currentCounter[s[i-wordLength]]-=1
                if currentCounter[s[i-wordLength]] < wordCounter[s[i-wordLength]]:
                    wordType -= 1
                if currentCounter[s[i-wordLength]] == 0:
                    del currentCounter[s[i-wordLength]]
    return False


