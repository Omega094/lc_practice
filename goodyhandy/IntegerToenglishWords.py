class Solution(object):
    def __init__(self):
        self.lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        self.thousands = ["","Thousand","Million","Billion"]

    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        result = ""
        for thousand in self.thousands:
            current = num % 1000
            if current != 0:
                result = self.toEnglishUnderThousand(current) +" " + thousand +" "+ result
            num = num // 1000
 
        return result.strip()

    def toEnglishUnderThousand(self, num):
        if num == 0: return ""
        if num < 20:
            return self.lessThan20[num]
        if num < 100:
            if num%10 == 0: return self.tens[num/10]
            return self.tens[num/10] + " " + self.toEnglishUnderThousand(num%10)
        if num % 100 == 0: return  self.lessThan20[num//100] + " Hundred"
        return self.lessThan20[num//100] + " Hundred " + self.toEnglishUnderThousand(num%100)

#test
sol = Solution()
print sol.toEnglishUnderThousand(999)
print sol.numberToWords(9999888888)
print sol.numberToWords(999)
print sol.numberToWords(9999)
