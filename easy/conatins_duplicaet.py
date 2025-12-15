class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        if len(set(nums)) - len(nums):
            return True
        else:
            return False
        # set deosnt allow duplicate items, so we know we have all unique fales in set(nums)
        # if it differs from len(nums), some values appeared more than once