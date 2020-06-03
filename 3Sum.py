class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums_list = sorted(list(nums))
        len_list = len(sorted_nums_list)
        new_list = list()

        for i,num in enumerate(sorted_nums_list):
            sum_to_search = -1*num
            j=i+1
            k=len_list-1
            while j<k:
                if sorted_nums_list[j]+sorted_nums_list[k] == sum_to_search:
                    new_list.append([num, sorted_nums_list[j], sorted_nums_list[k]])
                    j+=1
                    k-=1
                elif sorted_nums_list[j]+sorted_nums_list[k] < sum_to_search:
                    j+=1
                else:
                    k-=1
        del sorted_nums_list
        # res = list(set(tuple(item) for item in new_list))

        return list(set(tuple(item) for item in new_list))
        
