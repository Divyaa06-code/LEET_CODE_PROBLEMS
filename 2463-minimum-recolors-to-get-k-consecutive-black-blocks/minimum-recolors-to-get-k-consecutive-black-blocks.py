class Solution(object):
    def minimumRecolors(self, blocks, k):
        white = blocks[:k].count('W')
        ans = white

        # Slide the window
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                white -= 1
            if blocks[i] == 'W':
                white += 1

            ans = min(ans, white)

        return ans