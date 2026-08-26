class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        string_x = str(x)

        return string_x == string_x[::-1]

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse = 0
        original = x
        while x >= 1:
            last_digit = x % 10
            x = x // 10

            reverse = reverse * 10 + last_digit
        
        return reverse == original





