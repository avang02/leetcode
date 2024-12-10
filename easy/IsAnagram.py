# Is Anagram

# Given two strings 's' and 't', return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true

# Example 2:
# Input: s = "jar", t = "jam"
# Output: false

# Constraints:
# s and t consist of lowercase English letters.

string1 = {
    's': "racecar", 
    't': "carrace"
}
string2 = {
    's': "jar", 
    't': "jam"
}

def isAnagram(sObj):
    if len(sObj['s']) != len(sObj['t']):
        return False
    hashset1, hashset2 = {}, {}
    getRange = len(sObj['s'])
    for i in range(getRange):
        hashset1[sObj['s'][i]] = 1 + hashset1.get(sObj['s'][i], 0)
        hashset2[sObj['t'][i]] = 1 + hashset2.get(sObj['t'][i], 0)
    for c in hashset1:
        if hashset1[c] != hashset2.get(c, 0):
            return False
    return True

print(isAnagram(string1))
print(isAnagram(string2))
