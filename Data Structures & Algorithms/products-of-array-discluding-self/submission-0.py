class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1. My first thought is to product all nums first and divided by the current number.
        # 2. When think more, it would be a big issue if the current value is 0.
        # 3. So, we can do the same thing as step 1, but except zeros, and store the production of it.

        product = 1
        contain_zero = False
        contain_zeros = False
        for num in nums:
            if num == 0:
                if contain_zero:
                    contain_zeros = True
                contain_zero = True
            else:
                product *= num

        if contain_zeros:
            return [0] * len(nums)
        
        result = []

        for num in nums:
            if num != 0:
                if contain_zero:
                    result.append(0)
                else:
                    result.append(int(product/num))
            else:
                result.append(int(product))

        return result


