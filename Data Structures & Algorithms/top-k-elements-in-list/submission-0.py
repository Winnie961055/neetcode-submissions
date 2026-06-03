class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashMap = {}

        for i in nums:

            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] += 1
        
        pair = list(hashMap.items())
        pair.sort(key=lambda pair: pair[1], reverse=True)

        ans = []

        for num, freq in pair[:k]:
            ans.append(num)

        return ans
