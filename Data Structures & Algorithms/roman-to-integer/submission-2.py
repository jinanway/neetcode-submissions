class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        i = 0
        while(i < len(s)):
            if s[i] == "I":
                if(i < len(s) - 1):
                    if(s[i + 1] == "V"):
                        sum += 3
                        i += 1
                    elif(s[i + 1] == "X"):
                        sum += 8
                        i += 1
                sum += 1
            elif s[i] == "V":
                sum += 5
            elif s[i] == "X":
                if(i < len(s) - 1):
                    if(s[i + 1] == "L"):
                        sum += 30
                        i += 1
                    elif(s[i + 1] == "C"):
                        sum += 80
                        i += 1
                sum += 10
            elif s[i] == "L":
                sum += 50
            elif s[i] == "C":
                if(i < len(s) - 1):
                    if(s[i + 1] == "D"):
                        sum += 300
                        i += 1
                    elif(s[i + 1] == "M"):
                        sum += 800
                        i += 1
                sum += 100
            elif s[i] == "D":
                sum += 500
            elif s[i] == "M":
                sum += 1000
            i += 1

        return sum    
            

                    