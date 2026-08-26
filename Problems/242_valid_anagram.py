class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        else:
            def hash_map_maker(input_string):
                hash_map = dict()
                for i in range(len(input_string)):
                    if input_string[i] in hash_map:
                        hash_map[input_string[i]] +=1
                    else:
                        hash_map.update({input_string[i] : 1})

                return hash_map
        return hash_map_maker(s) == hash_map_maker(t)
