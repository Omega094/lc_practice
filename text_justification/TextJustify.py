
class Solution(object):
    def fullJustify(self, words, maxWidth):
        #First we need to put word into each line.
        wordForEachLine = []
        currentLine = []
        if words[0] == '' and len(words) == 1: return [' '*maxWidth]
        for i, word in enumerate(words, 0):
            currentLine.append(word)
            totalLength = (sum(len(s) for s in currentLine)) + (len(currentLine) - 1) * 1
            if totalLength > maxWidth:
                currentLine.pop()
                wordForEachLine.append(currentLine)
                currentLine = [word]
            if i == len(words) - 1:
                wordForEachLine.append(currentLine)
        #now we can start to arrange each line
        finalArrangement = []
        for i, line in enumerate(wordForEachLine):
            if len(line) == 1:
                finalArrangement.append(line[0] + (maxWidth - len(line[0]))*' ')
            elif i == len(wordForEachLine)-1:
                line = ' '.join(line)
                finalArrangement.append(line + (maxWidth - len(line))*' ')
            else:
                #calculate the space width
                spaceWidth = 1
                while (len(line)-1)*spaceWidth + sum(len(s) for s in line) <= maxWidth:
                    spaceWidth += 1
                spaceWidth -= 1
                currentLine = (' '*spaceWidth).join(line)
                finalArrangement.append(currentLine)
        return finalArrangement







#test:
if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    sol = Solution()
    print sol.fullJustify(words, maxWidth)
    print sol.fullJustify([''], 0)
    print sol.fullJustify(['a'],1)
