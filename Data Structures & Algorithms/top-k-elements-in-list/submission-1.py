class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        result = [num for num, freq in counts.most_common(k)]
        return result