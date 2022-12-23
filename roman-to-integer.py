#v1 108ms
class Solution:
    def romanToInt(self, s: str) -> int:
        d = dict(M=1000,D=500,C=100,L=50,X=10,V=5,I=1)
        special = {'IV','IX','XL','XC','CD','CM'}
        res = 0
        pre = 'T'
        for e in s:
            res+=d[e]
            cache = pre+e
            if cache in special:
                res-=2*d[pre]
            pre=e
        return res
        
#v2 102ms
class Solution:
    def romanToInt(self, s: str) -> int:
        d = dict(M=1000,D=500,C=100,L=50,X=10,V=5,I=1)
        res = 0
        L = len(s)
        for i in range(L):
            if i==L-1 or d[s[i]]>=d[s[i+1]]:
                res += d[s[i]]
            else:
                res -= d[s[i]]
        return res
        
#v3 66ms
class Solution:
    def romanToInt(self, s: str) -> int:
        d = dict(M=1000,D=500,C=100,L=50,X=10,V=5,I=1)
        res = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        for e in s:
            res += d[e]
        return res
        
#v4 45ms
class Solution:
    def romanToInt(self, s: str) -> int:
        d = dict(M=1000,D=500,C=100,L=50,X=10,V=5,I=1)
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        return sum(map(d.get,s))
