class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict = {}
        for word in words:
            dict[word] = dict.get(word, 0) + 1
        
        dic = []
        for key, val in dict.items():
            heapq.heappush(dic, (-val, key))
                       
        res = []
        for _ in range(k):
            res.append(heapq.heappop(dic)[1])
        return res
