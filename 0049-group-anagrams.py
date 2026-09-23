"""
LeetCode #49: Group Anagrams
Approach: Categorize by Sorted String (Hash Map Buckets)
Time Complexity: O(m * n log n) where m is word count, n is max word length
Space Complexity: O(m * n)
"""

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        
        for word in strs:
            sorted_key = "".join(sorted(word))
            
            if sorted_key not in groups:
                groups[sorted_key] = []
                
            groups[sorted_key].append(word)
            
        return list(groups.values())


if __name__ == "__main__":
    sol = Solution()
    test_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(sol.groupAnagrams(test_1))