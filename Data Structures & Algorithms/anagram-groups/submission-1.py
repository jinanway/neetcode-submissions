class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        used = set()
        i = 0;
        for word1 in strs:
            words = [word1]
            j = 0;
            for word2 in strs:
                if(len(word1) == len(word2)):
                    if(i != j):
                        if(sorted(word1) == sorted(word2)):
                            words.append(word2)
                j = j + 1
            if("".join(sorted(words)) not in used):
                anagrams.append(words)
            used.add("".join(sorted(words)))
            i = i + 1
        return anagrams
                