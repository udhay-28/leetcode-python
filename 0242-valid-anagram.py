"""
LeetCode #242: Valid Anagram
Approach: Hash Map Frequency Counter
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        counts = {}
        
        for char in s:
            counts[char] = counts.get(char, 0) + 1
            
        for char in t:
            if char not in counts or counts[char] == 0:
                return False
            counts[char] -= 1
            
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # True
    print(sol.isAnagram("rat", "car"))          # False
    print(sol.isAnagram("cct", "ctc"))          # True
    print(sol.isAnagram("cct", "cat"))          # False