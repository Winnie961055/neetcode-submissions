class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ## Bucket Sort
        
        count = {} # num : count
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1 # 假設：count = {}，如果直接count[1] --> KeyError: 1 --> 所以要用count.get(key, 預設值)
        for n, c in count.items():
            freq[c].append(n)

        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans