class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        wordList = {} # key: sorted string # value: list of anagram words

        for s in strs:
            
            key = "".join(sorted(s))

            if key not in wordList:
                wordList[key]= []
            wordList[key].append(s)
        
        return list(wordList.values())

                