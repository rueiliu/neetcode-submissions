'''
only lowercase
group by the string into sublists

create a dict
store index as keys(sorted), string as values
loop through the dict, when encounter the same keys assign them in the same sublist
save the results in res(list)

'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        sorted_dict = {}
        # 1. 建立字典
        for i in range(len(strs)):
            # 將字串排序後組合成「新字串」作為唯一的 Key
            sorted_key = "".join(sorted(strs[i]))
            
            if sorted_key not in sorted_dict:
                # 如果 Key 不存在，建立一個包含「原始字串」的 list
                sorted_dict[sorted_key] = [strs[i]]
            else:
                # 如果 Key 已經存在，直接把「原始字串」append 進去
                sorted_dict[sorted_key].append(strs[i])

        # 2. 收集結果
        # 因為字典的值 (values) 本身就是一個個分好組的 list
        # 我們直接把這些 values 倒進 res 裡面就完成了！
        for lst in sorted_dict.values():
            res.append(lst)

        return res



        