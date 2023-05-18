class Solution:
    def longestCommonPrefix(self,strs: list[str]) -> str: 
        if(len(strs) == 1): return "".join(strs)
        test=""
        sorted_list = list(sorted(strs, key=len))
        sample_one = sorted_list[0]
        count = 0     
        length_of_list = len(sorted_list)
        for i in range(0,len(sample_one)):
            sample = sample_one[0:len(sample_one)-i]
            for i in range(0, len(sorted_list)):        
                if sorted_list[i].startswith(sample):         
                    count += 1
            if(count == length_of_list):
                test = sample
                break
            else:
                count = 0  
        return test