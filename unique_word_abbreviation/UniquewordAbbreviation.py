class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        from collections import defaultdict
        self.wordDict = defaultdict(set)
        pairs = zip(dictionary, map(lambda x : self.abbreviate(x), dictionary))
        for pair in pairs:
            self.wordDict[pair[1]].add(pair[0])
        
    def abbreviate(self, word):
        if len(word) > 2: 
            number = (len(word[1:-1]))
            if number == 0:
                abb = ""
            else:
                abb = str(number)
            word = word[0] + abb + word[-1]
        return word

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        return self.abbreviate(word) not in self.wordDict or ( word in self.wordDict[self.abbreviate(word)] and len(self.wordDict[self.abbreviate(word)]) == 1)


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
