class Solution(object):
    def leastInterval(self, tasks, n):
        freq = [0] * 26

        for t in tasks:
            freq[ord(t) - ord('A')] += 1

        m = max(freq)
        c = freq.count(m)

        return max(len(tasks), (m - 1) * (n + 1) + c)