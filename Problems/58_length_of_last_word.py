class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        reverse_s = s[::-1]
        count = 0

        for char in reverse_s:            

            if char.isalpha():
                count +=1
            elif char.isspace() and count != 0:
                return count
            
        return count

        