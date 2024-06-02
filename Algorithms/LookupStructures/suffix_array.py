"""
Suffix Array

"""

class SuffixArray:
    def __init__(self, string):
        """
        Constructs a suffix array, an array of sorted suffixes, represented as starting indices using
        Prefix Doubling Algorithm.

        Time complexity:
            Since we double the number of letters checked every iteration, in total we will have log(N) iterations.
            Each iteration, we perform a sorting based on the rank.
                If using merge-sort, this would be O(N*Log(N)) * O(Log(N)) = O(N*Log(N)^2)
                If using radix-sort, this would be O(N) * O(Log(N)) = O(N*Log(N))
        
                
        Space complexity: O(N)

        """
        self.string = string
        n = len(string)
        self.suffix_arr = list(range(n))
        self.rank = [ord(string[i]) for i in self.suffix_arr]
        
        k =  1
        while k < n:
            # # 1. Sort using merge sort
            # self.suffix_arr = self.merge_sort(self.suffix_arr, k)

            # 1. or using radix sort
            self.suffix_arr = self.radix_sort(self.suffix_arr, k)

            # 2. Update rank array based on new sorted order
            temp = [0]*n
            for i in range(n-1): # note that the first one is skipped because by default the rank is 0
                temp[self.suffix_arr[i+1]] = temp[self.suffix_arr[i]] + self.compare(k, self.suffix_arr[i], self.suffix_arr[i+1])
            self.rank = temp

            k *= 2
        
        # construct LCP array?
        self.lcp = None
        


    def compare(self, k, i, j):
        """
        Compares suffix at index i and suffix at index j, 
        returns True is suffix i < suffix j for the first 2*k characters

        Time complexity: O(1)
        """

        n = len(self.rank)
        if self.rank[i] != self.rank[j]: # if first halves are not equal, just compare first halves
            return self.rank[i] < self.rank[j]
        elif i+k < n and j+k < n: # compare second halves if first halves have equal rank
            return self.rank[i+k] < self.rank[j+k]
        else: # if second half does not have enough letters
            return i > j # if suffix i starts later (shorter) than suffix j 
            
        

    def merge_sort(self, nums, k):
        if len(nums) <= 1: # base case only 1 element left
            return nums # already sorted
        else: # more than 1 element left in sub-array, keep splitting
            mid = len(nums)//2
            left = self.merge_sort(nums[:mid], k) # returns left half sorted
            right = self.merge_sort(nums[mid:], k) # returns right half sorted
            return self.merge(left, right, k) # merge 2 halves
    
    def merge(self, left, right, k):
        l = 0
        r = 0
        merged = []
        while l <= len(left)-1 or r <= len(right)-1:
            if l >= len(left): # left arr empty
                merged.append(right[r])
                r += 1
            elif r >= len(right): # right arr empty
                merged.append(left[l])
                l += 1
            else:
                if self.compare(k, left[l], right[r]):
                    merged.append(left[l])
                    l += 1
                else:
                    merged.append(right[r])
                    r += 1
        return merged
    
    def radix_sort(self, nums, k):
        """
        Radix sort first sorting the second half of the string ranks, then the first half
        """
        n = len(nums)
        # assinging second half rank to suffix id
        rank_and_id = []
        for i in range(n):
            if nums[i] + k < n:
                # shifting all the actual ranks by n+1 so that we can assign ranks based on length if second half is empty
                rank_and_id.append((self.rank[nums[i] + k]+n+1, nums[i])) 
            else: # if second half doesn't have enough letters
                # assign rank as the length of suffix -1, n-num[i]
                rank_and_id.append((n-nums[i], nums[i]))
        # sorting second half
        nums = self.counting_sort(rank_and_id)

        # assinging first half rank to suffix id
        rank_and_id = []
        for i in range(n):
            rank_and_id.append((self.rank[nums[i]], nums[i]))

        # sorting first half
        return self.counting_sort(rank_and_id)


    def counting_sort(self, nums):
        """
        Counting sort for sorting "zipped" items based on the first index
        Input:
            nums: A list of tuples (key, item)
        """
        if len(nums) == 0:
            return []
        
        max_rank = 0
        # find the nums range
        for rank, _ in nums:
            max_rank = max(max_rank, rank)

        counter = [0] * (max_rank + 1) #O(u) space

        # count occurence of each number
        for rank, _ in nums: # O(N) time
            counter[rank] += 1
        
        # calculate starting indexs of each number - optimized space
        prev = counter[0]
        counter[0] = 0
        for i in range(1, len(counter)): #O(u) time
            temp = counter[i]
            counter[i] = prev + counter[i-1]
            prev = temp

        # sort array
        res = [0] * len(nums) # O(n) space
        for rank, suffix_id in nums:
            res[counter[rank]] = suffix_id
            counter[rank] += 1
        return res
    
    def print_suffixes(self):
        print("")
        for i in self.suffix_arr:
            print(self.string[i:])