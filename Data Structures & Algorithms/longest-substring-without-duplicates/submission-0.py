class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_length = 0
        start = 0
        
        for end in range(len(s)):
            current_char = s[end]
            
            if current_char in char_map and char_map[current_char] >= start:
                start = char_map[current_char] + 1
                
            char_map[current_char] = end
            max_length = max(max_length, end - start + 1)
            
        return max_length