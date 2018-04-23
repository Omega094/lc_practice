def translate(sortedKeyVal):
    start = "0"
    resultDict = {}
    count = 1
    for c, freq in sortedKeyVal:
        resultDict[c] = start+"1"*count
        count += 1
    return resultDict

def encode(s):
    from collections import Counter
    ctr = Counter(s)
    cAndFreq = ctr.items()
    cAndFreq.sort(cmp = lambda x, y: y[1] - x[1] if x[1] !=  y[1] else  (s.find(x[0]) - s.find(y[0]))) 
    bitMap = translate(cAndFreq)
    numDistinct = len(cAndFreq)
    allKeys = map(lambda x : x[0], cAndFreq)
    cToBit = map(lambda x: bitMap[x], s)
    encodedResult = str(numDistinct) +"@#$"+ "".join(allKeys)+"@#$"+"".join(cToBit)
    return encodedResult

def decode(s):
    numDistinct, allKeys, bitStr = s.split("@#$")
    charsBit = bitStr.split("0")[1:]
    result = []
    for bit in charsBit:
        result.append(allKeys[len(bit)-1])
    return "".join(result)


#test
code = encode("hello world")
print code 
print decode(code)
