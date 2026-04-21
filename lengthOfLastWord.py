class Solution(object):
    def lengthOfLastWord(self, s):
#        words = s.split()
#        if not words:
#            return 0
#        return len(words[-1])

        i=len(s)-1
        lenth=0
        while i>=0 and s[i] ==   " ":
            i-=1
        while i>=0 and s[i]!= " ":
            lenth+=1
            i-=1
        return lenth


print(Solution().lengthOfLastWord("   fly me   to   the moon  "))