class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        i=0
        j=0
        max=1
        while(i<=j and j< len(s)-1):
            tmp= s[i:j+1]
            if s[j+1] not in tmp:
                j=j+1
                if len(tmp)+1>max:
                    max= len(tmp)+1
            else:
                i=i+1
                if j<i:
                    j=j+1
        return max
if __name__ == '__main__':
    sol=Solution()
    print(sol.lengthOfLongestSubstring("pwwkew"))