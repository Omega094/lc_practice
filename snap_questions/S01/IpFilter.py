def EightDigitBinary(num):
    result = ""
    for i in xrange(8):
        result = str(num  & 1)+result
        num = num >> 1
    return result 
    
def ipToBit(ipStr):
    ipStr = map(int, ipStr.split("."))
    addressBitStr = "".join(map(EightDigitBinary, ipStr))
    return addressBitStr  



def addressToStrNeeded(ipList):
    result = []
    print ipList, "$"*100
    for ip in ipList:
        print ip.split("/")
        address, numBit = ip.split("/")
        #Convert address into bit
        address = address.split(".")
        addressNum = map(int, address)
        print addressNum
        addressNum = "".join(map(EightDigitBinary, addressNum)) 
        print addressNum
        result.append(addressNum[:int(numBit)])
    print result, "Here are result s"
    return result




def storeBadIp(ipList):
    trie = {}
    ipStrList = addressToStrNeeded(ipList)
    for ipStr in ipStrList:
        currentTrieNode = trie 
        for c in ipStr:
            if c not in currentTrieNode:
                currentTrieNode[c] = {}
            currentTrieNode = currentTrieNode[c]
        currentTrieNode["#"] = {} 
    return trie

def isBadIp(ip, trie):
    currentTrieNode = trie
    ipStr = ipToBit(ip)
    print ipStr, "*"*10
    print trie
    for c in ipStr:
        print c, currentTrieNode
        if currentTrieNode.has_key("#"): return True 
        if not currentTrieNode.has_key(c): return False
        currentTrieNode =  currentTrieNode[c]
    return currentTrieNode.has_key("#")


#test 
#ipStr = addressToStrNeeded(["7.0.0.0/8", "10.3.0.0/16", "6.7.8.134/32"])
#print ipStr
#print ipToBit("7.0.0.0")

ipList = ["7.0.0.0/8"]
trie = storeBadIp(ipList)
print isBadIp("7.3.4.5", trie)
