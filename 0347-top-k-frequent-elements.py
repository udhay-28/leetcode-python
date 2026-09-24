"""
LeetCode #347: Top K Frequent Elements
Approach: Frequency Counter Hash Map + Bucket Sort
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        freq_buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            freq_buckets[freq].append(num)

        result = []
        for i in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
    print(sol.topKFrequent([1], 1))                  # [1]