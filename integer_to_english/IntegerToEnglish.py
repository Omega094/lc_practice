class Solution(object):

    def __init__(self):
        self.lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        self.thousands = ["","Thousand","Million","Billion"]

    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        res = ""
        for i in range(len(self.thousands)):
            if num % 1000 != 0:
                res = self.numberToWordsHelper(num % 1000) + self.thousands[i] + " " + res
            num /= 1000
        return res.strip()

    def numberToWordsHelper(self, num):
        if num == 0:
            return ""
        if num < 20:
            return self.lessThan20[num] + " "
        if num < 100:
            return self.tens[num/10] + " " + self.numberToWordsHelper(num%10)
        else:
            return self.lessThan20[num/100] + " Hundred "+ self.numberToWordsHelper(num%100) 

#test:
if __name__ == "__main__":
    sol = Solution()
    print sol.numberToWords(12345)
