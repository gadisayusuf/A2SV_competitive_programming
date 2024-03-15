class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s=""
        strs.sort()
        for i in range(len(strs[0])):
            for j in range (len(strs)-1):
                if strs[j][i]!=strs[j+1][i]:
                    return s
            s=s+strs[0][i]
        return s
