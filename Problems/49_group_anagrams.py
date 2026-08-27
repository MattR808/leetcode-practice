class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_map_list = [0] * (len(strs))
        def hash_map_maker(input_string):
                hash_map = dict()
                for i in range(len(input_string)):
                    if input_string[i] in hash_map:
                        hash_map[input_string[i]] +=1
                    else:
                        hash_map.update({input_string[i] : 1})

                return hash_map
        hash_map_tuple = dict()
        for i in range(len(strs)):
            
            hash_map_list[i] = hash_map_maker(strs[i])
            anagram_tuple = tuple(sorted(hash_map_list[i].items()))

            if anagram_tuple in hash_map_tuple:
                hash_map_tuple[anagram_tuple].append(strs[i])

            else:
                hash_map_tuple.update({anagram_tuple : [strs[i]]})
        print(hash_map_tuple)
        return list(hash_map_tuple.values())
        