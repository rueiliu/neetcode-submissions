'''
only lowercase
group by the string into sublists


'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for s in string:
                count[ord(s) - ord("a")] += 1
            sorted_dict[tuple(count)].append(string)

        return list(sorted_dict.values())
    


        