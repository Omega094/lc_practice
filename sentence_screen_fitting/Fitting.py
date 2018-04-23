class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        times = [0] * len(sentence)
        nextWord = [None] * len(sentence)
        for i, w in enumerate(sentence):
            index = i
            currentLen = 0
            time = 0
            while cols >= len(sentence[index]) + currentLen:
                currentLen += len(sentence[index]) + 1
                index += 1
                if index == len(sentence):
                    index = 0
                    time += 1
            times[i] = time
            nextWord[i] = index
        res = 0
        next = 0
        for i in xrange(0, rows):
            res += times[next]
            next = nextWord[next]
        return res
        
        
        
        
