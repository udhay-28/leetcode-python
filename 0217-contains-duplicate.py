"""
LeetCode #217: Contains Duplicate
Approach: Hash Map / Dictionary Lookup
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        notebook = {}
        
        for ticket in nums:
            if ticket in notebook:
                return True
            notebook[ticket] = True
            
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1, 2, 3, 1]))  # Output: True
    print(sol.containsDuplicate([1, 2, 3, 4]))  # Output: False