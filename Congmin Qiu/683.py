class Solution2:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        [1, 6, 3, 2, 4, 5]
        """

        l = len(flowers)
        start = (0, l+1)
        diff = k+1
        intervals = set([start])

        for i, pos in enumerate(flowers):
            temp = None

            





class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """

        days = [0] * len(flowers)
        # 第i天开第day[i]朵花


        for i in range(len(flowers)):
            days[flowers[i] - 1] = i + 1

        print(days)
        print(flowers)
        left = 0
        right = k + 1
        res = 9999
        i = 0
        while right < len(days):
            print("i = {} - {} - {} - {}".format(i, days[i], days[left], days[right]))
            if days[i] < days[left] or days[i] <= days[right]:
                if i == right:
                    res = min(res, max(days[left], days[right]))
                left = i
                right = k + 1 + i

            i += 1

        if res == 9999:
            return -1
        return res


s = Solution()
input = None
res = s.kEmptySlots([1, 6, 3, 2, 4, 5], 2)

print("")