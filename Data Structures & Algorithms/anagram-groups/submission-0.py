class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for s in strs: 
            key = [0]*26 
            for c in s.lower(): 
                idx = ord(c) - ord('a')
                key[idx] +=1 
            freq[tuple(key)].append(s)
        
        return list(freq.values())
