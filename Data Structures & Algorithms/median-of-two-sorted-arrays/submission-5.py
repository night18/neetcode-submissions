class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        median 的本質不是「排序後的中間值」，是把 m+n 個數切成左右兩半：左半 (m+n+1)//2 個，右半剩下的
        且 max(左) ≤ min(右)。median 只由切線兩側的至多四個數決定。

        現在換個座標：如果我在 nums1 切在位置 i(左邊拿 i 個)、nums2 切在位置 j
        那 i + j 必須等於 (m+n+1)//2 —— 所以 j 由 i 完全決定，自由度只有一個。整題塌縮成：在 [0, m] 裡找一個正確的 i。
        """

        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        
        total_len = len(A) + len(B)
        half = (len(A)+len(B)) // 2

        l , r = 0 , len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            """
            提示：左邊的東西不能大於右邊的東西，寫成兩個不等式
            """
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if (i + 1) < len(A) else float("inf")

            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total_len % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
