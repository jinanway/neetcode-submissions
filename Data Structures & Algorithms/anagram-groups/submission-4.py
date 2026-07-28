class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams = dict()

        for word in strs:
            counts = [0] * 26

            for c in word:
                counts[ord(c) - ord('a')] += 1
            
            if(tuple(counts) in grams):
                grams[tuple(counts)].append(word)
            else:
                grams[tuple(counts)] = [word]
            
        
        return(list(grams.values()))