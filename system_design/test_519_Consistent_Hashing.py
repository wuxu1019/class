class Solution:
    """
    @param: n: a positive integer
    @return: n x 3 matrix
    """

    def consistentHashing(self, n):
        # write your code here

        rt = [[0, 359, 1]]
        for i in range(1, n):
            index = 0
            for j in range(i):
                if rt[j][1] - rt[j][0] > rt[index][1] - rt[index][0]:
                    index = j
                elif rt[j][1] - rt[j][0] == rt[index][1] - rt[index][0] and rt[j][2] < rt[index][2]:
                    index = j
            x, y = rt[index][0], rt[index][1]
            rt[index][1] = (x + y) / 2
            rt.insert(index + 1, [(x + y) / 2 + 1, y, i + 1])
        return rt

if __name__ == '__main__':
    s = Solution()
    rt1 = s.consistentHashing(4)
    print rt1