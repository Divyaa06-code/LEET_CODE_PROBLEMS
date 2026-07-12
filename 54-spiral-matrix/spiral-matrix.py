class Solution(object):
    def spiralOrder(self, matrix):
        res = []

        while matrix:
            res += matrix.pop(0)

            for row in matrix:
                if row:
                    res.append(row.pop())

            if matrix:
                res += matrix.pop()[::-1]

            for row in matrix[::-1]:
                if row:
                    res.append(row.pop(0))

        return res