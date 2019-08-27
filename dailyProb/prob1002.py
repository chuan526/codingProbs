# Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

# You may return the answer in any order.

 

# Example 1:

# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: ["cool","lock","cook"]
# Output: ["c","o"]

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        chr_cnt = self.cntChrs(A[0])     
        for w in A:
            new_cnt = {}
            curr_cnt = self.cntChrs(w)
            for c, cnt in curr_cnt.items():
                if c in chr_cnt: 
                    new_cnt[c] = min(cnt, chr_cnt[c]) 
            chr_cnt = new_cnt 
        res = [] 
        for c, cnt in chr_cnt.items():
            if cnt == 1: 
                res.append(c)
            else:
                for _ in range(cnt):
                    res.append(c)
        return res 

    def cntChrs(self, w: str) -> dict: 
        d = {}
        for c in w: 
            if c not in d:
                d[c] = 0
            d[c] += 1 
        return d
