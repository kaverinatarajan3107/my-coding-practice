#Given an integer n, return true if it is a power of two. Otherwise, return false.
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n>0 and bin(n).count('1')==1:
            return True
        else:
            return False
        
