class Solution(object):
    def singleNumber(self, nums):
        first = True
        res = None
        for num in nums:
            if first == True:
                res = num
                first = False
            else:
                res = res ^ num
        return res
if __name__ == "__main__":
    data = [2,3,2,3,1]
    print(Solution().singleNumber(data))