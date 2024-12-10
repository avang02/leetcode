from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1 # subtracts the ASCII value of letters to get the List index

            res[tuple(count)].append(s) # Only in python we need to worry about the tuple(count)
        return res.values()
    
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat", "nate", "eant", "tean", "meremortal", "mortalmere"]

solution = Solution()
result = solution.groupAnagrams(strs)
result1 = solution.groupAnagrams(strs1)

print(result)
print(result1)

