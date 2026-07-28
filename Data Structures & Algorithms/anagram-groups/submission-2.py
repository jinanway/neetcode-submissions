class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams = dict()
        for i in strs:
            word = list(i)
            word.sort()
            word = "".join(word)
            if(word not in grams):
                grams[word] = [i]
            else:
                grams[word].append(i)
    
        return list(grams.values())