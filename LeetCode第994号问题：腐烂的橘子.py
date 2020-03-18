# coding:utf8
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # BFS
        rot, fresh = [], []  # 腐烂和新鲜橘子点集
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.append([i, j])
                elif grid[i][j] == 2:
                    rot.append([i, j])
        if not fresh:
            return 0

        time = 0
        while rot:
            if fresh:
                new_rot = []
                while rot:
                    cur = rot.pop()
                    for i, j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        if [cur[0] + i, cur[1] + j] in fresh:
                            fresh.remove([cur[0] + i, cur[1] + j])
                            new_rot.append([cur[0] + i, cur[1] + j])
                rot = new_rot
                time += 1
            else:
                break

        return time if not fresh else -1


if __name__ == "__main__":
    s = Solution()
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print s.orangesRotting(grid)
